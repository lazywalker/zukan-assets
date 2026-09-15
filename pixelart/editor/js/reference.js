// Per-generation icon strip, one large primary reference, three compare
// modes (side by side / ghost underlay / A-B hold), color picking off the
// reference, and the palette seed quantizer for the new-sprite wizard.

import { iconUrl, data } from "./api.js";
import { t } from "./i18n.js";

export class RefPanel {
  constructor(el, { onGhostChange, onPick } = {}) {
    this.el = el;
    this.onGhostChange = onGhostChange;
    this.onPick = onPick;
    this.monster = null;
    this.primary = null; // icon path like "mh4u/rathalos.png"
    this.mode = "side";
    this.img = null; // loaded primary, for ghost/AB/picking
    this.opacity = 40;
    this.dx = 0;
  }

  setMonster(monster) {
    this.monster = monster;
    this.primary = monster.primary_icon;
    this.dx = 0;
    this.loadPrimary();
    this.render();
  }

  setPrimary(iconPath) {
    this.primary = iconPath;
    this.dx = 0;
    this.loadPrimary();
    this.render();
  }

  loadPrimary() {
    this.img = null;
    this.pickCanvas = null;
    const img = new Image();
    img.onload = () => {
      this.img = img;
      const cv = document.createElement("canvas");
      cv.width = img.naturalWidth;
      cv.height = img.naturalHeight;
      cv.getContext("2d").drawImage(img, 0, 0);
      this.pickCanvas = cv;
      if (this.onGhostChange) this.onGhostChange();
    };
    img.src = iconUrl(this.primary);
  }

  setMode(mode) {
    this.mode = mode;
    this.render();
    if (this.onGhostChange) this.onGhostChange();
  }

  ghost() {
    if (!this.img) return null;
    return { img: this.img, opacity: this.mode === "overlay" ? this.opacity : 0, dx: this.dx };
  }

  abActive() {
    return this.mode === "ab";
  }

  gameAbbr(code) {
    return (data().games[code] || {}).abbr || code.toUpperCase();
  }

  // sorted by release for the strip; mho last
  orderedGames() {
    const order = data().game_order;
    return [...this.monster.games].sort(
      (a, b) => order.indexOf(a.game) - order.indexOf(b.game));
  }

  render() {
    if (!this.monster) {
      this.el.innerHTML = "";
      return;
    }
    const strip = this.orderedGames().map((g) =>
      `<button class="icon-chip ${g.icon === this.primary ? "sel" : ""}" ` +
      `data-icon="${g.icon}" title="${this.gameAbbr(g.game)}">` +
      `<img src="${iconUrl(g.icon)}" loading="lazy" alt="${g.game}">` +
      `<span>${this.gameAbbr(g.game)}</span></button>`).join("");
    this.el.innerHTML =
      `<div class="ref-head">${t("ref.head")}</div>` +
      `<div class="ref-strip">${strip}</div>` +
      `<div class="ref-modes">` +
      `<button data-mode="side" class="${this.mode === "side" ? "sel" : ""}">${t("ref.side")}</button>` +
      `<button data-mode="overlay" class="${this.mode === "overlay" ? "sel" : ""}">${t("ref.overlay")}</button>` +
      `<button data-mode="ab" class="${this.mode === "ab" ? "sel" : ""}">${t("ref.ab")}</button>` +
      `</div>` +
      `<div class="ref-stage" id="ref-stage"></div>` +
      (this.mode === "overlay"
        ? `<div class="ref-ctl">${t("ref.opacity")}<input id="ghost-alpha" type="range" ` +
          `min="0" max="100" value="${this.opacity}"> ${this.opacity}%` +
          `<div class="ref-ctl-row">${t("ref.offset")} <button id="ghost-l">←</button> ` +
          `<span id="ghost-dx">${this.dx}</span> <button id="ghost-r">→</button></div></div>`
        : "");
    this.el.querySelectorAll(".icon-chip").forEach((b) =>
      b.addEventListener("click", () => this.setPrimary(b.dataset.icon)));
    this.el.querySelectorAll("[data-mode]").forEach((b) =>
      b.addEventListener("click", () => this.setMode(b.dataset.mode)));
    const alpha = this.el.querySelector("#ghost-alpha");
    if (alpha) {
      alpha.addEventListener("input", () => {
        this.opacity = +alpha.value;
        this.refreshAlphaLabel();
        if (this.onGhostChange) this.onGhostChange();
      });
    }
    this.el.querySelector("#ghost-l")?.addEventListener("click", () => this.nudge(-1));
    this.el.querySelector("#ghost-r")?.addEventListener("click", () => this.nudge(1));
    this.renderStage();
  }

  refreshAlphaLabel() {
    const ctl = this.el.querySelector(".ref-ctl");
    if (!ctl) return;
    const txt = ctl.firstChild.textContent.replace(/\d+%/,
      `${this.opacity}%`);
    ctl.firstChild.textContent = txt;
  }

  nudge(d) {
    this.dx += d;
    const span = this.el.querySelector("#ghost-dx");
    if (span) span.textContent = this.dx;
    if (this.onGhostChange) this.onGhostChange();
  }

  renderStage() {
    const stage = this.el.querySelector("#ref-stage");
    if (!stage) return;
    if (this.mode === "side") {
      const side = document.createElement("div");
      side.className = "side-by-side";
      const left = document.createElement("img");
      left.src = iconUrl(this.primary);
      left.addEventListener("pointerdown", (e) => {
        if (!e.altKey || !this.pickCanvas) return;
        const nx = Math.round(e.offsetX / left.clientWidth * this.pickCanvas.width);
        const ny = Math.round(e.offsetY / left.clientHeight * this.pickCanvas.height);
        const px = this.pickCanvas.getContext("2d")
          .getImageData(Math.min(nx, this.pickCanvas.width - 1),
            Math.min(ny, this.pickCanvas.height - 1), 1, 1).data;
        if (this.onPick) this.onPick({ r: px[0], g: px[1], b: px[2] });
      });
      const right = document.createElement("canvas");
      right.className = "side-sprite";
      side.append(left, right);
      stage.append(side);
      if (this.onSideBySide) this.onSideBySide(right);
    } else if (this.mode === "overlay") {
      const hint = document.createElement("div");
      hint.className = "ref-hint";
      hint.textContent = t("ref.hint-overlay");
      stage.append(hint);
    } else {
      const hint = document.createElement("div");
      hint.className = "ref-hint";
      hint.textContent = t("ref.hint-ab");
      stage.append(hint);
    }
  }
}

// Median-cut quantization to n colors; used to seed a palette from the
// reference icon (a starting point only, the human decides the final set).
export function quantizeImage(img, n = 6) {
  const w = 48;
  const h = Math.max(1, Math.round(img.height * w / img.width));
  const cv = document.createElement("canvas");
  cv.width = w;
  cv.height = h;
  const ctx = cv.getContext("2d");
  ctx.imageSmoothingEnabled = true;
  ctx.drawImage(img, 0, 0, w, h);
  const pixels = [];
  const d = ctx.getImageData(0, 0, w, h).data;
  for (let i = 0; i < d.length; i += 4) {
    if (d[i + 3] < 128) continue; // skip transparent card background
    pixels.push([d[i], d[i + 1], d[i + 2]]);
  }
  if (!pixels.length) return [];
  let buckets = [pixels];
  while (buckets.length < n) {
    buckets.sort((a, b) => spread(b) - spread(a));
    const widest = buckets.shift();
    if (!widest || widest.length < 2) {
      if (widest) buckets.push(widest);
      break;
    }
    const axis = widestSpreadAxis(widest);
    widest.sort((p, q) => p[axis] - q[axis]);
    const mid = widest.length >> 1;
    buckets.push(widest.slice(0, mid), widest.slice(mid));
  }
  return buckets.map(avg).sort((a, b) => lum(b) - lum(a));
}

function spread(bucket) {
  let mx = 0;
  for (let a = 0; a < 3; a++) {
    let lo = 255;
    let hi = 0;
    for (const p of bucket) {
      if (p[a] < lo) lo = p[a];
      if (p[a] > hi) hi = p[a];
    }
    mx = Math.max(mx, hi - lo);
  }
  return mx;
}

function widestSpreadAxis(bucket) {
  let axis = 0;
  let best = -1;
  for (let a = 0; a < 3; a++) {
    let lo = 255;
    let hi = 0;
    for (const p of bucket) {
      if (p[a] < lo) lo = p[a];
      if (p[a] > hi) hi = p[a];
    }
    if (hi - lo > best) {
      best = hi - lo;
      axis = a;
    }
  }
  return axis;
}

function avg(bucket) {
  const s = [0, 0, 0];
  for (const p of bucket) {
    s[0] += p[0];
    s[1] += p[1];
    s[2] += p[2];
  }
  return s.map((v) => Math.round(v / bucket.length));
}

function lum([r, g, b]) {
  return 0.3 * r + 0.6 * g + 0.1 * b;
}
