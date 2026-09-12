// Wiring: hash routing (gallery / editor / wizard), the Aseprite-style
// tool loop, undo, the save chain, and the derived-config banner.
// Rendering truth stays in state.js + decompile.py; this file only
// routes input between them.

import {
  loadData, reloadData, data, save, ping, exportPng, downloadGrid,
  spriteBySlug, monsterBySlug,
} from "./api.js";
import { SpriteState, nearestChar, nextFreeChar } from "./state.js";
import { Undo } from "./undo.js";
import { Board } from "./canvas.js";
import { PaletteBar } from "./palette.js";
import { RefPanel, quantizeImage } from "./reference.js";
import { renderGallery, drawGrid } from "./gallery.js";
import {
  TOOLS, lineCells, shiftConstrain, rectCells, brushCells,
  pixelPerfect, floodCells,
} from "./tools.js";
import { t, applyDom, onLangChange, langSelector } from "./i18n.js";

const $ = (sel) => document.querySelector(sel);

const S = {
  slug: null,
  state: null,
  bundle: null,
  monster: null,
  isNew: false,
  docstring: "",
  compareTo: "",
  derivedFrom: "",
  dirty: false,
  serverUp: false,
};

const opt = {
  brush: 1, perfect: true, bucketContiguous: true, bucket8: false,
  rectFilled: true,
};
let toolId = "pencil";
let stroke = null; // {base, pts, anchor, button}
let wizardOpen = false;
let wizardUi = null; // {primary, width, skeleton, seedColors, baseIdx}
const undo = new Undo();
let board, pal, ref;
let spaceHeld = false;

async function boot() {
  await loadData();
  S.serverUp = await ping();
  board = new Board($("#board"), $("#board-wrap"));
  board.onStroke = onStroke;
  // local debug handles; the editor is a dev tool, not a shipped product
  window.__board = board;
  window.__S = S;
  board.onHover = onHover;
  board.onZoom = (z) => status();
  new ResizeObserver(() => board.resize()).observe($("#board-wrap"));
  pal = new PaletteBar($("#colorbar"), {
    onPick: () => status(),
  });
  ref = new RefPanel($("#refpanel"), {
    onGhostChange: updateGhost,
    onPick: pickRgb,
    onSideBySide: renderSideSprite,
  });
  buildMenubar();
  buildToolcol();
  applyDom();
  $("#langslot").append(langSelector());
  $("#btn-undo").addEventListener("click", doUndo);
  $("#btn-redo").addEventListener("click", doRedo);
  onLangChange(() => {
    applyDom();
    buildToolcol();
    setTool(toolId);
    renderDerivedBadge();
    if (pal.state) pal.render();
    if (S.state) ref.render();
    if (wizardOpen) startWizard();
    else if (!$("#page-gallery").classList.contains("hidden")) showGallery();
  });
  window.addEventListener("hashchange", route);
  window.addEventListener("keydown", onKeyDown);
  window.addEventListener("keyup", onKeyUp);
  window.addEventListener("beforeunload", (e) => {
    if (S.dirty) {
      e.preventDefault();
      e.returnValue = "";
    }
  });
  route();
}

function route() {
  const hash = location.hash || "#/";
  const [, page, slug] = hash.split("/");
  if (page === "edit" && slug) openEditor(decodeURIComponent(slug), false);
  else if (page === "new" && slug) openEditor(decodeURIComponent(slug), true);
  else showGallery();
}

function show(pageId) {
  document.querySelectorAll(".page").forEach((p) =>
    p.classList.toggle("hidden", p.id !== pageId));
}

function showGallery() {
  show("page-gallery");
  renderGallery($("#gallery-root"), {
    onOpen: (slug) => {
      location.hash = data().coverage.done.includes(slug)
        ? `#/edit/${slug}`
        : `#/new/${slug}`;
    },
  });
}

// ---------------------------------------------------------------- editor

async function openEditor(slug, isNew) {
  const monster = monsterBySlug(slug);
  if (!monster) {
    toast(t("unknown-monster", { slug }));
    location.hash = "#/";
    return;
  }
  const bundle = spriteBySlug(slug);
  if (isNew && bundle) {
    location.hash = `#/edit/${slug}`;
    return;
  }
  if (!isNew && !bundle) {
    location.hash = `#/new/${slug}`;
    return;
  }
  show("page-editor");
  S.slug = slug;
  S.monster = monster;
  S.bundle = bundle;
  S.isNew = isNew;
  S.dirty = false;
  undo.past.length = 0;
  undo.future.length = 0;
  board.selection = null;

  ref.setMonster(monster);
  renderDerivedBadge();
  if (isNew) {
    startWizard();
    return;
  }
  S.docstring = bundle.docstring;
  S.compareTo = bundle.compare_to;
  S.state = SpriteState.fromBundle(bundle);
  enterCanvas();
}

function enterCanvas() {
  $("#wizard").classList.add("hidden");
  wizardOpen = false;
  pal.attach(S.state, S.state.base);
  board.setState(S.state);
  board.fit();
  updateGhost();
  setTool(toolId);
  status();
}

function renderDerivedBadge() {
  const el = $("#derived-badge");
  const parent = S.bundle ? S.bundle.derived_from : "";
  el.classList.toggle("hidden", !parent);
  if (!parent) return;
  el.innerHTML =
    `<span class="warn">${t("badge.derived", { parent })}</span>` +
    `<button data-a="parent">${t("badge.parent")}</button>` +
    `<button data-a="stay">${t("badge.stay")}</button>`;
  el.querySelector('[data-a="parent"]').addEventListener("click", () => {
    location.hash = `#/edit/${parent}`;
  });
  el.querySelector('[data-a="stay"]').addEventListener("click", () =>
    el.classList.add("hidden"));
}

// ---------------------------------------------------------------- wizard

function startWizard() {
  const wiz = $("#wizard");
  wiz.classList.remove("hidden");
  wizardOpen = true;
  const d = data();
  // UI state survives a language re-render; a fresh wizard starts blank
  if (!wizardUi) {
    wizardUi = {
      primary: S.monster.primary_icon,
      width: 36,
      skeleton: "",
      seedColors: null,
      baseIdx: 0,
    };
  }
  let { primary, width, skeleton, seedColors, baseIdx } = wizardUi;

  const abbr = (code) => (d.games[code] || {}).abbr || code;
  const strip = [...S.monster.games]
    .sort((a, b) => d.game_order.indexOf(a.game) - d.game_order.indexOf(b.game))
    .map((g) =>
      `<button class="icon-chip ${g.icon === primary ? "sel" : ""}" data-icon="${g.icon}">` +
      `<img src="${data().icon_base + g.icon}" loading="lazy">` +
      `<span>${abbr(g.game)}</span></button>`).join("");
  const skeletons = `<option value="">${t("wiz.no-skeleton")}</option>` +
    d.skeletons.map((s) => `<option value="${s}">${s}</option>`).join("");
  wiz.innerHTML =
    `<div class="wiz-card"><h2>${t("wiz.title", { name: S.monster.name })}</h2>` +
    `<div class="wiz-step"><b>${t("wiz.step-ref")}</b><div class="ref-strip">${strip}</div></div>` +
    `<div class="wiz-step"><b>${t("wiz.canvas")}</b>` +
    `<label>${t("wiz.width")} <input id="wz-w" type="range" min="16" max="64" value="${width}"> <span id="wz-wv">${width}</span></label>` +
    `<label>${t("wiz.height-lock")}</label>` +
    `<label>${t("wiz.skeleton")} <select id="wz-skel">${skeletons}</select></label></div>` +
    `<div class="wiz-step"><b>${t("wiz.seed")}</b>` +
    `<div id="wz-seed" class="swatches"><span class="dim">${t("wiz.quantizing")}</span></div>` +
    `<div class="dim">${t("wiz.seed-hint")}</div></div>` +
    `<div class="wiz-actions"><button id="wz-go">${t("wiz.go")}</button>` +
    `<button id="wz-cancel">${t("wiz.cancel")}</button></div></div>`;

  wiz.querySelectorAll(".icon-chip").forEach((b) =>
    b.addEventListener("click", () => {
      wizardUi.primary = b.dataset.icon;
      wizardUi.seedColors = null;
      wiz.querySelectorAll(".icon-chip").forEach((x) =>
        x.classList.toggle("sel", x === b));
      loadSeed();
    }));
  const wInput = wiz.querySelector("#wz-w");
  wInput.addEventListener("input", () => {
    wizardUi.width = +wInput.value;
    wiz.querySelector("#wz-wv").textContent = wizardUi.width;
  });
  wiz.querySelector("#wz-skel").addEventListener("change", (e) => {
    wizardUi.skeleton = e.target.value;
  });
  wiz.querySelector("#wz-cancel").addEventListener("click", () => {
    wizardUi = null;
    location.hash = "#/";
  });
  wiz.querySelector("#wz-go").addEventListener("click", () => {
    finishWizard();
  });

  function loadSeed() {
    const holder = wiz.querySelector("#wz-seed");
    holder.innerHTML = `<span class="dim">${t("wiz.quantizing")}</span>`;
    const img = new Image();
    img.onload = () => {
      wizardUi.seedColors = quantizeImage(img, 6).map((rgb) => ({ rgb, keep: true }));
      wizardUi.baseIdx = 0;
      paintSeed();
    };
    img.src = data().icon_base + wizardUi.primary;
  }

  function paintSeed() {
    const holder = wiz.querySelector("#wz-seed");
    holder.innerHTML = wizardUi.seedColors.map((c, i) =>
      `<div class="swatch ${c.keep ? "" : "off"} ${i === wizardUi.baseIdx ? "fg" : ""}" ` +
      `data-i="${i}" style="background:rgb(${c.rgb.join(",")})"></div>`).join("");
    holder.querySelectorAll(".swatch").forEach((sw) =>
      sw.addEventListener("click", () => {
        const i = +sw.dataset.i;
        if (i === wizardUi.baseIdx) wizardUi.seedColors[i].keep = !wizardUi.seedColors[i].keep;
        else wizardUi.baseIdx = i;
        paintSeed();
      }));
  }

  if (seedColors) paintSeed();
  else loadSeed();
}

function finishWizard() {
  const { primary, skeleton, seedColors, baseIdx } = wizardUi;
  const width = wizardUi.width;
  const marked = seedColors[baseIdx];
  const kept = seedColors.filter((c) => c.keep);
  const baseColor = marked && marked.keep ? marked.rgb : kept[0]?.rgb;
  if (skeleton) {
    const sk = spriteBySlug(skeleton);
    S.state = SpriteState.fromBundle(sk);
    S.docstring = `${S.monster.name}: traced from the ${gameAbbrFor(primary)} icon.`;
  } else {
    const palette = { ".": [0, 0, 0, 0], "K": [24, 20, 22, 255] };
    let base = "K";
    kept.forEach((c) => {
      const ch = nextFreeChar(palette);
      if (!ch) return;
      palette[ch] = [...c.rgb, 255];
      if (c.rgb === baseColor) base = ch;
    });
    if (base === "K" && Object.keys(palette).length > 2) {
      base = Object.keys(palette)[2];
    }
    S.state = SpriteState.blank(width, 24, palette, base);
    S.docstring = `${S.monster.name}: traced from the ${gameAbbrFor(primary)} icon.`;
  }
  S.compareTo = `../icons/${primary}`;
  S.derivedFrom = "";
  wizardUi = null;
  wizardOpen = false;
  enterCanvas();
  toast(t("wiz.done"));
}

function gameAbbrFor(iconPath) {
  const code = iconPath.split("/")[0];
  return (data().games[code] || {}).abbr || code;
}

// ---------------------------------------------------------------- tools

function setTool(id) {
  toolId = id;
  document.querySelectorAll("#toolcol [data-tool]").forEach((b) =>
    b.classList.toggle("sel", b.dataset.tool === id));
  renderContextbar();
  status();
}

function buildToolcol() {
  const col = $("#toolcol");
  col.innerHTML = TOOLS.map((tl) =>
    `<button data-tool="${tl.id}" title="${t(tl.hint)}">${t(tl.label)}<` +
    `span class="key">${tl.key.toUpperCase()}</span></button>`).join("");
  col.querySelectorAll("[data-tool]").forEach((b) =>
    b.addEventListener("click", () => setTool(b.dataset.tool)));
}

function renderContextbar() {
  const bar = $("#contextbar");
  const seg = (brushable) => {
    if (!brushable) return "";
    return `<span>${t("ctx.brush")}</span>` +
      [1, 2, 3, 4].map((n) =>
        `<button class="opt ${opt.brush === n ? "sel" : ""}" data-brush="${n}">${n}</button>`).join("");
  };
  let html = "";
  if (toolId === "pencil") {
    html = seg(true) +
      `<label class="opt"><input type="checkbox" id="cb-perfect" ` +
      `${opt.perfect ? "checked" : ""} ${opt.brush > 1 ? "disabled" : ""}>pixel-perfect</label>`;
  } else if (toolId === "eraser") {
    html = seg(true);
  } else if (toolId === "bucket") {
    html =
      `<label class="opt"><input type="checkbox" id="cb-cont" ` +
      `${opt.bucketContiguous ? "checked" : ""}>${t("ctx.contiguous")}</label>` +
      `<span>${t("ctx.connectivity")}</span>` +
      `<button class="opt ${!opt.bucket8 ? "sel" : ""}" data-conn="4">4</button>` +
      `<button class="opt ${opt.bucket8 ? "sel" : ""}" data-conn="8">8</button>`;
  } else if (toolId === "line") {
    html = `<span class="dim">${t("ctx.line-hint")}</span>`;
  } else if (toolId === "rect") {
    html =
      `<button class="opt" id="cb-filled">${opt.rectFilled ? t("ctx.filled") : t("ctx.hollow")}</button>` +
      `<span class="dim">${t("ctx.rect-toggle")}</span>`;
  } else if (toolId === "marquee") {
    html = `<span class="dim">${t("ctx.marquee-hint")}</span>`;
  } else if (toolId === "move") {
    html = `<span class="dim">${t("ctx.move-hint")}</span>`;
  } else if (toolId === "picker") {
    html = `<span class="dim">${t("ctx.picker-hint")}</span>`;
  }
  bar.innerHTML = html;
  bar.querySelectorAll("[data-brush]").forEach((b) =>
    b.addEventListener("click", () => {
      opt.brush = +b.dataset.brush;
      renderContextbar();
    }));
  bar.querySelector("#cb-perfect")?.addEventListener("change", (e) => {
    opt.perfect = e.target.checked;
  });
  bar.querySelector("#cb-cont")?.addEventListener("change", (e) => {
    opt.bucketContiguous = e.target.checked;
  });
  bar.querySelectorAll("[data-conn]").forEach((b) =>
    b.addEventListener("click", () => {
      opt.bucket8 = b.dataset.conn === "8";
      renderContextbar();
    }));
  bar.querySelector("#cb-filled")?.addEventListener("click", () => {
    opt.rectFilled = !opt.rectFilled;
    renderContextbar();
  });
}

function paintChar(button) {
  return button === 2 ? (pal.bg === "." ? "." : pal.bg) : pal.fg;
}

function applyStroke(preview) {
  // preview: SpriteState mutated from stroke.base each pointer event
  const st = preview;
  const ch = paintChar(stroke.button);
  const erase = ch === ".";
  const cellsFor = () => {
    if (toolId === "pencil" || toolId === "eraser") {
      let pts = stroke.pts;
      if ((toolId === "pencil" && opt.perfect && opt.brush === 1) ||
          toolId === "eraser") {
        pts = pixelPerfect(pts);
      }
      const out = [];
      for (const [r, c] of pts) out.push(...brushCells(r, c, opt.brush));
      return out;
    }
    if (toolId === "line") {
      let [r1, c1] = stroke.cur || stroke.anchor;
      if (stroke.shift) [c1, r1] = shiftConstrain(stroke.anchor[1], stroke.anchor[0], c1, r1);
      return lineCells(stroke.anchor[1], stroke.anchor[0], c1, r1);
    }
    if (toolId === "rect") {
      const [r1, c1] = stroke.cur || stroke.anchor;
      return rectCells(stroke.anchor[0], stroke.anchor[1], r1, c1, opt.rectFilled);
    }
    return [];
  };
  if (toolId === "eraser" || (toolId === "pencil" && erase)) {
    for (const [r, c] of cellsFor()) st.erase(r, c);
  } else if (toolId === "pencil") {
    for (const [r, c] of cellsFor()) st.paint(r, c, ch);
  } else if (toolId === "line" || toolId === "rect") {
    for (const [r, c] of cellsFor()) {
      if (erase) st.erase(r, c);
      else st.paint(r, c, ch);
    }
  } else if (toolId === "bucket") {
    const view = st.view();
    const [r, c] = stroke.anchor;
    if (st.inBounds(r, c)) {
      const cells = floodCells(view, r, c, opt.bucket8 ? 8 : 4,
        opt.bucketContiguous);
      for (const [rr, cc] of cells) {
        if (erase) st.erase(rr, cc);
        else st.paint(rr, cc, ch);
      }
    }
  } else if (toolId === "move") {
    const cur = stroke.cur || stroke.anchor;
    const dr = cur[0] - stroke.anchor[0];
    const dc = cur[1] - stroke.anchor[1];
    if (dr || dc) {
      st.move(dr, dc, board.selection
        ? [board.selection.r0, board.selection.c0,
           board.selection.r1, board.selection.c1]
        : null);
    }
  }
}

function onStroke(phase, cell, e) {
  if (spaceHeld && phase === "down") {
    board.panning = { x: e.clientX, y: e.clientY };
    return;
  }
  if (phase === "down") {
    if (!cell) return;
    if (e.altKey || toolId === "picker") {
      pickFromCell(cell);
      return;
    }
    if (e.button === 1) return;
    if (toolId === "marquee") {
      stroke = { anchor: cell, marquee: true, base: S.state.clone() };
      board.selection = { r0: cell[0], c0: cell[1], r1: cell[0], c1: cell[1] };
      board.draw();
      return;
    }
    stroke = {
      base: S.state.clone(),
      pts: [cell],
      anchor: cell,
      cur: cell,
      button: e.button,
      shift: e.shiftKey,
    };
    refreshPreview();
  } else if (phase === "move") {
    if (!cell) return;
    if (stroke?.marquee) {
      board.selection = {
        r0: Math.min(stroke.anchor[0], cell[0]),
        c0: Math.min(stroke.anchor[1], cell[1]),
        r1: Math.max(stroke.anchor[0], cell[0]),
        c1: Math.max(stroke.anchor[1], cell[1]),
      };
      board.draw();
      return;
    }
    if (!stroke) return;
    stroke.shift = e.shiftKey;
    if (toolId === "pencil" || toolId === "eraser") {
      const last = stroke.pts[stroke.pts.length - 1];
      const seg = lineCells(last[1], last[0], cell[1], cell[0]);
      for (const [r, c] of seg) {
        const l = stroke.pts[stroke.pts.length - 1];
        if (!l || l[0] !== r || l[1] !== c) stroke.pts.push([r, c]);
      }
    } else {
      stroke.cur = cell;
    }
    refreshPreview();
  } else if (phase === "up") {
    if (!stroke) return;
    if (stroke.marquee) {
      stroke = null;
      status();
      return;
    }
    if (!S.state.snapshotEq(stroke.base)) {
      undo.push(stroke.base);
      S.dirty = true;
    }
    stroke = null;
    status();
  }
}

function refreshPreview() {
  const preview = stroke.base.clone();
  applyStroke(preview);
  S.state.mask = preview.mask;
  S.state.explicit = preview.explicit;
  board.draw();
  renderSideLive();
}

function pickFromCell(cell) {
  const ch = S.state.view()[cell[0]][cell[1]];
  if (ch && ch !== ".") pal.setFg(ch);
  status();
}

function pickRgb({ r, g, b }) {
  const { ch, dist } = nearestChar(S.state.palette, r, g, b);
  const rgb = `${r},${g},${b}`;
  if (ch && dist < 40) {
    pal.setFg(ch);
    toast(t("pick.picked", { ch, rgb }));
    return;
  }
  if (confirm(t("pick.add-confirm", { rgb }))) {
    const added = pal.addColor(r, g, b);
    if (added) toast(t("pick.added", { ch: added, rgb }));
  }
}

// ---------------------------------------------------------------- keyboard

function onKeyDown(e) {
  if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT" ||
      e.target.tagName === "TEXTAREA") return;
  const k = e.key.toLowerCase();
  if ((e.ctrlKey || e.metaKey) && k === "z") {
    e.preventDefault();
    if (e.shiftKey) doRedo(); else doUndo();
    return;
  }
  if ((e.ctrlKey || e.metaKey) && k === "y") {
    e.preventDefault();
    doRedo();
    return;
  }
  if ((e.ctrlKey || e.metaKey) && k === "s") {
    e.preventDefault();
    doSave();
    return;
  }
  if (e.ctrlKey || e.metaKey) return;
  if (e.shiftKey && (k === "h" || k === "v")) {
    flip(k);
    return;
  }
  if (!$("#page-editor").classList.contains("hidden") &&
      $("#wizard").classList.contains("hidden")) {
    const t = TOOLS.find((x) => x.key === k);
    if (t) {
      if (t.id === "rect" && toolId === "rect") {
        opt.rectFilled = !opt.rectFilled;
        renderContextbar();
      } else {
        setTool(t.id);
      }
      return;
    }
  }
  switch (k) {
    case " ":
      spaceHeld = true;
      e.preventDefault();
      break;
    case "x":
      pal.swap();
      break;
    case "z":
      board.setZoom(board.zoom * 2);
      break;
    case "a":
      if (ref.abActive() && !board.abHold) {
        board.abHold = true;
        board.draw();
      }
      break;
    case "=":
    case "+":
      board.setZoom(board.zoom * 2);
      break;
    case "-":
      board.setZoom(board.zoom / 2);
      break;
    case "escape":
      board.selection = null;
      board.draw();
      break;
    case "arrowleft":
    case "arrowright":
    case "arrowup":
    case "arrowdown":
      if (board.selection) {
        e.preventDefault();
        nudgeSelection(k);
      }
      break;
  }
}

function onKeyUp(e) {
  if (e.key === " ") spaceHeld = false;
  if (e.key.toLowerCase() === "a" || e.key === "A") {
    board.abHold = false;
    board.draw();
  }
}

function nudgeSelection(k) {
  const s = board.selection;
  if (k === "arrowleft") { s.c0--; s.c1--; }
  if (k === "arrowright") { s.c0++; s.c1++; }
  if (k === "arrowup") { s.r0--; s.r1--; }
  if (k === "arrowdown") { s.r0++; s.r1++; }
  s.c0 = Math.max(0, s.c0);
  s.r0 = Math.max(0, s.r0);
  s.c1 = Math.min(S.state.w - 1, s.c1);
  s.r1 = Math.min(S.state.h - 1, s.r1);
  board.draw();
}

function doUndo() {
  if (undo.undo(S.state)) {
    S.dirty = true;
    board.draw();
    renderSideLive();
    status();
  }
}

function doRedo() {
  if (undo.redo(S.state)) {
    S.dirty = true;
    board.draw();
    renderSideLive();
    status();
  }
}

function flip(axis) {
  const whole = !board.selection;
  if (axis === "h" && !confirm(t("flip.h-confirm"))) {
    return;
  }
  undo.push(S.state.clone());
  S.state.flip(axis, whole ? null : [
    board.selection.r0, board.selection.c0,
    board.selection.r1, board.selection.c1]);
  S.dirty = true;
  board.draw();
  renderSideLive();
  status();
}

// ---------------------------------------------------------------- save

async function doSave() {
  if (!S.state) return;
  if (S.bundle?.derived_from) {
    const ok = confirm(t("save.materialize-confirm",
      { slug: S.slug, parent: S.bundle.derived_from }));
    if (!ok) return;
    const parentBundle = spriteBySlug(S.bundle.derived_from);
    if (parentBundle && !(parentBundle.base in S.state.palette)) {
      toast(t("save.l11-fail"));
      return;
    }
  }
  const payload = S.state.payload({
    slug: S.slug,
    docstring: S.docstring || `${S.monster.name}: pixel sprite.`,
    compare_to: S.compareTo,
  });
  toast(t("save.saving"));
  const res = await save(payload);
  if (res.ok) {
    S.dirty = false;
    S.bundle = await refreshBundle(S.slug);
    renderDerivedBadge();
    status();
    toast(res.ok && res.changed
      ? t("save.written", { file: res.file, commit: res.commit })
      : t("save.unchanged"));
  } else {
    toast(res.error, 8000);
  }
}

async function refreshBundle(slug) {
  // data.json was rebuilt server-side; drop the cache and refetch
  await reloadData();
  return spriteBySlug(slug);
}

// ---------------------------------------------------------------- chrome

function buildMenubar() {
  document.querySelectorAll(".menu").forEach((menu) => {
    menu.addEventListener("click", (e) => {
      if (e.target.closest(".dropdown button")) return;
      document.querySelectorAll(".menu.open").forEach((m) =>
        m !== menu && m.classList.remove("open"));
      menu.classList.toggle("open");
    });
    menu.querySelectorAll(".dropdown button").forEach((b) =>
      b.addEventListener("click", () => {
        menu.classList.remove("open");
        menuAction(b.dataset.act);
      }));
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".menu")) {
      document.querySelectorAll(".menu.open").forEach((m) =>
        m.classList.remove("open"));
    }
  });
}

function menuAction(act) {
  switch (act) {
    case "save": doSave(); break;
    case "grid":
      downloadGrid(S.state.payload({
        slug: S.slug, docstring: S.docstring, compare_to: S.compareTo,
      }));
      break;
    case "png": exportPng(S.state, S.slug); break;
    case "gallery": location.hash = "#/"; break;
    case "undo": doUndo(); break;
    case "redo": doRedo(); break;
    case "flip-h": flip("h"); break;
    case "flip-v": flip("v"); break;
    case "clear":
      undo.push(S.state.clone());
      S.state.mask.fill(0);
      S.state.explicit.clear();
      S.dirty = true;
      board.draw();
      renderSideLive();
      status();
      break;
    case "zoom-in": board.setZoom(board.zoom * 2); break;
    case "zoom-out": board.setZoom(board.zoom / 2); break;
    case "fit": board.fit(); break;
    case "grid-lines":
      board.showGrid = !board.showGrid;
      board.draw();
      break;
    case "overlay": ref.setMode(ref.mode === "overlay" ? "side" : "overlay"); break;
    case "shortcuts": $("#shortcuts").classList.toggle("hidden"); break;
  }
}

function onHover(cell) {
  status(cell);
}

function status(cell) {
  const bar = $("#statusbar");
  // history buttons live in the menubar; reflect undo/redo availability
  $("#btn-undo").disabled = undo.past.length === 0;
  $("#btn-redo").disabled = undo.future.length === 0;
  if (!S.state) {
    bar.textContent = "";
    return;
  }
  const parts = [];
  if (cell) {
    const ch = S.state.view()[cell[0]][cell[1]];
    parts.push(`r${cell[0]} c${cell[1]}`, ch);
  }
  parts.push(`${board.zoom}x`, `${S.state.w}x${S.state.h}`);
  parts.push(S.dirty ? t("status.unsaved") : t("status.saved"));
  if (!S.serverUp) parts.push(t("status.offline"));
  if (S.bundle?.derived_from) parts.push(`derived from ${S.bundle.derived_from}`);
  if (S.isNew) parts.push(t("status.new"));
  bar.textContent = parts.join(" · ");
}

function updateGhost() {
  board.ghost = ref.ghost();
  board.draw();
}

function renderSideSprite(canvas) {
  const scale = Math.max(4, Math.floor(200 / S.state.h));
  drawGrid(canvas, S.state.view(), S.state.palette, scale);
  canvas.style.width = "auto";
}

function renderSideLive() {
  const canvas = document.querySelector(".side-sprite");
  if (canvas && S.state) renderSideSprite(canvas);
}

let toastTimer = null;
function toast(msg, ms = 4200) {
  const el = $("#toast");
  el.textContent = msg;
  el.classList.remove("hidden");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => el.classList.add("hidden"), ms);
}

boot();
