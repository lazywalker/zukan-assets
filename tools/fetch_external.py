#!/usr/bin/env python3
"""Fetch external sources for zukan-assets.

  Reachable (live-tested):
    - mhw-db.com          (JSON API, MHW + Iceborne monsters/items)
    - wilds.mhdb.io       (JSON API, Monster Hunter Wilds monsters/items)
    - Monster Hunter Fandom wiki  (MediaWiki API, Category:Monster_Icons)

Each source is fetched independently with its own try/except so one
failure does not abort the others. Raw downloads land in gitignored
directories (see source/README.md); the cache/manifests are committed.

Usage:
    python3 tools/fetch_external.py              # fetch all reachable
    python3 tools/fetch_external.py --only api   # only the JSON APIs
    python3 tools/fetch_external.py --only fandom
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

# Browser-like identity; the Fandom API returns empty for the default
# requests User-Agent.
BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
)
HEADERS = {
    "User-Agent": (
        "zukan-assets/1.0 (https://github.com/lazywalker/zukan-assets; "
        "fan asset aggregator)"
    ),
    "Accept": "*/*",
}
BROWSER_HEADERS = {"User-Agent": BROWSER_UA, "Accept": "*/*"}

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
API_CACHE = SOURCE / "api_cache"
FANDOM_RAW = SOURCE / "fandom-raw"

TIMEOUT = 30
# Polite crawl delay for the Fandom wiki (seconds between requests).
FANDOM_DELAY = 1.0

# Map Fandom category suffix -> our short game prefix. Anything not in this
# map is kept under its raw category name (so MH3/MHP3/MHO/MHFG land in a
# fallback bucket rather than being silently mislabelled).
FANDOM_CATEGORY_TO_GAME = {
    "MHFU": "mhfu",
    "MH3U": "mh3u",
    "MH4U": "mh4u",
    "MHXX": "mhgu",  # MHXX (JP) == Generations Ultimate (West)
    "MHGen": "mhgu",
    "MHRise": "mhrise",
    "MHW": "mhw",
    "MHWI": "mhwi",
    # fallbacks — kept but lower priority
    "MH3": "mh3u",
    "MH3G": "mh3u",
    "MH4": "mh4u",
    "MHP3": "mhfu",
    "MHR": "mhrise",
}

# Top-level Fandom category whose subcategories enumerate per-game icon sets.
MONSTER_ICONS_CAT = "Category:Monster_Icons"


class FetchError(Exception):
    """Raised when a source cannot be fetched."""


def get(url: str, *, browser: bool = False, **kw) -> requests.Response:
    headers = BROWSER_HEADERS if browser else HEADERS
    kw.setdefault("timeout", TIMEOUT)
    resp = requests.get(url, headers=headers, **kw)
    return resp


def fetch_json(url: str, *, browser: bool = False) -> dict | list:
    resp = get(url, browser=browser)
    resp.raise_for_status()
    return resp.json()


# --------------------------------------------------------------------------- #
# JSON APIs (mhw-db.com + wilds.mhdb.io)
# --------------------------------------------------------------------------- #
def fetch_api_cache() -> None:
    """Fetch the two JSON APIs into source/api_cache/."""
    API_CACHE.mkdir(parents=True, exist_ok=True)
    endpoints = {
        "mhw_monsters.json": "https://mhw-db.com/monsters",
        "mhw_items.json": "https://mhw-db.com/items",
        "wilds_monsters.json": "https://wilds.mhdb.io/en/monsters",
        "wilds_items.json": "https://wilds.mhdb.io/en/items",
    }
    for fname, url in endpoints.items():
        dest = API_CACHE / fname
        try:
            data = fetch_json(url)
            dest.write_text(json.dumps(data, ensure_ascii=False, indent=2))
            n = len(data) if isinstance(data, list) else len(data.keys())
            print(f"  [api] {fname}: {n} records")
        except Exception as exc:  # noqa: BLE001
            raise FetchError(f"failed to fetch {url}: {exc}") from exc


# --------------------------------------------------------------------------- #
# Fandom wiki (MediaWiki API)
# --------------------------------------------------------------------------- #
FANDOM_API = "https://monsterhunter.fandom.com/api.php"


def _fandom_get(params: dict) -> dict:
    """One Fandom API call with browser UA and polite delay."""
    time.sleep(FANDOM_DELAY)
    params = {**params, "format": "json"}
    resp = get(FANDOM_API, browser=True, params=params)
    resp.raise_for_status()
    return resp.json()


def _cmcontinue(data: dict) -> str | None:
    """Pull the categorymembers continue token from either format.

    MediaWiki returns pagination under either the legacy `query-continue` key
    or the modern `continue` key depending on the request/version, so check
    both — missing one silently truncates large categories to 500.
    """
    cont = data.get("query-continue", {}).get("categorymembers", {})
    return cont.get("cmcontinue") or data.get("continue", {}).get("cmcontinue")


def fandom_list_subcategories(category: str) -> list[str]:
    """Return all subcategory titles under a category (paginated)."""
    titles: list[str] = []
    cmcontinue = None
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": category,
            "cmtype": "subcat",
            "cmlimit": "500",
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
        data = _fandom_get(params)
        members = data.get("query", {}).get("categorymembers", [])
        titles.extend(m["title"] for m in members)
        cmcontinue = _cmcontinue(data)
        if not cmcontinue:
            break
    return titles


def fandom_list_files(category: str) -> list[str]:
    """Return all File: titles under a category (paginated)."""
    titles: list[str] = []
    cmcontinue = None
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": category,
            "cmtype": "file",
            "cmlimit": "500",
        }
        if cmcontinue:
            params["cmcontinue"] = cmcontinue
        data = _fandom_get(params)
        members = data.get("query", {}).get("categorymembers", [])
        titles.extend(m["title"] for m in members)
        cmcontinue = _cmcontinue(data)
        if not cmcontinue:
            break
    return titles


def fandom_file_urls(file_titles: list[str]) -> dict[str, str]:
    """Resolve a batch of File: titles to their original media URLs."""
    out: dict[str, str] = {}
    # imageinfo accepts up to 50 titles per call (generator handles paging).
    for i in range(0, len(file_titles), 50):
        batch = file_titles[i : i + 50]
        params = {
            "action": "query",
            "titles": "|".join(batch),
            "prop": "imageinfo",
            "iiprop": "url|size|mime",
        }
        data = _fandom_get(params)
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            title = page.get("title", "")
            infos = page.get("imageinfo") or []
            if infos:
                out[title] = infos[0]["url"]
    return out


def fandom_category_to_game(category: str) -> str:
    """Derive a game prefix from a Fandom subcategory title.

    e.g. 'Category:MH4U Monster Icons' -> 'mh4u'. Unknown -> 'misc'.
    """
    m = re.search(r"Category:(MH[A-Z0-9]+)\b", category)
    if not m:
        return "misc"
    code = m.group(1)
    return FANDOM_CATEGORY_TO_GAME.get(code, code.lower())


def _write_fandom_manifest(manifest: list[dict]) -> None:
    (FANDOM_RAW / "_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2)
    )


def fetch_fandom() -> None:
    """Crawl the Fandom Monster_Icons category tree and download icons.

    Resumable: the manifest is rewritten after each category, and files
    already on disk are skipped. Re-running picks up where it left off.
    """
    FANDOM_RAW.mkdir(parents=True, exist_ok=True)
    manifest_path = FANDOM_RAW / "_manifest.json"
    manifest: list[dict] = []
    seen_titles: set[str] = set()
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        seen_titles = {r["wiki_title"] for r in manifest}
        print(f"  [fandom] resuming — {len(manifest)} icons already recorded")

    # Subcategories give us per-game buckets; the top category itself also
    # holds ~240 files (mostly Frontier), so we fetch both.
    cats = [MONSTER_ICONS_CAT] + fandom_list_subcategories(MONSTER_ICONS_CAT)
    print(f"  [fandom] {len(cats)} categories to crawl (incl. top-level)")

    for cat in cats:
        game = fandom_category_to_game(cat)
        try:
            files = fandom_list_files(cat)
        except Exception as exc:  # noqa: BLE001
            print(f"    ! {cat}: {exc}")
            continue
        if not files:
            continue
        # Only resolve URLs for titles we don't already have.
        new_files = [t for t in files if t not in seen_titles]
        if not new_files:
            continue
        urls = fandom_file_urls(new_files)
        added = 0
        for title, url in urls.items():
            if title in seen_titles:
                continue
            seen_titles.add(title)
            fname = title.split(":", 1)[1]  # strip "File:"
            out_dir = FANDOM_RAW / game
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / fname
            try:
                if not out_path.exists():  # skip already-downloaded on resume
                    resp = get(url, browser=True)
                    resp.raise_for_status()
                    out_path.write_bytes(resp.content)
            except Exception as exc:  # noqa: BLE001
                print(f"      ! download {title}: {exc}")
                continue
            manifest.append(
                {
                    "category": cat,
                    "game": game,
                    "wiki_title": title,
                    "source_url": url,
                    "filename": fname,
                }
            )
            added += 1
        # Persist after each category so an interruption is recoverable.
        _write_fandom_manifest(manifest)
        print(f"    {cat}: +{added} new ({len(new_files)} pending)")

    print(f"  [fandom] {len(manifest)} icons total, manifest written")


# --------------------------------------------------------------------------- #
# Dispatch
# --------------------------------------------------------------------------- #
SOURCES = {
    "api": fetch_api_cache,
    "fandom": fetch_fandom,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        choices=list(SOURCES),
        action="append",
        help="fetch only the named source(s)",
    )
    args = parser.parse_args()
    targets = args.only or list(SOURCES)

    failures: list[str] = []
    for name in targets:
        print(f"== {name} ==")
        try:
            SOURCES[name]()
        except FetchError as exc:
            print(f"  FAILED: {exc}")
            failures.append(name)
        except Exception as exc:  # noqa: BLE001
            print(f"  UNEXPECTED: {exc}")
            failures.append(name)

    print("\n== summary ==")
    for name in targets:
        status = "FAILED" if name in failures else "ok"
        print(f"  {name}: {status}")
    # Exit non-zero only if everything failed; partial success still
    # produces usable artifacts and is worth committing.
    return 0 if len(failures) < len(targets) else 1


if __name__ == "__main__":
    sys.exit(main())
