#!/usr/bin/env python3
"""Zero out RGB on fully-transparent pixels across all output icons.

monster-hunter-DB's source icons for several games carry leftover background
color in the RGB channels of alpha=0 pixels (MHFU green, MHGU blue, MH4U gold,
Rise/Sunbreak near-white): the background was keyed to alpha 0 but its color
was never cleared. In straight-alpha compositing this is invisible, but it
leaks as a faint halo under premultiplied compositing and is a latent
correctness defect flagged by tools/audit.py.

This pass makes every icon strictly clean: alpha=0 ⟹ RGB=(0,0,0). It runs
after build.py over icons/ and is idempotent.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"


def clean_transparent_rgb(path: Path) -> bool:
    """Clear RGB on alpha=0 pixels. Returns True if any pixel changed."""
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    data = bytearray(im.tobytes())  # RGBA, row-major
    changed = False
    for i in range(0, len(data), 4):
        if data[i + 3] == 0:  # alpha
            if data[i] or data[i + 1] or data[i + 2]:
                data[i] = data[i + 1] = data[i + 2] = 0
                changed = True
    if changed:
        Image.frombytes("RGBA", (w, h), bytes(data)).save(path)
    return changed


def main() -> int:
    files = sorted(ICONS.glob("*/*.png"))
    if not files:
        print("no icons in icons/ (run build.py first)")
        return 1
    cleaned = 0
    for f in files:
        if clean_transparent_rgb(f):
            cleaned += 1
    print(f"cleared RGB residue on {cleaned}/{len(files)} icons")
    return 0


if __name__ == "__main__":
    sys.exit(main())
