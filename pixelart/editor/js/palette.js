// fg/bg dual slot (left click paints fg, right click bg, X swaps) over the
// config's indexed palette. Only in-palette chars are paintable; past 8
// colors the panel reminds of guide 5.5.

import { nextFreeChar } from "./state.js";
import { t } from "./i18n.js";

export class PaletteBar {
  constructor(el, { onPick } = {}) {
    this.el = el;
    this.onPick = onPick;
    this.fg = "K";
    this.bg = ".";
    this.state = null;
    el.addEventListener("pointerdown", (e) => {
      const swatch = e.target.closest("[data-ch]");
      if (!swatch) return;
      const ch = swatch.dataset.ch;
      if (e.button === 2) this.bg = ch;
      else this.fg = ch;
      this.render();
      if (this.onPick) this.onPick(ch);
    });
    el.addEventListener("contextmenu", (e) => e.preventDefault());
  }

  attach(state, fg) {
    this.state = state;
    if (fg) this.fg = fg;
    if (!(this.bg in state.palette)) this.bg = ".";
    if (!(this.fg in state.palette)) this.fg = state.base;
    this.render();
  }

  swap() {
    [this.fg, this.bg] = [this.bg, this.fg];
    this.render();
  }

  setFg(ch) {
    if (ch && ch in this.state.palette) {
      this.fg = ch;
      this.render();
    }
  }

  addColor(r, g, b) {
    const ch = nextFreeChar(this.state.palette);
    if (!ch) return null;
    this.state.palette[ch] = [r, g, b, 255];
    this.fg = ch;
    this.render();
    return ch;
  }

  render() {
    if (!this.state) return;
    const chars = Object.keys(this.state.palette).filter((c) => c !== ".");
    const cell = (ch) => {
      const [r, g, b] = this.state.palette[ch];
      const mark = ch === this.fg ? "fg" : ch === this.bg ? "bg" : "";
      return `<div class="swatch ${mark}" data-ch="${ch}" ` +
        `style="background:rgb(${r},${g},${b})" title="${ch}"></div>`;
    };
    const over = chars.length > 8;
    // the visible input itself is the affordance: Safari only opens the
    // color panel for a trusted click on the element, so a hidden input
    // driven by .click() stays dead there
    this.el.innerHTML =
      `<div class="fgbg">${cell(this.fg)}${cell(this.bg === "." ? "K" : this.bg)}</div>` +
      `<div class="swatches">${chars.map(cell).join("")}</div>` +
      `<input type="color" class="add-color" value="${this.lastAdd || "#c05030"}" ` +
      `title="${t("pal.add-title")}">` +
      (over ? `<div class="pal-hint">${t("pal.over-hint")}</div>` : "");
    this.el.querySelector(".add-color").addEventListener("change", (e) => {
      const ch = nextFreeChar(this.state.palette);
      if (!ch) {
        alert(t("pal.exhausted"));
        return;
      }
      const hex = e.target.value;
      const r = parseInt(hex.slice(1, 3), 16);
      const g = parseInt(hex.slice(3, 5), 16);
      const b = parseInt(hex.slice(5, 7), 16);
      this.lastAdd = hex;
      if (confirm(t("pal.add-confirm", { ch, rgb: `${r},${g},${b}` }))) {
        this.addColor(r, g, b);
      }
    });
  }
}
