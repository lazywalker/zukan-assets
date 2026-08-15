#!/usr/bin/env python3
"""Build the pixelart sprite sets from sprites/*.py (monsters) and
endemic/*.py (endemic life, --endemic) configs.

Usage:
    python3 build_sprites.py                     # dev: previews + contact sheet
    python3 build_sprites.py rathalos            # dev: one sprite
    python3 build_sprites.py --out DIR           # release: native-size slug PNGs
    python3 build_sprites.py --check DIR         # verify DIR PNGs are current

Set spec: height <= 24, width unlimited. --out emits each sprite at its
native size (no padding, no scaling). Every sprite name must be a known
slug in the matching data JSON (monsters.json, or endemic_life.json with
--endemic; one record per game dedupes to one sprite per slug). --check
byte-compares DIR against a fresh build so committed PNGs can never drift
from the configs; pixelart-check CI asserts this.
"""
import argparse
import importlib
import json
import sys
from pathlib import Path

import spritekit as sk

HERE = Path(__file__).resolve().parent
SPRITES = HERE / "sprites"
ENDEMIC_SPRITES = HERE / "endemic"
MONSTERS_JSON = HERE.parent / "data" / "monsters.json"
ENDEMIC_JSON = HERE.parent / "data" / "endemic_life.json"


def load_configs(only=None, endemic=False):
    # variants do `from rathalos import CONFIG`, so the sprites dir must
    # be importable as flat modules
    sprites = ENDEMIC_SPRITES if endemic else SPRITES
    sys.path.insert(0, str(sprites))
    mods = {}
    for p in sorted(sprites.glob("*.py")):
        if p.stem.startswith("_"):
            continue
        mod = importlib.import_module(p.stem)
        mods[p.stem] = mod
    if only:
        # accept either the module stem or the sprite name
        by_name = {mod.CONFIG["name"]: mod for mod in mods.values()}
        mods = {stem: mod for stem, mod in mods.items()
                if stem in only or mod.CONFIG["name"] in only}
    return [mod.CONFIG for mod in mods.values()]


def validate_dimensions(cfgs):
    """Set spec: height never exceeds 24; width is unlimited."""
    too_tall = [f"{c['name']} ({c['size'][1]}px)"
                for c in cfgs if c["size"][1] > 24]
    if too_tall:
        sys.exit(f"sprites taller than 24px: {', '.join(too_tall)}")


def known_slugs(endemic=False):
    src = ENDEMIC_JSON if endemic else MONSTERS_JSON
    if not src.exists():
        sys.exit(f"sprite data not found: {src}")
    return {m["slug"] for m in json.loads(src.read_text())}


def validate_slugs(cfgs, endemic=False):
    slugs = known_slugs(endemic)
    unknown = [c["name"] for c in cfgs if c["name"] not in slugs]
    if unknown:
        sys.exit(f"sprite names not in data/monsters.json: {', '.join(unknown)}")


def build_dev(cfg, endemic=False):
    name = cfg["name"]
    prefix = "endemic-" if endemic else ""
    (HERE / f"{prefix}{name}_sprite.png").write_bytes(sk.png_bytes(cfg))
    sk.to_image(cfg, sk.build_grid(cfg), scale=12, bg=(24, 26, 30, 255)).save(
        HERE / f"{prefix}{name}_sprite_preview.png"
    )
    if cfg.get("compare_to"):
        sk.render_comparison(cfg, HERE / f"{prefix}{name}_sprite_vs_original.png",
                             HERE)
    print(f"{name}: built ({cfg['size'][0]}x{cfg['size'][1]})")


def emit_release(cfg, out_dir):
    png = out_dir / f"{cfg['name']}.png"
    png.write_bytes(sk.png_bytes(cfg))
    print(f"{cfg['name']}: {png} ({cfg['size'][0]}x{cfg['size'][1]})")


def check_release(cfg, out_dir):
    png = out_dir / f"{cfg['name']}.png"
    if not png.exists():
        print(f"{cfg['name']}: MISSING in {out_dir}")
        return False
    ok = png.read_bytes() == sk.png_bytes(cfg)
    print(f"{cfg['name']}: {'OK' if ok else 'DRIFT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*", help="sprite name(s) or module stem(s)")
    ap.add_argument("--endemic", action="store_true",
                    help="build the endemic-life set from endemic/ configs "
                         "(slugs validated against data/endemic_life.json)")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--out", metavar="DIR",
                      help="emit native-size release PNGs into DIR")
    mode.add_argument("--check", metavar="DIR",
                      help="verify DIR PNGs match the configs byte for byte")
    args = ap.parse_args()

    only = args.names or None
    cfgs = load_configs(only, endemic=args.endemic)
    if not cfgs:
        sys.exit(f"no sprite configs match: {only}")
    cfgs = dedupe_names(cfgs)
    validate_slugs(cfgs, endemic=args.endemic)
    validate_dimensions(cfgs)

    if args.out or args.check:
        out_dir = Path(args.out or args.check)
        if args.check:
            ok = all(check_release(c, out_dir) for c in cfgs)
            sys.exit(0 if ok else 1)
        out_dir.mkdir(parents=True, exist_ok=True)
        for cfg in cfgs:
            emit_release(cfg, out_dir)
        return

    for cfg in cfgs:
        build_dev(cfg, endemic=args.endemic)
    # the review boards always show the whole set, even on a single build
    cfgs_all = dedupe_names(load_configs(endemic=args.endemic))
    suffix = "_endemic" if args.endemic else ""
    sk.contact_sheet(cfgs_all, HERE / f"contact_sheet{suffix}.png")
    roster_preview(cfgs_all, HERE / f"roster_preview{suffix}.png")
    print(f"contact sheet: {HERE / f'contact_sheet{suffix}.png'}")


def dedupe_names(cfgs):
    """endemic_life.json carries one record per game; one sprite per slug."""
    seen = set()
    out = []
    for cfg in cfgs:
        if cfg["name"] not in seen:
            seen.add(cfg["name"])
            out.append(cfg)
    return out


def roster_preview(cfgs, out_path, scale=7, pad=16, lab=30, cols=5):
    """Numbered 5-per-row review board (the one used for roster reviews)."""
    from PIL import Image, ImageDraw

    tiles = []
    for cfg in cfgs:
        im = sk.to_image(cfg, sk.build_grid(cfg), scale=scale)
        tiles.append((cfg["name"], im))
    cw = max(t.width for _, t in tiles) + pad*2
    ch = max(t.height for _, t in tiles) + pad*2 + lab
    rows = (len(tiles) + cols - 1) // cols
    canvas = Image.new("RGBA", (cw*cols, ch*rows), (24, 26, 30, 255))
    draw = ImageDraw.Draw(canvas)
    for i, (name, t) in enumerate(tiles):
        x0 = (i % cols) * cw + pad
        y0 = (i // cols) * ch + pad
        canvas.paste(t, (x0, y0), t)
        color = (255, 200, 90, 255) if i % 2 else (150, 200, 255, 255)
        draw.text((x0 + 4, y0 + t.height + 2), f"#{i+1:02d} {name}", fill=color)
    canvas.save(out_path)


if __name__ == "__main__":
    main()
