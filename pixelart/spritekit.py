#!/usr/bin/env python3
"""Pixel-sprite engine for the pixelart sprite sets (monsters + endemic life).

A sprite is defined by a config dict (see sprites/*.py):

    name        output stem; files are <name>_sprite.png and
                <name>_sprite_preview.png next to the driver
    size        (width, height)
    palette     char -> (r, g, b, a)
    base        char every silhouette pixel starts as
    spans       row -> [(col_start, col_end), ...] silhouette runs, '#'
    fills       ordered op list, executed after the stroke pass:
                    ("runs", cells, ch[, frm])  recolor (row, c0, c1) runs,
                                                frm defaults to base
                    ("put", row, col, chars)    repaint a char run in place
    compare_to  optional source-icon path (relative to the driver dir)
                rendered next to the sprite

Build is deterministic: the same config encodes to identical PNG bytes,
which is what build_sprites.py --check asserts against the files on disk.
"""
import io

from PIL import Image, ImageDraw


def _mask(cfg):
    w, h = cfg["size"]
    rows = [["."] * w for _ in range(h)]
    for r, runs in cfg["spans"].items():
        for a, b in runs:
            for c in range(a, b + 1):
                rows[r][c] = "#"
    return rows


def _stroke(mask):
    """Outline pass: transparent cells touching the mask become 'K'.

    Parts authored 1px apart share the filled-in channel, which is what
    draws the black separation line between wing, body and tail.
    """
    h = len(mask)
    w = len(mask[0])
    g = [[c if c == "#" else "." for c in row] for row in mask]

    def filled(x, y):
        return 0 <= x < w and 0 <= y < h and g[y][x] == "#"

    for y in range(h):
        for x in range(w):
            if g[y][x] == "." and any(
                filled(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
            ):
                g[y][x] = "K"
    return g


def build_grid(cfg):
    g = _stroke(_mask(cfg))
    base = cfg["base"]
    h, w = len(g), len(g[0])
    for y in range(h):
        for x in range(w):
            if g[y][x] == "#":
                g[y][x] = base

    name = cfg["name"]
    for op in cfg.get("fills", []):
        kind = op[0]
        if kind == "runs":
            cells, ch = op[1], op[2]
            frm = op[3] if len(op) > 3 else base
            for r, a, b in cells:
                for c in range(a, b + 1):
                    if g[r][c] == frm:
                        g[r][c] = ch
        elif kind == "put":
            r, c0, chars = op[1], op[2], op[3]
            for i, ch in enumerate(chars):
                if g[r][c0 + i] == ".":
                    raise SystemExit(f"{name}: put on transparent cell r{r} c{c0 + i}")
                g[r][c0 + i] = ch
        else:
            raise SystemExit(f"{name}: unknown fill op {kind!r}")
    return g


def to_image(cfg, grid, scale=1, bg=None):
    w, h = cfg["size"]
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    pal = cfg["palette"]
    for y in range(h):
        for x in range(w):
            im.putpixel((x, y), pal[grid[y][x]])
    if scale > 1:
        big = im.resize((w * scale, h * scale), Image.NEAREST)
        if bg:
            canvas = Image.new("RGBA", big.size, bg)
            canvas.paste(big, (0, 0), big)
            return canvas
        return big
    return im


def png_bytes(cfg, scale=1, bg=None):
    buf = io.BytesIO()
    to_image(cfg, build_grid(cfg), scale=scale, bg=bg).save(buf, format="PNG")
    return buf.getvalue()


def render_comparison(cfg, out_path, root, scale=12, bg=(24, 26, 30, 255)):
    """Sprite next to its source icon, both snapped to the sprite's height."""
    import os

    orig = Image.open(os.path.join(root, cfg["compare_to"])).convert("RGBA")
    tile_h = cfg["size"][1] * scale
    ow = round(orig.width * tile_h / orig.height)
    orig_big = orig.resize((ow, tile_h), Image.NEAREST)
    sprite_big = to_image(cfg, build_grid(cfg), scale=scale)
    pad = 24
    canvas = Image.new("RGBA", (ow + sprite_big.width + pad * 3, tile_h + pad * 2), bg)
    canvas.paste(orig_big, (pad, pad), orig_big)
    canvas.paste(sprite_big, (ow + pad * 2, pad), sprite_big)
    canvas.save(out_path)


def contact_sheet(cfgs, out_path, scale=8, bg=(24, 26, 30, 255)):
    """Every sprite on one board at review size, named, for eyeball passes."""
    pad, label_h = 20, 18
    tiles = []
    for cfg in cfgs:
        im = to_image(cfg, build_grid(cfg), scale=scale)
        tiles.append((cfg["name"], im))
    width = sum(im.width for _, im in tiles) + pad * (len(tiles) + 1)
    height = max(im.height for _, im in tiles) + pad * 2 + label_h
    canvas = Image.new("RGBA", (width, height), bg)
    draw = ImageDraw.Draw(canvas)
    x = pad
    for name, im in tiles:
        canvas.paste(im, (x, pad), im)
        draw.text((x + 2, pad + im.height + 2), name, fill=(165, 170, 180, 255))
        x += im.width + pad
    canvas.save(out_path)
