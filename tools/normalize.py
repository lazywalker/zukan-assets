#!/usr/bin/env python3
"""Normalize all icons to a uniform terminal-friendly spec.

zukan's icons were wildly inconsistent: 54px–512px across games, ~25MB for
731 icons, with rendered games (Wilds 512px/2400 colors) bloating the bundle
and rendering as a muddy blur.

This pass brings every icon to one spec:
  - resize to a fixed TARGET_W × TARGET_W square;
  - quantize to a small palette (PALETTE_COLORS) for flat pixel-art regions.

Monster Hunter icons are card-style illustrations with their own backgrounds
(e.g. the in-game hunter's notebook tiles), not isolated sprites, so the full
square frame is kept — no transparent-margin trimming. This preserves the
source art's composition. Runs over icons/ after build.py. Idempotent.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"

# Fixed square output size (terminal columns = rows before half-block).
# 48px is the stored size — detailed enough to read clearly. zukan shrinks
# it at runtime (NEAREST) to 32 for viewing or 24 for bash startup art, with
# negligible loss (a single downscale from 48 is visually clean). Keeping one
# stored size halves maintenance vs maintaining 32+24 sets.
TARGET_W = 48
PALETTE_COLORS = 32


def quantize_rgba(im: Image.Image, colors: int) -> Image.Image:
    """Reduce to `colors` without touching alpha."""
    r, g, b, a = im.split()
    rgb = Image.merge("RGB", (r, g, b))
    q = rgb.quantize(colors=colors, method=Image.MEDIANCUT, dither=Image.NONE)
    qr, qg, qb = q.convert("RGB").split()
    out = Image.merge("RGBA", (qr, qg, qb, a))
    # Re-zero RGB on fully-transparent pixels (quantize may have recolored them).
    data = bytearray(out.tobytes())
    for i in range(0, len(data), 4):
        if data[i + 3] == 0:
            data[i] = data[i + 1] = data[i + 2] = 0
    return Image.frombytes("RGBA", im.size, bytes(data))


def normalize(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    # Resize to a fixed square. Monster Hunter icons are card-style
    # illustrations with their own backgrounds, not isolated sprites, so we
    # keep the full square frame (no trim) — matching the source art. Item
    # icons are flood-filled to a card by fill_background.py first, so they go
    # through the same path.
    im = im.resize((TARGET_W, TARGET_W), Image.LANCZOS)
    # Enhance contrast before quantizing: downscaling averages colors and
    # muddies the monster-vs-background separation, so sharpen edges, stretch
    # contrast, and boost saturation to recover readable separation.
    rgb = im.convert("RGB")
    rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=2))
    rgb = ImageEnhance.Contrast(rgb).enhance(1.3)
    rgb = ImageEnhance.Color(rgb).enhance(1.4)
    r, g, b = rgb.split()
    im = Image.merge("RGBA", (r, g, b, im.split()[3]))
    im = quantize_rgba(im, PALETTE_COLORS)
    return im


def main() -> int:
    files = sorted(ICONS.glob("*/*.png"))
    if not files:
        print("no icons in icons/ (run build.py first)")
        return 1
    processed = 0
    for f in files:
        normalize(Image.open(f)).save(f)
        processed += 1
    print(f"normalized {processed} icons -> {TARGET_W}px wide, {PALETTE_COLORS} colors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
