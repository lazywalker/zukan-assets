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

// nibble-at-a-time: JS bitwise ops are 32-bit, and sprites run 36 wide
export function packRow(bits, w) {
  let out = "";
  for (let i = 0; i < Math.ceil(w / 4); i++) {
    let n = 0;
    for (let j = 0; j < 4; j++) {
      const c = i * 4 + j;
      n = (n << 1) | (c < w && bits[c] ? 1 : 0);
    }
    out += n.toString(16);
  }
  return out;
}

export function unpackRow(hex, w) {
  const bits = new Uint8Array(w);
  for (let i = 0; i < hex.length; i++) {
    const n = parseInt(hex[i], 16);
    for (let j = 0; j < 4; j++) {
      const c = i * 4 + j;
      if (c < w) bits[c] = (n >> (3 - j)) & 1;
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

  paint(r, c, ch) {
    if (!this.inBounds(r, c)) return;
    const i = this.idx(r, c);
    const key = `${r},${c}`;
    if (this.mask[i] === 1) {
      if (ch === this.base) this.explicit.delete(key);
      else this.explicit.set(key, ch);
    } else if (this.touchesMask(r, c)) {
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

  view() {
    const rows = [];
    for (let r = 0; r < this.h; r++) {
      let row = "";
      for (let c = 0; c < this.w; c++) {
        const i = this.idx(r, c);
        let ch;
        if (this.mask[i] === 1) ch = this.base;
        else if (this.touchesMask(r, c)) ch = "K";
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
