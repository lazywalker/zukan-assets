// Navigator: whole-canvas thumbnail with the visible viewport outlined.
// Click or drag inside the thumbnail moves the main view to that point.
// Pointer events must not reach #board-wrap underneath (it paints).

export class Navigator {
  constructor(board, host) {
    this.board = board;
    this.box = document.createElement("div");
    this.box.className = "navigator";
    this.canvas = document.createElement("canvas");
    this.box.append(this.canvas);
    host.append(this.box);
    this.dragging = false;
    for (const ev of ["pointerdown", "pointermove", "pointerup"]) {
      this.box.addEventListener(ev, (e) => e.stopPropagation());
    }
    this.canvas.addEventListener("pointerdown", (e) => {
      this.dragging = true;
      this.canvas.setPointerCapture(e.pointerId);
      this.jump(e);
    });
    this.canvas.addEventListener("pointermove", (e) => {
      if (this.dragging) this.jump(e);
    });
    this.canvas.addEventListener("pointerup", () => {
      this.dragging = false;
    });
    board.onRedraw = () => this.sync();
  }

  // minimap scale: fit the sprite into a ~150x110 box
  scale() {
    const b = this.board.state;
    return Math.min(150 / b.w, 110 / b.h);
  }

  jump(e) {
    const rect = this.canvas.getBoundingClientRect();
    const k = this.scale();
    this.board.centerOn((e.clientX - rect.left) / k,
      (e.clientY - rect.top) / k);
  }

  sync() {
    const b = this.board;
    if (!b.state) return;
    const k = this.scale();
    const w = Math.round(b.state.w * k);
    const h = Math.round(b.state.h * k);
    const dpr = window.devicePixelRatio || 1;
    if (this.canvas.width !== Math.round(w * dpr)) {
      this.canvas.width = Math.round(w * dpr);
      this.canvas.height = Math.round(h * dpr);
      this.canvas.style.width = `${w}px`;
      this.canvas.style.height = `${h}px`;
    }
    const ctx = this.canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    const view = b.state.view({ outline: b.showOutline });
    for (let r = 0; r < b.state.h; r++) {
      for (let c = 0; c < b.state.w; c++) {
        const ch = view[r][c];
        if (ch === ".") continue;
        const [pr, pg, pb] = b.state.palette[ch] || [255, 0, 255];
        ctx.fillStyle = `rgb(${pr},${pg},${pb})`;
        ctx.fillRect(c * k, r * k, Math.max(1, k), Math.max(1, k));
      }
    }
    const v = b.visibleRect();
    const x0 = Math.max(0.5, v.x * k);
    const y0 = Math.max(0.5, v.y * k);
    const x1 = Math.min(w - 0.5, (v.x + v.w) * k);
    const y1 = Math.min(h - 0.5, (v.y + v.h) * k);
    if (x1 > x0 && y1 > y0) {
      ctx.strokeStyle = "#e8b45a";
      ctx.lineWidth = 1;
      ctx.strokeRect(x0, y0, x1 - x0, y1 - y0);
    }
  }
}
