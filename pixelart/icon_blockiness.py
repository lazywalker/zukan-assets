#!/usr/bin/env python3
"""Rank sprite icons by big-block traceability.

Downsamples every compare_to icon to its sprite canvas, quantizes to six
colors and measures the mean connected same-color blob (share of cells)
plus the boundary ratio. Natively flat icons (MHO / MHST2 / MHWilds
renders) score high and are the candidates for icon_trace.py; painterly
squares score low and need a hand redraw (guide L25). Reference line:
abiorugu's icon scores ~0.016. "?" placeholder icons score high but are
unusable, so eyeball the top list before queueing.

Usage:
    python3 icon_blockiness.py [slug ...]      # default: every sprite
"""

import importlib
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SPRITES = HERE / "sprites"


def score(path, w, h):
    im = Image.open(path).convert("RGBA")
    im = im.crop(im.getbbox())
    if im.width < 2 or im.height < 2:
        return None
    small = im.resize((w, h), Image.BOX)
    q = small.convert("RGB").quantize(colors=6, method=Image.MEDIANCUT).convert("RGB")
    alpha = small.split()[3]
    w2, h2 = small.size
    apx, rgb, qpx = alpha.load(), small.convert("RGB").load(), q.load()
    cells = [(y, x) for y in range(h2) for x in range(w2) if apx[x, y] >= 60]
    n = len(cells)
    if n < 8:
        return None
    boundary = 0
    for y, x in cells:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w2 and 0 <= ny < h2 and apx[nx, ny] >= 60 \
               and qpx[nx, ny] != qpx[x, y]:
                boundary += 1
                break
    seen, blobs = set(), []
    for cell in cells:
        if cell in seen:
            continue
        stack, size, col = [cell], 0, qpx[cell[1], cell[0]]
        while stack:
            y, x = stack.pop()
            if (y, x) in seen:
                continue
            seen.add((y, x))
            if qpx[x, y] != col:
                continue
            size += 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w2 and 0 <= ny < h2 and (ny, nx) not in seen \
                   and apx[nx, ny] >= 60 and qpx[nx, ny] == col:
                    stack.append((ny, nx))
        blobs.append(size)
    return sum(blobs) / len(blobs) / n, boundary / n


def icon_path(cfg):
    ct = cfg.get("compare_to")
    if ct:
        return ct
    slug = cfg["name"]
    for g in ("mho", "mhst2", "mhst", "mhwilds", "mhrise", "mhw", "mhwi",
              "mh4u", "mh3u", "mhfu", "mhgu"):
        for name in (slug, slug.replace("-", "_"), slug.replace("_", "-")):
            p = HERE.parent / "icons" / g / f"{name}.png"
            if p.exists():
                return str(p)
    return None


def main():
    sys.path.insert(0, str(SPRITES))
    slugs = sys.argv[1:]
    rows = []
    import glob
    for f in sorted(glob.glob(str(SPRITES / "*.py"))):
        stem = f.split("/")[-1][:-3]
        if stem.startswith("_"):
            continue
        if slugs and stem.replace("_", "-") not in slugs \
           and stem not in slugs:
            continue
        for m in list(sys.modules):
            if m == stem: del sys.modules[m]
        cfg = importlib.import_module(stem).CONFIG
        p = icon_path(cfg)
        if not p:
            continue
        r = score(p, *cfg["size"])
        if r:
            rows.append((r[0], r[1], stem, cfg["size"]))
    rows.sort(reverse=True)
    print(f"{len(rows)} icons scored (mean blob share; abiorugu ref ~0.016)")
    for i, (mb, bd, stem, size) in enumerate(rows):
        print(f"{i+1:3}. blob={mb:.3f} boundary={bd:.2f}  {stem:28} "
              f"{size[0]}x{size[1]}")


if __name__ == "__main__":
    main()
