#!/usr/bin/env python3
"""Process raw Fandom wiki downloads into slug-named committed outputs.

Reorganizes source/fandom-raw/<game>/<wiki-filename>.png (the original wiki
filenames, with game prefixes and "Icon" tokens) into clean
source/fandom-processed/<game>/<slug>.png that build.py can match.

Idempotent: re-running overwrites cleanly.

The raw downloads are gitignored (Fandom prohibits redistribution); only the
slug-renamed copies are committed.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
FANDOM_RAW = SOURCE / "fandom-raw"
FANDOM_OUT = SOURCE / "fandom-processed"
sys.path.insert(0, str(ROOT / "tools"))
from common import slugify  # noqa: E402


def process_fandom() -> None:
    manifest_path = FANDOM_RAW / "_manifest.json"
    if not manifest_path.exists():
        print("  [fandom] no manifest (raw not fetched); skipping")
        return
    FANDOM_OUT.mkdir(parents=True, exist_ok=True)
    for f in FANDOM_OUT.glob("**/*.png"):
        f.unlink()
    for f in FANDOM_OUT.glob("**/*.svg"):
        f.unlink()

    manifest = json.loads(manifest_path.read_text())
    out_records: list[dict] = []
    for entry in manifest:
        game = entry["game"]
        fname = entry["filename"]
        src = FANDOM_RAW / game / fname
        if not src.exists():
            continue
        # Slug from the wiki filename: drop game prefix and 'Icon' token,
        # keep extension. e.g. 'Rathalos MH4-Icon.png' -> 'rathalos.png'
        stem = src.stem
        if "-" in stem:
            _, rest = stem.split("-", 1)
        else:
            rest = stem
        rest = rest.replace("Icon", "").strip()
        slug = slugify(rest)
        ext = src.suffix.lower()
        game_dir = FANDOM_OUT / game
        game_dir.mkdir(parents=True, exist_ok=True)
        dest = game_dir / f"{slug}{ext}"
        i = 1
        while dest.exists():
            dest = game_dir / f"{slug}-{i}{ext}"
            i += 1
        shutil.copy2(src, dest)
        out_records.append(
            {
                "game": game,
                "slug": slug,
                "filename": str(dest.relative_to(FANDOM_OUT)),
                "source": entry["source_url"],
                "wiki_title": entry["wiki_title"],
            }
        )

    (FANDOM_OUT / "_manifest.json").write_text(
        json.dumps(out_records, ensure_ascii=False, indent=2)
    )
    print(f"  [fandom] {len(out_records)} icons processed -> {FANDOM_OUT.name}/")


def main() -> int:
    process_fandom()
    return 0


if __name__ == "__main__":
    sys.exit(main())
