#!/usr/bin/env python3
"""Remove the dark frame from monster-hunter-DB MHST2 icons.

The monster-hunter-DB MHST2 icons are clean pixel sprites, but they sit on a
near-black frame (RGB ~21,15,5, alpha ~1) rather than true transparency —
unlike every other MHDB game, which is already transparent. This script
removes that frame by a darkness threshold (the frame is the only near-black
region; monster parts are rarely pure black), feathering the transition zone
for smooth edges, then trims to the monster bbox.

Reads from source/monster-hunter-DB/icons/MHST2-*_Icon.png and writes cleaned
sprites to source/mhst2-cleaned/<slug>.png.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
MHDB_ICONS = SOURCE / "monster-hunter-DB" / "icons"
OUT = SOURCE / "mhst2-cleaned"
sys.path.insert(0, str(ROOT / "tools"))
from common import icon_ref_to_monster_slug  # noqa: E402

# Frame is RGB ~21,15,5. Below DARK_FRAME the pixel is frame; above DARK_CLEAR
# it is fully monster. The band between is feathered for anti-aliasing.
DARK_FRAME = 60
DARK_CLEAR = 100


def clean_frame(icon: Image.Image) -> Image.Image:
    """Remove the dark frame: alpha scaled by brightness in the transition zone."""
    icon = icon.convert("RGBA")
    w, h = icon.size
    px = icon.load()
    out = icon.copy()
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            brightness = max(r, g, b)
            if brightness < DARK_FRAME:
                # Frame: fully transparent. Clear RGB too so no residual color
                # leaks at the transparent edge (keeps premultiplied-clean).
                op[x, y] = (0, 0, 0, 0)
            elif brightness < DARK_CLEAR:
                # Feather: ramp alpha across the anti-aliased frame edge,
                # fading RGB toward black so the dark frame color tapers off.
                t = (brightness - DARK_FRAME) / (DARK_CLEAR - DARK_FRAME)
                op[x, y] = (int(r * t), int(g * t), int(b * t), int(a * t))
            # else: keep opaque monster pixel as-is.
    return out


def main() -> int:
    files = sorted(MHDB_ICONS.glob("MHST2-*_Icon.png"))
    if not files:
        print("no MHST2 icons found in monster-hunter-DB")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.glob("*.png"):
        f.unlink()

    out_records = []
    for f in files:
        cleaned = clean_frame(Image.open(f))
        bbox = cleaned.split()[3].getbbox()
        if bbox:
            cleaned = cleaned.crop(bbox)
        slug = icon_ref_to_monster_slug(f.name)
        dest = OUT / f"{slug}.png"
        cleaned.save(dest)
        out_records.append({"slug": slug, "filename": dest.name, "source": f.name})

    (OUT / "_manifest.json").write_text(
        json.dumps(out_records, ensure_ascii=False, indent=2)
    )
    print(f"cleaned {len(out_records)} MHST2 icons -> {OUT.name}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
