#!/usr/bin/env python3
"""Fetch item-type icons from the Fandom wiki and render them to PNG.

Monster Hunter's item icons are *generic per type*, not per item: every
"Scale" shares one scale illustration, every "Hide" one hide, and so on,
colored by rarity. The Fandom wiki hosts these as a clean SVG set under
Category:5th_Generation_Item_Icons (covering MHW + Wilds). This pulls the SVGs
into source/item-icons/ and writes a manifest the build joins items against by
{kind, color}; rendering to PNG happens at build time (build.py's copy_icon),
so this step stores only the SVG source.

The SVGs are community-drawn generic art, not CAPCOM assets, so they're
vendored into the repo directly (unlike CAPCOM monster icons which stay
gitignored). Change detection uses the Fandom CDN's ETag: each re-run sends
If-None-Match per icon, so an unchanged SVG returns 304 with no body and costs
no bandwidth, keeping periodic re-fetches cheap and polite to the wiki.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Reuse the Fandom crawl plumbing from fetch_external rather than duplicate it.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_external import (  # noqa: E402
    BROWSER_UA,
    TIMEOUT,
    fandom_file_urls,
    fandom_list_files,
)

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
OUT_DIR = SOURCE / "item-icons"  # committed: SVGs + manifest (PNGs rendered at build time)
MANIFEST = OUT_DIR / "_manifest.json"

ITEM_ICONS_CAT = "Category:5th_Generation_Item_Icons"

# Known color words used as the rarity tier suffix in the Fandom filenames.
# The longest matches first so "Dark Blue" wins over a trailing "Blue".
COLORS = [
    "Dark Blue", "Dark Green", "Dark Purple", "Dark Red", "Dark Teal",
    "Blue Purple", "Moss Green", "Sage Green", "Deep Teal", "Light Brown",
    "Light Green", "Dark Gray", "Ultramarine", "Lemon",
    "Blue", "Brown", "Gold", "Green", "Grey", "Orange", "Pink", "Purple",
    "Red", "Teal", "White", "Yellow", "Gray", "Black", "Silver", "Ivory",
    "Rose", "Vermilion", "Sky", "Emerald",
]
_COLOR_RE = "|".join(re.escape(c) for c in sorted(COLORS, key=len, reverse=True))


def slugify(s: str) -> str:
    """Lowercase, spaces/hyphens to single hyphen, strip non-alnum-hyphen."""
    s = s.strip().lower()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"[^a-z0-9-]", "", s)
    return s.strip("-")


def parse_kind_color(wiki_title: str) -> tuple[str, str] | None:
    """Split a 'File:5thGen Item Icon-{Type} {Color}.svg' into (kind, color).

    Returns None if the filename doesn't match the expected shape.
    """
    # Strip namespace + prefix + extension.
    name = wiki_title.split(":", 1)[-1]  # drop "File:"
    name = re.sub(r"^5thGen Item Icon-", "", name)
    name = re.sub(r"\.(svg|png|jpg)$", "", name, flags=re.I)
    # Match a trailing color; everything before it is the kind.
    m = re.search(r"\s(" + _COLOR_RE + r")$", name, flags=re.I)
    if not m:
        return None
    kind = name[: m.start()].strip()
    color = m.group(1)
    if not kind:
        return None
    return kind, color


def fetch_with_etag(url: str, etag: str | None) -> tuple[bytes | None, str | None, int]:
    """GET a URL with an If-None-Match precondition, via curl.

    curl is used (rather than requests) because the Fandom CDN only returns an
    ETag over HTTP/2, which requests doesn't speak; curl negotiates HTTP/2 and
    gets the header. The `?cb=…` query param that MediaWiki appends suppresses
    the ETag, so callers pass the bare /revision/latest URL (cb stripped).

    Returns (body, new_etag, status). On a 304 the body is None and the etag is
    unchanged; on 200 the body is the new bytes and etag is the new value.
    Network/HTTP errors return (None, etag, 0) so the caller can fall back to
    the SVG already on disk.
    """
    cmd = ["curl", "-sS", "--http2", "-A", BROWSER_UA,
           "--max-time", str(TIMEOUT), "-D", "-", "-o", "-", url]
    if etag:
        cmd.insert(-3, "-H")  # before the url positional
        cmd.insert(-3, f"If-None-Match: {etag}")
    try:
        proc = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT + 10)
    except subprocess.TimeoutExpired:
        return None, etag, 0
    raw = proc.stdout
    # curl with -D - writes headers then a blank line then the body. Split on
    # the first blank line (\r\n\r\n over HTTP/2).
    sep = raw.find(b"\r\n\r\n")
    head = raw[:sep].decode("utf-8", "replace") if sep != -1 else ""
    body = raw[sep + 4:] if sep != -1 else b""
    sm = re.search(r"(?im)^HTTP/\S+\s+(\d+)", head)
    status = int(sm.group(1)) if sm else 0
    em = re.search(r"(?im)^etag:\s*(.+)$", head)
    new_etag = em.group(1).strip() if em else None
    if status == 304:
        return None, etag, 304
    if status == 200:
        return body, new_etag, 200
    return None, etag, status


def main() -> int:
    print("== item icons ==")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("  listing Category:5th_Generation_Item_Icons ...")
    titles = fandom_list_files(ITEM_ICONS_CAT)
    print(f"  {len(titles)} files listed")

    # Filter to the named-shape icons we can parse; skip stray uploads.
    parsed: list[tuple[str, str, str]] = []  # (wiki_title, kind, color)
    skipped = 0
    for t in titles:
        kc = parse_kind_color(t)
        if kc is None:
            skipped += 1
            continue
        parsed.append((t, kc[0], kc[1]))
    print(f"  {len(parsed)} parse as Type+Color ({skipped} skipped)")

    print("  resolving image URLs ...")
    urls = fandom_file_urls([t for t, _, _ in parsed])

    # Load the prior manifest keyed by SVG filename, so we can send the stored
    # ETag and skip re-downloading unchanged SVGs.
    prior: dict[str, dict] = {}
    if MANIFEST.exists():
        data = json.loads(MANIFEST.read_text())
        for rec in data.get("icons", data if isinstance(data, list) else []):
            prior[rec["svg"]] = rec

    manifest: list[dict] = []
    changed = 0   # SVG was new or updated
    cached = 0    # 304 Not Modified → kept existing SVG
    failed = 0
    for wiki_title, kind, color in parsed:
        url = urls.get(wiki_title)
        if not url:
            continue
        kind_slug = slugify(kind)
        color_slug = slugify(color)
        svg_name = f"{kind_slug}-{color_slug}.svg"
        svg_path = OUT_DIR / svg_name

        prev = prior.get(svg_name)
        # The `?cb=…` version param MediaWiki appends suppresses the ETag, so
        # fetch the bare /revision/latest URL (cb is just a cache-buster).
        clean_url = url.split("?")[0]
        body, new_etag, status = fetch_with_etag(clean_url, prev.get("etag") if prev else None)

        if status == 304:
            # Unchanged: keep the SVG on disk, carry forward the etag.
            cached += 1
        elif body is not None:
            # New or updated SVG: persist it.
            svg_path.write_bytes(body)
            changed += 1
        else:
            # Network/HTTP failure. Fall back to the SVG on disk if we have one;
            # otherwise this icon is dropped from the manifest.
            if svg_path.exists():
                print(f"    ! fetch {wiki_title} (status {status}); keeping stale SVG")
            else:
                print(f"    ! fetch {wiki_title} (status {status}); no SVG, skipping")
                failed += 1
                continue

        manifest.append({
            "kind": kind_slug,
            "color": color_slug,
            "svg": svg_name,
            "source_url": url,
            "source_title": wiki_title,
            "etag": new_etag,
        })

    manifest_with_meta = {
        "source": "monsterhunter.fandom.com/Category:5th_Generation_Item_Icons",
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "icon_count": len(manifest),
        "icons": manifest,
    }
    MANIFEST.write_text(json.dumps(manifest_with_meta, ensure_ascii=False, indent=2))
    print(f"  changed/new: {changed}, unchanged (304): {cached}")
    if failed:
        print(f"  failed: {failed}")
    print(f"  manifest: {len(manifest)} entries -> {OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
