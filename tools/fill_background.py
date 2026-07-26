#!/usr/bin/env python3
"""Complete the partial background on Monster Hunter icons.

OPTIONAL — this is "style 2" (filled square card). The default pipeline keeps
icons transparent and does NOT run this script; CI omits it. Run it between
build.py and normalize.py only if you want the opaque-card look. See
tools/README.md "Background styles".

monster-hunter-DB's source icons have their background keyed to alpha 0 only
around the outer ring (a rounded/circular crop), leaving a broken-looking
frame with transparent gaps. This pass fills those outer transparent regions
with the original background color so each icon becomes a complete square card.

Background color is determined per-icon:
  - if the transparent pixels carry a non-zero RGB residue (MHFU green,
    Rise near-white, etc.), that residue IS the original bg — use it;
  - otherwise sample the nearest opaque color from the edges (MHWI gold).

Only the outer transparent region (flood-filled from the border) is filled —
interior transparency belonging to the monster (hollows, gaps between limbs)
is left alone. Runs over icons/ before normalize.py. Idempotent.
"""

from __future__ import annotations

import sys
from collections import Counter, deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"


def _sample_bg(px, w: int, h: int) -> tuple[int, int, int]:
    """Determine the background color of an icon.

    Tries, in order of preference:
      1. the most common non-zero RGB residue among transparent border pixels
         (the keyed-out bg usually leaves its color in the RGB channels);
      2. the most common opaque color on the border ring;
      3. the most common opaque color in the four corner quadrants (used when
         the whole border ring is transparent, e.g. Wilds, which otherwise
         sampled as pure black).
    """
    trans_colors: Counter = Counter()
    opaque_colors: Counter = Counter()
    ring = [0, 1, 2, w - 1, w - 2, w - 3] if w > 6 else list(range(w))
    for y in list(range(min(3, h))) + list(range(max(0, h - 3), h)):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a < 128:
                if r or g or b:
                    trans_colors[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
            else:
                opaque_colors[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
    for x in ring:
        for y in range(h):
            r, g, b, a = px[x, y]
            if a < 128:
                if r or g or b:
                    trans_colors[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
            else:
                opaque_colors[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
    if trans_colors:
        return trans_colors.most_common(1)[0][0]
    if opaque_colors:
        return opaque_colors.most_common(1)[0][0]
    # Border ring fully transparent (Wilds etc.): sample the four corner
    # quadrants, which are background but inside the transparent ring.
    corner_colors: Counter = Counter()
    cw, ch = max(1, w // 2), max(1, h // 2)
    for ry in (0, ch):
        for rx in (0, cw):
            for y in range(ry, min(ry + ch, h), 2):
                for x in range(rx, min(rx + cw, w), 2):
                    r, g, b, a = px[x, y]
                    if a > 128:
                        corner_colors[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
    if corner_colors:
        return corner_colors.most_common(1)[0][0]
    return (0, 0, 0)


def fill_background(im: Image.Image) -> tuple[Image.Image, int]:
    """Flood-fill outer transparent regions with the sampled bg color.

    Returns (image, filled_pixel_count).
    """
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    # Item-type icons are transparent-background sprites (rendered from SVG,
    # so their transparent pixels carry RGB=0, unlike monster card icons whose
    # keyed-out ring still holds the original bg color). They have no native
    # card color, so sample_bg would grab a random subject edge color. Give them
    # one uniform dark bg instead — matches a dark terminal seamlessly.
    border_transparent_rgb_nonzero = False
    for x in range(w):
        for y in (0, h - 1):
            r, g, b, a = px[x, y]
            if a < 128 and (r or g or b):
                border_transparent_rgb_nonzero = True
                break
    for y in range(h):
        for x in (0, w - 1):
            r, g, b, a = px[x, y]
            if a < 128 and (r or g or b):
                border_transparent_rgb_nonzero = True
                break
    if border_transparent_rgb_nonzero:
        bg = _sample_bg(px, w, h)  # monster card: use the keyed-out residue
    else:
        bg = (30, 30, 30)  # item sprite: uniform dark bg

    out = im.copy()
    op = out.load()
    visited = [[False] * w for _ in range(h)]
    q: deque = deque()
    # Seed from all border pixels that are transparent.
    for x in range(w):
        for y in (0, h - 1):
            if op[x, y][3] < 128 and not visited[y][x]:
                q.append((x, y))
                visited[y][x] = True
    for y in range(h):
        for x in (0, w - 1):
            if op[x, y][3] < 128 and not visited[y][x]:
                q.append((x, y))
                visited[y][x] = True
    filled = 0
    while q:
        x, y = q.popleft()
        op[x, y] = (bg[0], bg[1], bg[2], 255)
        filled += 1
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and op[nx, ny][3] < 128:
                visited[ny][nx] = True
                q.append((nx, ny))
    return out, filled


def main() -> int:
    files = sorted(ICONS.glob("*/*.png"))
    if not files:
        print("no icons in icons/ (run build.py first)")
        return 1
    total_filled = 0
    touched = 0
    for f in files:
        out, filled = fill_background(Image.open(f))
        if filled:
            out.save(f)
            touched += 1
            total_filled += filled
    print(f"filled bg on {touched}/{len(files)} icons ({total_filled} px)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
