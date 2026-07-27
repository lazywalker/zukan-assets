#!/usr/bin/env python3
"""Strip the semi-transparent white halo around Monster Hunter icons.

monster-hunter-DB's Rise/Sunbreak icons ship with a feathered white edge: the
background was keyed toward alpha 0 but a band of *semi-transparent*
(0 < alpha < 255) near-white pixels remains as anti-aliasing around the
subject. clean_background.py clears the RGB residue on the fully-transparent
(alpha=0) pixels, but not this halo, so after normalize.py it shows up as a
visible white ring, especially on Rise/Sunbreak, whose art style produces a
wide feathered edge.

This pass removes that halo by flood-filling from the image border through the
set of "near-white semi-transparent" pixels and clearing them to fully
transparent (alpha=0, RGB=0). Only halo pixels *connected to the border* are
touched, so white highlights inside the subject (eyes, scales) survive: the
halo is a connected outer ring, interior whites are isolated.

Runs over icons/ after build.py, before normalize.py. Idempotent: a second
run finds no halo to clear.
"""

from __future__ import annotations

import sys
from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"

# A pixel is "halo" if it's semi-transparent (0 < a < HIGH) AND near-white.
# Semi-transparent (not fully opaque) is what distinguishes the feathered edge
# from the subject's solid white areas; near-white (RGB all > WHITE) matches
# the keyed-out bg's residue color.
ALPHA_HIGH = 200      # opaque pixels (a >= this) always keep: subject interior
WHITE = 225           # min of R,G,B above which counts as near-white


def _halo_mask(px, w: int, h: int) -> list[list[bool]]:
    """Boolean grid of near-white semi-transparent pixels."""
    mask = [[False] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if 0 < a < ALPHA_HIGH and min(r, g, b) > WHITE:
                mask[y][x] = True
    return mask


def clean_halo(im: Image.Image) -> tuple[Image.Image, int]:
    """Flood-fill from the border through near-white semi-transparent pixels,
    clearing them to alpha=0. Returns (modified_image, pixels_cleared).

    Returns a new image (convert may copy); callers must use the return value,
    not the passed-in image.
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    mask = _halo_mask(px, w, h)

    visited = [[False] * w for _ in range(h)]
    q: deque = deque()
    # Seed from all border pixels that are halo.
    for x in range(w):
        for y in (0, h - 1):
            if mask[y][x] and not visited[y][x]:
                visited[y][x] = True
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if mask[y][x] and not visited[y][x]:
                visited[y][x] = True
                q.append((x, y))
    while q:
        x, y = q.popleft()
        px[x, y] = (0, 0, 0, 0)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and mask[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))
    return im, sum(sum(row) for row in visited)


def main() -> int:
    files = sorted(ICONS.glob("*/*.png"))
    if not files:
        print("no icons in icons/ (run build.py first)")
        return 1
    total_cleared = 0
    touched = 0
    for f in files:
        out, cleared = clean_halo(Image.open(f))
        if cleared:
            out.save(f)
            touched += 1
            total_cleared += cleared
    print(f"cleared halo on {touched}/{len(files)} icons ({total_cleared} px)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
