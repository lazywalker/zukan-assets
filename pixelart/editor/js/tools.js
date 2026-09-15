// Geometry and fill helpers, pure so selftest.html can exercise them
// without a canvas. Tool wiring lives in main.js.

export function lineCells(x0, y0, x1, y1) {
  const cells = [];
  const dx = Math.abs(x1 - x0);
  const dy = -Math.abs(y1 - y0);
  const sx = x0 < x1 ? 1 : -1;
  const sy = y0 < y1 ? 1 : -1;
  let err = dx + dy;
  let x = x0;
  let y = y0;
  for (;;) {
    cells.push([y, x]);
    if (x === x1 && y === y1) break;
    const e2 = 2 * err;
    if (e2 >= dy) {
      err += dy;
      x += sx;
    }
    if (e2 <= dx) {
      err += dx;
      y += sy;
    }
  }
  return cells;
}

// Snap the free end of a line to horizontal / vertical / 45 degrees.
export function shiftConstrain(x0, y0, x1, y1) {
  const dx = x1 - x0;
  const dy = y1 - y0;
  if (Math.abs(dx) > 2 * Math.abs(dy)) return [x1, y0];
  if (Math.abs(dy) > 2 * Math.abs(dx)) return [x0, y1];
  const d = Math.min(Math.abs(dx), Math.abs(dy));
  return [x0 + Math.sign(dx) * d, y0 + Math.sign(dy) * d];
}

export function rectCells(r0, c0, r1, c1, filled) {
  const [ra, rb] = [Math.min(r0, r1), Math.max(r0, r1)];
  const [ca, cb] = [Math.min(c0, c1), Math.max(c0, c1)];
  const cells = [];
  for (let r = ra; r <= rb; r++) {
    for (let c = ca; c <= cb; c++) {
      const edge = r === ra || r === rb || c === ca || c === cb;
      if (filled || edge) cells.push([r, c]);
    }
  }
  return cells;
}

export function brushCells(r, c, size) {
  const cells = [];
  for (let dr = 0; dr < size; dr++) {
    for (let dc = 0; dc < size; dc++) cells.push([r + dr, c + dc]);
  }
  return cells;
}

// Remove the corner pixel of every L in a freehand 1px stroke (Aseprite
// pixel-perfect). Input must be gapless (interpolate first): with unit
// steps, A and C diagonal neighbors means B is the L corner between them.
// Endpoints are never dropped, so a stroke that stops on a corner keeps it.
export function pixelPerfect(points) {
  const pts = [];
  for (const p of points) {
    const last = pts[pts.length - 1];
    if (!last || last[0] !== p[0] || last[1] !== p[1]) pts.push(p);
  }
  if (pts.length <= 2) return pts;
  const drop = new Set();
  for (let i = 1; i < pts.length - 1; i++) {
    const [a, c] = [pts[i - 1], pts[i + 1]];
    if (Math.abs(a[0] - c[0]) === 1 && Math.abs(a[1] - c[1]) === 1) drop.add(i);
  }
  return pts.filter((_, i) => !drop.has(i));
}

// Same-char region at (r, c) on a grid of row strings. Tolerance is zero:
// palette indexing means exact char match. connectivity 4 or 8; pass
// contiguous false for the global bucket.
export function floodCells(view, r, c, connectivity, contiguous) {
  const h = view.length;
  const w = view[0].length;
  const target = view[r][c];
  const hit = (rr, cc) => rr >= 0 && rr < h && cc >= 0 && cc < w &&
    view[rr][cc] === target;
  if (!contiguous) {
    const cells = [];
    for (let rr = 0; rr < h; rr++) {
      for (let cc = 0; cc < w; cc++) {
        if (view[rr][cc] === target) cells.push([rr, cc]);
      }
    }
    return cells;
  }
  const seen = new Set();
  const queue = [[r, c]];
  const cells = [];
  while (queue.length) {
    const [rr, cc] = queue.pop();
    const key = `${rr},${cc}`;
    if (seen.has(key) || !hit(rr, cc)) continue;
    seen.add(key);
    cells.push([rr, cc]);
    const next = connectivity === 8
      ? [[rr - 1, cc], [rr + 1, cc], [rr, cc - 1], [rr, cc + 1],
         [rr - 1, cc - 1], [rr - 1, cc + 1], [rr + 1, cc - 1], [rr + 1, cc + 1]]
      : [[rr - 1, cc], [rr + 1, cc], [rr, cc - 1], [rr, cc + 1]];
    for (const n of next) queue.push(n);
  }
  return cells;
}

// Labels/hints are i18n keys; buildToolcol resolves them at render time so
// a language switch re-renders the toolbar.
export const TOOLS = [
  { id: "pencil", key: "b", label: "tool.pencil", hint: "hint.pencil" },
  { id: "eraser", key: "e", label: "tool.eraser", hint: "hint.eraser" },
  { id: "bucket", key: "g", label: "tool.bucket", hint: "hint.bucket" },
  { id: "line", key: "l", label: "tool.line", hint: "hint.line" },
  { id: "rect", key: "u", label: "tool.rect", hint: "hint.rect" },
  { id: "marquee", key: "m", label: "tool.marquee", hint: "hint.marquee" },
  { id: "move", key: "v", label: "tool.move", hint: "hint.move" },
  { id: "picker", key: "i", label: "tool.picker", hint: "hint.picker" },
];

export const MAX_HISTORY = 100;
