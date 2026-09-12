// Data bundle access and the save chain. With editor_server.py running,
// save POSTs to it; without a server the same payload downloads as a
// grid JSON for `python3 pixelart/apply_grid.py dump.json`.

import { t } from "./i18n.js";

let DATA = null;

export async function loadData() {
  if (DATA) return DATA;
  const res = await fetch("_data/data.json");
  if (!res.ok) throw new Error(`data.json ${res.status}`);
  DATA = await res.json();
  return DATA;
}

export async function reloadData() {
  DATA = null;
  return loadData();
}

export function data() {
  return DATA;
}

export function iconUrl(iconPath) {
  return DATA.icon_base + iconPath;
}

export function spriteBySlug(slug) {
  return DATA.sprites.find((s) => s.slug === slug) || null;
}

export function monsterBySlug(slug) {
  return DATA.monsters.find((m) => m.slug === slug) || null;
}

export async function ping() {
  try {
    const res = await fetch("api/ping");
    return res.ok;
  } catch {
    return false;
  }
}

function download(name, text, type = "application/json") {
  const blob = new Blob([text], { type });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = name;
  a.click();
  URL.revokeObjectURL(a.href);
}

// Returns {ok, ...report} from the server, or {ok: false, offline: true}
// after dropping the payload as a dump file for apply_grid.py.
export async function save(payload) {
  try {
    const res = await fetch("api/save", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const body = await res.json().catch(() => ({}));
    if (!res.ok) return { ok: false, error: body.error || `HTTP ${res.status}` };
    return body;
  } catch {
    download(`${payload.slug}-grid.json`, JSON.stringify(payload, null, 2));
    return {
      ok: false,
      offline: true,
      error: t("api.offline"),
    };
  }
}

export function exportPng(state, name, scale = 8) {
  const canvas = document.createElement("canvas");
  canvas.width = state.w * scale;
  canvas.height = state.h * scale;
  const ctx = canvas.getContext("2d");
  ctx.imageSmoothingEnabled = false;
  const view = state.view();
  for (let r = 0; r < state.h; r++) {
    for (let c = 0; c < state.w; c++) {
      const ch = view[r][c];
      if (ch === ".") continue;
      const [pr, pg, pb, pa] = state.palette[ch] || [255, 0, 255, 255];
      ctx.fillStyle = `rgba(${pr},${pg},${pb},${(pa ?? 255) / 255})`;
      ctx.fillRect(c * scale, r * scale, scale, scale);
    }
  }
  canvas.toBlob((blob) => {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `${name}.png`;
    a.click();
    URL.revokeObjectURL(a.href);
  });
}

export function downloadGrid(payload) {
  download(`${payload.slug}-grid.json`, JSON.stringify(payload, null, 2));
}
