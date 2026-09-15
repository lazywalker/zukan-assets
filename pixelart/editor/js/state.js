// Editor state: mask (the authored silhouette) + explicit (sparse cell ->
// palette char overrides). The view is always synthesized from these two
// with the same three rules as pixelart/decompile.py synthesize(); keep
// the two implementations in sync or saves will be refused as view drift.

export const CHAR_POOL =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

export function nextFreeChar(palette) {
  for (const ch of CHAR_POOL) {
    if (!(ch in palette) && ch !== "K" && ch !== ".") return ch;
  }
  return null;
}

// nibble-at-a-time: JS bitwise ops are 32-bit, and sprites run 36 wide.
// Column c is bit (w-1-c) of the row integer, matching decompile.py
// pack_row/unpack_rows. When w is not a multiple of 4 the top hex digit
// is partially used; getting this wrong shifts every mask column by
// (4*ceil(w/4) - w) on both load and save.
export function packRow(bits, w) {
  const D = Math.ceil(w / 4);
  const nib = new Uint8Array(D);
  for (let c = 0; c < w; c++) {
    if (!bits[c]) continue;
    const p = w - 1 - c;
    nib[D - 1 - (p >> 2)] |= 1 << (p & 3);
  }
  let out = "";
  for (let i = 0; i < D; i++) out += nib[i].toString(16);
  return out;
}

export function unpackRow(hex, w) {
  const bits = new Uint8Array(w);
  const D = hex.length;
  for (let i = 0; i < D; i++) {
    const n = parseInt(hex[i], 16);
    const base = (D - 1 - i) * 4;
    for (let b = 0; b < 4; b++) {
      const c = w - 1 - (base + b);
      if (c >= 0 && c < w && (n >> b) & 1) bits[c] = 1;
    }
  }
  return bits;
}

export function nearestChar(palette, r, g, b) {
  let best = null;
  let bestD = Infinity;
  for (const ch in palette) {
    if (ch === ".") continue;
    const [pr, pg, pb] = palette[ch];
    const d = (pr - r) ** 2 + (pg - g) ** 2 + (pb - b) ** 2;
    if (d < bestD) {
      bestD = d;
      best = ch;
    }
  }
  return { ch: best, dist: Math.sqrt(bestD) };
}

export class SpriteState {
  constructor({ w, h, base, palette, mask, explicit }) {
    this.w = w;
    this.h = h;
    this.base = base;
    this.palette = palette; // ordered object: char -> [r,g,b,a]
    this.mask = mask;       // Uint8Array w*h
    this.explicit = explicit; // Map "r,c" -> char
  }

  static blank(w, h, palette, base) {
    return new SpriteState({
      w, h, base, palette,
      mask: new Uint8Array(w * h),
      explicit: new Map(),
    });
  }

  static fromBundle(b) {
    const [w, h] = b.size;
    const mask = new Uint8Array(w * h);
    for (let r = 0; r < h; r++) {
      const bits = unpackRow(b.mask[r], w);
      for (let c = 0; c < w; c++) mask[r * w + c] = bits[c];
    }
    const explicit = new Map(Object.entries(b.explicit));
    return new SpriteState({
      w, h, base: b.base,
      palette: { ...b.palette },
      mask, explicit,
    });
  }

  idx(r, c) {
    return r * this.w + c;
  }

  inBounds(r, c) {
    return r >= 0 && r < this.h && c >= 0 && c < this.w;
  }

  inMask(r, c) {
    return this.inBounds(r, c) && this.mask[this.idx(r, c)] === 1;
  }

  touchesMask(r, c) {
    return this.inMask(r + 1, c) || this.inMask(r - 1, c) ||
      this.inMask(r, c + 1) || this.inMask(r, c - 1);
  }

  // grow: paint a mask-adjacent empty cell as silhouette growth instead of
  // an override on the stroke ring (silhouette mode, outline display off)
  paint(r, c, ch, grow) {
    if (!this.inBounds(r, c)) return;
    const i = this.idx(r, c);
    const key = `${r},${c}`;
    if (this.mask[i] === 1) {
      if (ch === this.base) this.explicit.delete(key);
      else this.explicit.set(key, ch);
    } else if (!grow && this.touchesMask(r, c)) {
      this.explicit.set(key, ch);
    } else {
      this.mask[i] = 1;
      if (ch !== this.base) this.explicit.set(key, ch);
    }
  }

  erase(r, c) {
    if (!this.inBounds(r, c)) return;
    this.mask[this.idx(r, c)] = 0;
    this.explicit.delete(`${r},${c}`);
  }

  // outline: false hides the derived K ring for display only (silhouette
  // mode). Authored explicit overrides still render, and the save path
  // always sends the full view: decompile.py synthesize() must keep
  // matching it cell for cell.
  view(opts) {
    const outline = !opts || opts.outline !== false;
    const rows = [];
    for (let r = 0; r < this.h; r++) {
      let row = "";
      for (let c = 0; c < this.w; c++) {
        const i = r * this.w + c;
        let ch;
        if (this.mask[i] === 1) ch = this.base;
        else if (outline && this.touchesMask(r, c)) ch = "K";
        else ch = ".";
        if (ch !== ".") {
          const e = this.explicit.get(`${r},${c}`);
          if (e) ch = e;
        }
        row += ch;
      }
      rows.push(row);
    }
    return rows;
  }

  charAt(r, c) {
    if (!this.inBounds(r, c)) return null;
    return this.view()[r][c];
  }

  clone() {
    return new SpriteState({
      w: this.w, h: this.h, base: this.base,
      palette: { ...this.palette },
      mask: new Uint8Array(this.mask),
      explicit: new Map(this.explicit),
    });
  }

  snapshotEq(other) {
    if (this.base !== other.base) return false;
    const a = [...this.explicit.entries()].sort();
    const b = [...other.explicit.entries()].sort();
    return this.mask.length === other.mask.length &&
      this.mask.every((v, i) => v === other.mask[i]) &&
      a.length === b.length && a.every((p, i) => p[0] === b[i][0] && p[1] === b[i][1]);
  }

  // Move the content inside bounds (or the whole canvas) by (dr, dc).
  // Mask bits and explicit overrides travel together; the stroke ring is
  // never moved because it is recomputed from the mask on every view.
  move(dr, dc, sel) {
    const [r0, c0, r1, c1] = sel || [0, 0, this.h - 1, this.w - 1];
    const mask = new Uint8Array(this.w * this.h);
    const explicit = new Map();
    for (let r = 0; r < this.h; r++) {
      for (let c = 0; c < this.w; c++) {
        const inside = r >= r0 && r <= r1 && c >= c0 && c <= c1;
        const src = inside ? [r + dr, c + dc] : [r, c];
        const [sr, sc] = src;
        if (!this.inBounds(sr, sc)) continue;
        mask[r * this.w + c] = this.mask[sr * this.w + sc];
        const e = this.explicit.get(`${sr},${sc}`);
        if (e) explicit.set(`${r},${c}`, e);
      }
    }
    this.mask = mask;
    this.explicit = explicit;
  }

  flip(axis, sel) {
    const [r0, c0, r1, c1] = sel || [0, 0, this.h - 1, this.w - 1];
    const mask = new Uint8Array(this.mask);
    const explicit = new Map();
    for (let r = r0; r <= r1; r++) {
      for (let c = c0; c <= c1; c++) {
        const mr = axis === "h" ? r : r1 - (r - r0);
        const mc = axis === "h" ? c1 - (c - c0) : c;
        mask[mr * this.w + mc] = this.mask[r * this.w + c];
        const e = this.explicit.get(`${r},${c}`);
        if (e) explicit.set(`${mr},${mc}`, e);
      }
    }
    // clear explicit entries that landed outside their old spot
    for (const key of [...this.explicit.keys()]) {
      const [r, c] = key.split(",").map(Number);
      if (r >= r0 && r <= r1 && c >= c0 && c <= c1) this.explicit.delete(key);
    }
    this.mask = mask;
    for (const [k, v] of explicit) this.explicit.set(k, v);
  }

  payload(meta) {
    const maskRows = [];
    for (let r = 0; r < this.h; r++) {
      maskRows.push(packRow(this.mask.subarray(r * this.w, (r + 1) * this.w), this.w));
    }
    const explicit = {};
    for (const [k, v] of this.explicit.entries()) explicit[k] = v;
    return {
      ...meta,
      size: [this.w, this.h],
      base: this.base,
      palette: this.palette,
      mask: maskRows,
      explicit,
      view: this.view(),
    };
  }
}
