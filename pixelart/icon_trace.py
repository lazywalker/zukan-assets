#!/usr/bin/env python3
"""Trace an icon into a draft sprite config (big-block icon redrawing).

Downsamples the icon to the sprite canvas, maps every cell to the nearest
color of the identity palette and writes the result as a sprites/ config
through the same source_text formatter the editor save path uses. The
stroke ring stays on the house K (24, 20, 22).

Tracing only works on natively flat icons (MHO / MHST2 / MHWilds render
style, guide L25). A painterly mhgu/mh4u square traced this way turns
into abstract color noise: redraw those by hand instead. The draft is a
starting point either way; expect a hand cleanup pass for stray quantizer
buckets and the identity details (guide L26).

Usage:
    python3 icon_trace.py <slug> <icon.png> [--colors N] [--speckle N]
        [--block N] [--seed ch=R,G,B]...

The identity palette is auto-sampled from the icon's most common block
colors (the background bucket is dropped). --seed pins one color to a
palette char so small high-contrast regions (eyes, tusks) survive the
mapping; repeat the flag per seed. Char K is reserved for the ring.
"""

import argparse
import importlib
import sys
from pathlib import Path

from PIL import Image

import build_sprites
import spritekit as sk
from decompile import fills_from_view, source_text, spans_from_mask

HERE = Path(__file__).resolve().parent
SPRITES = HERE / "sprites"
HOUSE_K = (24, 20, 22, 255)
POOL = "BCDEFGHOPQRY"                  # seed chars, luminance order; K reserved
GAMES = ("mho", "mhst2", "mhst", "mhwilds", "mhrise", "mhw", "mhwi",
         "mh4u", "mh3u", "mhfu", "mhgu")


def find_icon(slug):
    for g in GAMES:
        for name in (slug, slug.replace("_", "-"), slug.replace("-", "_")):
            p = HERE.parent / "icons" / g / f"{name}.png"
            if p.exists():
                return str(p)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("icon")
    ap.add_argument("--colors", type=int, default=6)
    ap.add_argument("--speckle", type=int, default=6)
    ap.add_argument("--block", type=int, default=1,
                    help="pixelate to (w/block, h/block) first")
    ap.add_argument("--seed", action="append", default=[],
                    metavar="ch=R,G,B", help="pin an identity color")
    args = ap.parse_args()

    stem = args.slug.replace("-", "_")
    sys.path.insert(0, str(SPRITES))
    for m in list(sys.modules):
        if m == stem: del sys.modules[m]
    old = importlib.import_module(stem).CONFIG
    doc = sys.modules[stem].__doc__ or ""
    W, H = old["size"]

    im = Image.open(args.icon).convert("RGBA")
    im = im.crop(im.getbbox())
    bg = im.getpixel((0, 0))[:3]
    bw, bh = max(1, W // args.block), max(1, H // args.block)
    small = im.resize((bw, bh), Image.BOX)
    rgb, alpha = small.convert("RGB").load(), small.split()[3].load()

    seeds = []
    for s in args.seed:
        ch, rgbtext = s.split("=")
        seeds.append((ch, tuple(int(v) for v in rgbtext.split(","))))

    quant = small.convert("RGB").quantize(colors=args.colors + 1,
                                          method=Image.MEDIANCUT).convert("RGB")
    qpx = quant.load()
    from collections import Counter
    buckets = Counter(qpx[x, y] for y in range(bh) for x in range(bw))
    for rgbv, _ in buckets.most_common():
        if len(seeds) >= args.colors:
            break
        if sum(abs(a - b) for a, b in zip(rgbv, bg)) < 90:
            continue
        if any(sum(abs(a - b) for a, b in zip(rgbv, srgb)) < 90
               for _, srgb in seeds):
            continue
        ch = next(c for c in POOL if c not in [x[0] for x in seeds])
        seeds.append((ch, rgbv))
    seeds.sort(key=lambda s: 0.3 * s[1][0] + 0.6 * s[1][1] + 0.1 * s[1][2])

    def nearest(rgbv):
        return min(seeds, key=lambda s: sum(abs(a - b) for a, b in
                                            zip(rgbv, s[1])))[0]

    grid = [[None] * W for _ in range(H)]
    for by in range(bh):
        for bx in range(bw):
            if alpha[bx, by] < 70:
                continue
            ch = nearest(rgb[bx, by])
            for y in range(by * (H // bh), min(H, (by + 1) * (H // bh))):
                for x in range(bx * (W // bw), min(W, (bx + 1) * (W // bw))):
                    grid[y][x] = ch

    def blobs(g):
        seen, out = set(), []
        for y in range(H):
            for x in range(W):
                if g[y][x] is None or (y, x) in seen:
                    continue
                stack, comp, col = [(y, x)], [], g[y][x]
                while stack:
                    cy, cx = stack.pop()
                    if (cy, cx) in seen or g[cy][cx] != col:
                        continue
                    seen.add((cy, cx)); comp.append((cy, cx))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            stack.append((ny, nx))
                out.append((col, comp))
        return out

    for col, comp in blobs(grid):
        if len(comp) < args.speckle:
            neigh = {}
            for y, x in comp:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] not in (None, col):
                        c = grid[ny][nx]
                        neigh[c] = neigh.get(c, 0) + 1
            if neigh:
                best = max(neigh, key=neigh.get)
                for y, x in comp:
                    grid[y][x] = best

    palette = {".": (0, 0, 0, 0), "K": HOUSE_K}
    for ch, rgbv in seeds:
        palette[ch] = (rgbv[0], rgbv[1], rgbv[2], 255)
    counts = {ch: 0 for ch, _ in seeds}
    for row in grid:
        for c in row:
            if c is not None:
                counts[c] += 1
    base = max(counts, key=counts.get)

    view, mask = [], []
    for y in range(H):
        vr, mr = "", []
        for x in range(W):
            c = grid[y][x]
            if c is None:
                vr += "."; mr.append(False)
            else:
                vr += c; mr.append(True)
        view.append(vr); mask.append(mr)

    cfg = {"name": old["name"], "size": (W, H),
           "compare_to": old.get("compare_to", ""),
           "palette": palette, "base": base,
           "spans": spans_from_mask(mask)}
    fills = fills_from_view(view, mask, base)
    if fills:
        cfg["fills"] = fills

    build_sprites.validate_slugs([cfg])
    build_sprites.validate_dimensions([cfg])
    sk.build_grid(cfg)
    open(SPRITES / f"{stem}.py", "w").write(source_text(cfg, doc))
    print(f"traced {cfg['name']}: {len(seeds)} colors, base={base}, "
          f"{len(cfg.get('fills', []))} fill ops -> sprites/{stem}.py")
    print("next: hand clean (guide L26), then python3 build_sprites.py", cfg["name"])


if __name__ == "__main__":
    main()
