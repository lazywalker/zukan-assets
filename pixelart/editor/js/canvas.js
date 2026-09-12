// Canvas board: checkerboard (CSS) + sprite pixels + optional grid lines
// (zoom >= 8) + ghost underlay + A/B hold. Full redraw per change; at
// 36x24 there is nothing to optimize. Pointer events are translated to
// cell coordinates and handed to callbacks set by main.js.

const CHECKER = 8;

export class Board {
  constructor(canvasEl, wrapEl) {
    this.canvas = canvasEl;
    this.ctx = canvasEl.getContext("2d");
    this.wrap = wrapEl;
    this.zoom = 16;
    this.pan = { x: 0, y: 0 };
    this.state = null;
    this.ghost = null; // {img, opacity, dx} reference underlay
    this.abHold = false; // while true, show the reference instead
    this.selection = null; // {r0, c0, r1, c1} normalized
    this.hover = null; // [r, c]
    this.onStroke = null; // (phase, cell, button) -> bool
    this.showGrid = true;

    wrapEl.addEventListener("pointerdown", (e) => this.pointerDown(e));
    wrapEl.addEventListener("pointermove", (e) => this.pointerMove(e));
    wrapEl.addEventListener("pointerup", (e) => this.pointerUp(e));
    wrapEl.addEventListener("pointerleave", () => {
      this.hover = null;
      this.draw();
      if (this.onHover) this.onHover(null);
    });
    wrapEl.addEventListener("contextmenu", (e) => e.preventDefault());
    wrapEl.addEventListener("wheel", (e) => {
      e.preventDefault();
      const dir = e.deltaY < 0 ? 2 : 0.5;
      this.setZoom(this.zoom * dir, e);
    }, { passive: false });
  }

  setState(state) {
    this.state = state;
    this.draw();
  }

  fit() {
    const rect = this.wrap.getBoundingClientRect();
    const z = Math.max(4, Math.min(32,
      Math.floor(Math.min(rect.width / (this.state.w + 4),
        rect.height / (this.state.h + 4)))));
    this.zoom = z;
    this.center();
  }

  center() {
    const rect = this.wrap.getBoundingClientRect();
    this.pan.x = Math.round((rect.width - this.state.w * this.zoom) / 2);
    this.pan.y = Math.round((rect.height - this.state.h * this.zoom) / 2);
    this.draw();
  }

  setZoom(z, event) {
    const nz = Math.max(4, Math.min(32, Math.round(z)));
    if (nz === this.zoom) return;
    if (event) {
      // keep the cell under the cursor pinned
      const rect = this.wrap.getBoundingClientRect();
      const mx = event.clientX - rect.left;
      const my = event.clientY - rect.top;
      const cx = (mx - this.pan.x) / this.zoom;
      const cy = (my - this.pan.y) / this.zoom;
      this.zoom = nz;
      this.pan.x = Math.round(mx - cx * nz);
      this.pan.y = Math.round(my - cy * nz);
    } else {
      this.zoom = nz;
    }
    this.draw();
    if (this.onZoom) this.onZoom(nz);
  }

  cellAt(e) {
    const rect = this.wrap.getBoundingClientRect();
    const x = e.clientX - rect.left - this.pan.x;
    const y = e.clientY - rect.top - this.pan.y;
    const c = Math.floor(x / this.zoom);
    const r = Math.floor(y / this.zoom);
    if (!this.state.inBounds(r, c)) return null;
    return [r, c];
  }

  pointerDown(e) {
    if (e.pointerId != null) this.wrap.setPointerCapture(e.pointerId);
    const cell = this.cellAt(e);
    if (this.onStroke) this.onStroke("down", cell, e);
    if (e.button === 1) this.panning = { x: e.clientX, y: e.clientY };
  }

  pointerMove(e) {
    if (this.panning) {
      this.pan.x += e.clientX - this.panning.x;
      this.pan.y += e.clientY - this.panning.y;
      this.panning = { x: e.clientX, y: e.clientY };
      this.draw();
      return;
    }
    const cell = this.cellAt(e);
    this.hover = cell;
    if (this.onStroke) this.onStroke("move", cell, e);
    if (this.onHover) this.onHover(cell);
  }

  pointerUp(e) {
    this.panning = null;
    const cell = this.cellAt(e);
    if (this.onStroke) this.onStroke("up", cell, e);
  }

  resize() {
    const rect = this.wrap.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.canvas.width = Math.round(rect.width * dpr);
    this.canvas.height = Math.round(rect.height * dpr);
    this.canvas.style.width = `${rect.width}px`;
    this.canvas.style.height = `${rect.height}px`;
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.draw();
  }

  draw() {
    const { ctx, state } = this;
    if (!state) return;
    const rect = this.wrap.getBoundingClientRect();
    ctx.clearRect(0, 0, rect.width, rect.height);
    const z = this.zoom;
    const x0 = this.pan.x;
    const y0 = this.pan.y;

    if (this.abHold && this.ghost && this.ghost.img) {
      this.drawGhostFitted(rect, z);
      return;
    }

    // checkerboard under the sprite area only
    ctx.save();
    ctx.beginPath();
    ctx.rect(x0, y0, state.w * z, state.h * z);
    ctx.clip();
    for (let y = 0; y < state.h * z; y += CHECKER) {
      for (let x = 0; x < state.w * z; x += CHECKER) {
        const dark = ((x / CHECKER) | 0) % 2 === ((y / CHECKER) | 0) % 2;
        ctx.fillStyle = dark ? "#26282e" : "#2e3138";
        ctx.fillRect(x0 + x, y0 + y, CHECKER, CHECKER);
      }
    }
    if (this.ghost && this.ghost.img && this.ghost.opacity > 0) {
      this.drawGhostFitted(rect, z);
    }
    ctx.restore();

    const view = state.view();
    for (let r = 0; r < state.h; r++) {
      for (let c = 0; c < state.w; c++) {
        const ch = view[r][c];
        if (ch === ".") continue;
        const [pr, pg, pb] = state.palette[ch] || [255, 0, 255];
        ctx.fillStyle = `rgb(${pr},${pg},${pb})`;
        ctx.fillRect(x0 + c * z, y0 + r * z, z, z);
      }
    }

    if (this.showGrid && z >= 8) {
      ctx.strokeStyle = "rgba(255,255,255,0.08)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      for (let c = 0; c <= state.w; c++) {
        ctx.moveTo(x0 + c * z + 0.5, y0);
        ctx.lineTo(x0 + c * z + 0.5, y0 + state.h * z);
      }
      for (let r = 0; r <= state.h; r++) {
        ctx.moveTo(x0, y0 + r * z + 0.5);
        ctx.lineTo(x0 + state.w * z, y0 + r * z + 0.5);
      }
      ctx.stroke();
    }

    if (this.selection) {
      const { r0, c0, r1, c1 } = this.selection;
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 3]);
      ctx.strokeRect(x0 + c0 * z + 0.5, y0 + r0 * z + 0.5,
        (c1 - c0 + 1) * z - 1, (r1 - r0 + 1) * z - 1);
      ctx.setLineDash([]);
    }

    if (this.hover && !this.abHold) {
      const [r, c] = this.hover;
      ctx.strokeStyle = "rgba(255,255,255,0.9)";
      ctx.lineWidth = 2;
      ctx.strokeRect(x0 + c * z + 1, y0 + r * z + 1, z - 2, z - 2);
    }
  }

  // reference image normalized to the sprite height, horizontally
  // centered plus a user offset (icons range 62px to 552px and are not
  // square, so height is the only shared axis)
  drawGhostFitted(rect, z) {
    const { ctx } = this;
    const img = this.ghost.img;
    const th = this.state.h * z;
    const tw = Math.round(img.width * th / img.height);
    const dx = this.ghost.dx || 0;
    const x = this.pan.x + Math.round((this.state.w * z - tw) / 2) + dx * z;
    const y = this.pan.y;
    ctx.save();
    ctx.imageSmoothingEnabled = false;
    ctx.globalAlpha = this.abHold ? 1 : this.ghost.opacity / 100;
    ctx.drawImage(img, x, y, tw, th);
    ctx.restore();
  }
}
