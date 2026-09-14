// Landing gallery (W1): one card per monster, done cards show the sprite
// next to every generation's icon, undone cards show the icons as the
// trace reference. Search matches slug / english / chinese / japanese.

import { data, iconUrl } from "./api.js";
import { t, applyDom, langSelector } from "./i18n.js";

export function renderGallery(gridEl, { onOpen }) {
  const d = data();
  const bySlug = Object.fromEntries(d.sprites.map((s) => [s.slug, s]));
  const state = { q: "", filter: "all" };

  const head = document.createElement("div");
  head.className = "gallery-top";
  head.innerHTML =
    `<div class="gallery-title"><h1>${t("gallery.title")}</h1>` +
    `<span id="glang"></span></div>` +
    `<div class="gallery-ctl">` +
    `<input id="gq" type="search" data-i18n-ph="gallery.search-ph">` +
    `<div class="chips">` +
    `<button data-f="all" class="sel">${t("gallery.all")}</button>` +
    `<button data-f="done">${t("gallery.done")}</button>` +
    `<button data-f="todo">${t("gallery.todo")}</button>` +
    `</div></div>` +
    `<div class="gallery-count" id="gcount"></div>`;
  gridEl.replaceChildren(head);
  applyDom(head);
  head.querySelector("#glang").append(langSelector());

  const cards = document.createElement("div");
  cards.className = "cards";
  gridEl.append(cards);

  head.querySelector("#gq").addEventListener("input", (e) => {
    state.q = e.target.value.trim().toLowerCase();
    refresh();
  });
  head.querySelectorAll("[data-f]").forEach((b) =>
    b.addEventListener("click", () => {
      state.filter = b.dataset.f;
      head.querySelectorAll("[data-f]").forEach((x) =>
        x.classList.toggle("sel", x === b));
      refresh();
    }));

  function refresh() {
    const doneSet = new Set(d.coverage.done);
    const list = d.monsters.filter((m) => {
      if (state.filter === "done" && !doneSet.has(m.slug)) return false;
      if (state.filter === "todo" && doneSet.has(m.slug)) return false;
      if (!state.q) return true;
      const hay = `${m.slug} ${m.name} ${m.zh} ${m.ja}`.toLowerCase();
      return hay.includes(state.q);
    });
    head.querySelector("#gcount").textContent =
      `${list.length} / ${d.monsters.length}`;
    cards.replaceChildren(...list.map((m) => card(m, bySlug[m.slug], d, onOpen)));
  }
  refresh();
}

function card(m, sprite, d, onOpen) {
  const el = document.createElement("button");
  el.className = "card" + (sprite ? " done" : " todo");
  const abbr = (code) => (d.games[code] || {}).abbr || code;
  const icons = m.games
    .sort((a, b) => d.game_order.indexOf(a.game) - d.game_order.indexOf(b.game))
    .map((g) =>
      `<span class="card-icon" title="${abbr(g.game)}">` +
      `<img src="${iconUrl(g.icon)}" loading="lazy" alt="${abbr(g.game)}"></span>`)
    .join("");
  const spriteHtml = sprite
    ? `<canvas class="card-sprite" width="${sprite.size[0] * 3}" ` +
      `height="${sprite.size[1] * 3}"></canvas>`
    : `<div class="card-empty">${t("gallery.undrawn")}</div>`;
  // all three names on every card: english left, ja/zh right
  el.innerHTML =
    `<div class="card-name"><b>${m.name}</b>` +
    `<span class="card-loc"><span class="card-ja">${m.ja || ""}</span>` +
    `<span class="card-zh">${m.zh || ""}</span></span></div>` +
    `<div class="card-row">${spriteHtml}<div class="card-icons">${icons}</div></div>`;
  el.addEventListener("click", () => onOpen(m.slug));
  if (sprite) {
    const cv = el.querySelector(".card-sprite");
    drawGrid(cv, sprite.grid, sprite.palette, 3);
  }
  return el;
}

export function drawGrid(canvas, grid, palette, scale) {
  const ctx = canvas.getContext("2d");
  const h = grid.length;
  const w = grid[0].length;
  canvas.width = w * scale;
  canvas.height = h * scale;
  for (let r = 0; r < h; r++) {
    for (let c = 0; c < w; c++) {
      const ch = grid[r][c];
      if (ch === ".") continue;
      const [pr, pg, pb] = palette[ch] || [255, 0, 255];
      ctx.fillStyle = `rgb(${pr},${pg},${pb})`;
      ctx.fillRect(c * scale, r * scale, scale, scale);
    }
  }
}
