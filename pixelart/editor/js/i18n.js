// UI language: browser detection with a localStorage override, t() lookup
// with {var} interpolation, and an onLangChange hook so each page component
// can re-render its strings. Dictionaries: en / zh / ja.

const STORAGE_KEY = "pixelart-editor-lang";

const DICTS = {
  en: {
    "menu.file": "File",
    "menu.edit": "Edit",
    "menu.view": "View",
    "menu.help": "Help",
    "act.save": "Save Ctrl+S",
    "act.grid": "Download grid JSON",
    "act.png": "Export PNG",
    "act.gallery": "Back to gallery",
    "act.undo": "Undo Ctrl+Z",
    "act.redo": "Redo Ctrl+Y",
    "act.flip-h": "Flip horizontal (warns)",
    "act.flip-v": "Flip vertical",
    "act.clear": "Clear canvas",
    "act.zoom-in": "Zoom in",
    "act.zoom-out": "Zoom out",
    "act.fit": "Fit window",
    "act.grid-lines": "Toggle grid lines",
    "act.overlay": "Toggle reference overlay",
    "act.shortcuts": "Shortcuts",
    "shortcuts.title": "Shortcuts (Aseprite mapping)",
    "shortcuts.close": "Close",
    "sc.pencil": "Pencil (1-4px, pixel-perfect on by default)",
    "sc.eraser": "Eraser (erases mask, stroke shrinks)",
    "sc.picker": "Pick color (canvas and reference image)",
    "sc.bucket": "Fill (contiguous/global, 4/8-connected)",
    "sc.line": "Line (Shift constrains H/V/45°)",
    "sc.rect": "Rectangle (press U again to toggle filled)",
    "sc.marquee": "Rect select (arrows nudge, Esc cancels)",
    "sc.move": "Move selection (no selection: whole image)",
    "sc.zoom": "Zoom (mouse wheel works too)",
    "sc.pan": "Pan",
    "sc.swap": "Swap foreground/background color",
    "sc.rightbtn": "Paint background color",
    "sc.undo": "Undo / Redo",
    "sc.flip": "Flip (horizontal breaks the facing-left rule, warns)",
    "sc.alternate": "Hold A: show original / release: show sprite",
    "sc.save": "Save (writes sprites/<slug>.py)",

    "unknown-monster": "Unknown monster: {slug}",
    "badge.derived": "derived from {parent}",
    "badge.parent": "Edit parent",
    "badge.stay": "Stay here",

    "wiz.no-skeleton": "No skeleton",
    "wiz.title": "Trace {name}",
    "wiz.step-ref": "1. Pick the primary reference",
    "wiz.canvas": "2. Canvas",
    "wiz.width": "Width",
    "wiz.height-lock": "Height locked to 24 (guide L1 viability floor)",
    "wiz.skeleton": "Skeleton archetype",
    "wiz.seed": "3. Palette seed",
    "wiz.quantizing": "Quantizing from reference icon...",
    "wiz.seed-hint":
      "A starting hint only; the human decides. Click a swatch to set the base color, click again to remove",
    "wiz.go": "Start tracing",
    "wiz.cancel": "Cancel",
    "wiz.done": "Wizard done; height locked to 24, start tracing",

    "ctx.brush": "Brush",
    "ctx.contiguous": "Contiguous",
    "ctx.connectivity": "Connectivity",
    "ctx.line-hint": "Shift constrains H/V/45°",
    "ctx.filled": "Filled",
    "ctx.hollow": "Hollow",
    "ctx.rect-toggle": "(press U to toggle)",
    "ctx.marquee-hint": "Arrow keys nudge · Esc cancels",
    "ctx.move-hint": "Drag to move; no selection moves the whole image",
    "ctx.picker-hint": "Click canvas to pick a char; Alt-click the reference to pick a color",

    "pick.picked": "Picked {ch} (rgb {rgb})",
    "pick.add-confirm": "Color rgb({rgb}) is not in the palette. Add it?",
    "pick.added": "Added to palette {ch} (rgb {rgb})",

    "flip.h-confirm":
      "Horizontal flip breaks the facing-left convention (guide 5.1); every existing sprite faces left. Continue?",

    "save.materialize-confirm":
      "Saving materializes {slug} into a standalone config (currently derived from {parent}); family fixes to the parent will no longer apply automatically. Continue?",
    "save.l11-fail": "L11 check failed: parent base char missing from the palette",
    "save.saving": "Saving...",
    "save.written": "Wrote {file}\nSuggested commit: {commit}",
    "save.unchanged": "No change to the view; nothing written",

    "status.unsaved": "unsaved",
    "status.saved": "saved",
    "status.offline": "offline (saving will download a dump)",
    "status.new": "new sprite",

    "tool.pencil": "Pencil",
    "tool.eraser": "Eraser",
    "tool.bucket": "Fill",
    "tool.line": "Line",
    "tool.rect": "Rect",
    "tool.marquee": "Select",
    "tool.move": "Move",
    "tool.picker": "Pick",
    "hint.pencil": "B Pencil",
    "hint.eraser": "E Eraser",
    "hint.bucket": "G Fill",
    "hint.line": "L Line",
    "hint.rect": "U Rect (press U again to toggle filled)",
    "hint.marquee": "M Rect select",
    "hint.move": "V Move selection",
    "hint.picker": "I / Alt Pick",

    "gallery.title": "pixelart gallery",
    "gallery.search-ph": "Search slug / English / Chinese / Japanese name",
    "gallery.all": "All",
    "gallery.done": "Done",
    "gallery.todo": "To do",
    "gallery.undrawn": "not drawn",

    "pal.add-title": "Add color",
    "pal.over-hint": "Over 8 colors; guide 5.5 recommends 5-8",
    "pal.exhausted": "Palette chars exhausted (A-Z a-z 0-9)",
    "pal.add-confirm": "Add to palette {ch} = rgb({rgb})?",

    "ref.head": "Reference icons by generation",
    "ref.side": "Side by side",
    "ref.overlay": "Overlay",
    "ref.ab": "Alternate (hold A)",
    "ref.opacity": "Ghost opacity ",
    "ref.offset": "Offset",
    "ref.hint-overlay": "The reference is layered under the canvas; trace on the canvas",
    "ref.hint-ab": "Back to canvas; hold A for the original, release for the sprite",

    "api.offline":
      "No local server; downloaded the grid JSON. Run python3 pixelart/apply_grid.py <file> to apply",
  },
  zh: {
    "menu.file": "文件",
    "menu.edit": "编辑",
    "menu.view": "视图",
    "menu.help": "帮助",
    "act.save": "保存 Ctrl+S",
    "act.grid": "下载 grid JSON",
    "act.png": "导出 PNG",
    "act.gallery": "返回画廊",
    "act.undo": "撤销 Ctrl+Z",
    "act.redo": "重做 Ctrl+Y",
    "act.flip-h": "水平翻转 (警示)",
    "act.flip-v": "垂直翻转",
    "act.clear": "清空画布",
    "act.zoom-in": "放大",
    "act.zoom-out": "缩小",
    "act.fit": "适应窗口",
    "act.grid-lines": "网格线开关",
    "act.overlay": "底稿叠放开关",
    "act.shortcuts": "快捷键",
    "shortcuts.title": "快捷键 (Aseprite 映射)",
    "shortcuts.close": "关闭",
    "sc.pencil": "铅笔 (1-4px,pixel-perfect 默认开)",
    "sc.eraser": "橡皮 (退 mask,描边自动收缩)",
    "sc.picker": "取色 (画布与参考图通用)",
    "sc.bucket": "油漆桶 (连续/全局,4/8 连通)",
    "sc.line": "直线 (Shift 约束 H/V/45°)",
    "sc.rect": "矩形 (再按 U 空心/实心切换)",
    "sc.marquee": "矩形选区 (方向键微调,Esc 取消)",
    "sc.move": "移动选区 (无选区时移动整图)",
    "sc.zoom": "缩放 (滚轮亦可)",
    "sc.pan": "平移",
    "sc.swap": "交换前景/背景色",
    "sc.rightbtn": "画背景色",
    "sc.undo": "撤销 / 重做",
    "sc.flip": "翻转 (水平翻转破坏朝左约定,有警示)",
    "sc.alternate": "交替模式:看原图 / 松开看 sprite",
    "sc.save": "保存 (写回 sprites/<slug>.py)",

    "unknown-monster": "未知怪物: {slug}",
    "badge.derived": "派生自 {parent}",
    "badge.parent": "编辑父级",
    "badge.stay": "在此查看",

    "wiz.no-skeleton": "不使用骨架",
    "wiz.title": "描摹 {name}",
    "wiz.step-ref": "1. 选择主参考",
    "wiz.canvas": "2. 画布",
    "wiz.width": "宽度",
    "wiz.height-lock": "高度锁定 24 (guide L1 可行性下限)",
    "wiz.skeleton": "骨架原型",
    "wiz.seed": "3. 调色板种子",
    "wiz.quantizing": "从参考图标量化...",
    "wiz.seed-hint":
      "仅供参考起点,最终以人为准;点击色块设为基色,再次点击移除",
    "wiz.go": "开始描摹",
    "wiz.cancel": "取消",
    "wiz.done": "向导完成;高度已锁 24,开始描摹",

    "ctx.brush": "笔刷",
    "ctx.contiguous": "连续",
    "ctx.connectivity": "连通",
    "ctx.line-hint": "Shift 约束 水平/垂直/45°",
    "ctx.filled": "实心",
    "ctx.hollow": "空心",
    "ctx.rect-toggle": "(再按 U 切换)",
    "ctx.marquee-hint": "方向键微调 · Esc 取消",
    "ctx.move-hint": "拖动移动;无选区时移动整图",
    "ctx.picker-hint": "点击画布取字符;Alt 点击参考大图取色",

    "pick.picked": "取色 {ch} (rgb {rgb})",
    "pick.add-confirm": "颜色 rgb({rgb}) 不在调色板,加入?",
    "pick.added": "已加入调色板 {ch} (rgb {rgb})",

    "flip.h-confirm":
      "水平翻转会破坏朝左约定 (guide 5.1),所有已有 sprite 都是朝左的。继续?",

    "save.materialize-confirm":
      "保存会把 {slug} 物化为独立配置 (当前派生自 {parent})," +
      "之后父级的家族修正不再自动生效。继续?",
    "save.l11-fail": "L11 校验失败: 父级 base 字符不在当前调色板",
    "save.saving": "保存中...",
    "save.written": "已写入 {file}\n建议 commit: {commit}",
    "save.unchanged": "视图无变化,未写盘",

    "status.unsaved": "未保存",
    "status.saved": "已保存",
    "status.offline": "离线 (保存将下载 dump)",
    "status.new": "新精灵",

    "tool.pencil": "铅笔",
    "tool.eraser": "橡皮",
    "tool.bucket": "油漆桶",
    "tool.line": "直线",
    "tool.rect": "矩形",
    "tool.marquee": "选区",
    "tool.move": "移动",
    "tool.picker": "取色",
    "hint.pencil": "B 铅笔",
    "hint.eraser": "E 橡皮",
    "hint.bucket": "G 油漆桶",
    "hint.line": "L 直线",
    "hint.rect": "U 矩形 (再按 U 切换实心)",
    "hint.marquee": "M 矩形选区",
    "hint.move": "V 移动选区",
    "hint.picker": "I / Alt 取色",

    "gallery.title": "pixelart 画廊",
    "gallery.search-ph": "搜索 slug / 英文 / 中文 / 日文名",
    "gallery.all": "全部",
    "gallery.done": "已完成",
    "gallery.todo": "未完成",
    "gallery.undrawn": "未绘制",

    "pal.add-title": "新增颜色",
    "pal.over-hint": "已超过 8 色;guide 5.5 建议 5-8 色",
    "pal.exhausted": "调色板字符已用尽 (A-Z a-z 0-9)",
    "pal.add-confirm": "加入调色板 {ch} = rgb({rgb})?",

    "ref.head": "各代原图",
    "ref.side": "并排",
    "ref.overlay": "叠放",
    "ref.ab": "交替 (按住 A)",
    "ref.opacity": "底稿不透明度 ",
    "ref.offset": "偏移",
    "ref.hint-overlay": "底稿已垫在画布下,回画布描摹",
    "ref.hint-ab": "回到画布,按住 A 看原图,松开看 sprite",

    "api.offline":
      "无本地服务,已下载 grid JSON;运行 python3 pixelart/apply_grid.py <文件> 落盘",
  },
  ja: {
    "menu.file": "ファイル",
    "menu.edit": "編集",
    "menu.view": "表示",
    "menu.help": "ヘルプ",
    "act.save": "保存 Ctrl+S",
    "act.grid": "grid JSON をダウンロード",
    "act.png": "PNG をエクスポート",
    "act.gallery": "ギャラリーに戻る",
    "act.undo": "元に戻す Ctrl+Z",
    "act.redo": "やり直す Ctrl+Y",
    "act.flip-h": "左右反転 (警告あり)",
    "act.flip-v": "上下反転",
    "act.clear": "キャンバスをクリア",
    "act.zoom-in": "拡大",
    "act.zoom-out": "縮小",
    "act.fit": "ウィンドウに合わせる",
    "act.grid-lines": "グリッド線の切り替え",
    "act.overlay": "下絵重ねの切り替え",
    "act.shortcuts": "ショートカット",
    "shortcuts.title": "ショートカット (Aseprite 対応)",
    "shortcuts.close": "閉じる",
    "sc.pencil": "鉛筆 (1-4px、pixel-perfect 既定オン)",
    "sc.eraser": "消しゴム (mask を消す、輪郭は自動収縮)",
    "sc.picker": "スポイト (キャンバスと参考画像の両方)",
    "sc.bucket": "塗りつぶし (連続/全体、4/8 近傍)",
    "sc.line": "直線 (Shift で水平/垂直/45° 制限)",
    "sc.rect": "矩形 (もう一度 U で塗り/枠を切替)",
    "sc.marquee": "範囲選択 (矢印キーで微調整、Esc で解除)",
    "sc.move": "選択範囲を移動 (未選択なら全体)",
    "sc.zoom": "ズーム (ホイールも可)",
    "sc.pan": "パン",
    "sc.swap": "前景色/背景色を入れ替え",
    "sc.rightbtn": "右クリックで背景色を塗る",
    "sc.undo": "元に戻す / やり直す",
    "sc.flip": "反転 (左右反転は左向き規約を壊すため警告あり)",
    "sc.alternate": "A 長押し: 原図を表示 / 離すと sprite",
    "sc.save": "保存 (sprites/<slug>.py に書き戻す)",

    "unknown-monster": "不明なモンスター: {slug}",
    "badge.derived": "{parent} から派生",
    "badge.parent": "親を編集",
    "badge.stay": "このまま表示",

    "wiz.no-skeleton": "骨格を使わない",
    "wiz.title": "{name} をトレース",
    "wiz.step-ref": "1. 主参考を選択",
    "wiz.canvas": "2. キャンバス",
    "wiz.width": "幅",
    "wiz.height-lock": "高さは 24 に固定 (guide L1 の下限)",
    "wiz.skeleton": "骨格アーキタイプ",
    "wiz.seed": "3. パレットシード",
    "wiz.quantizing": "参考アイコンから量子化中...",
    "wiz.seed-hint":
      "あくまで出発点。最終判断は人間が行います。スウォッチclickで基本色に設定、再clickで削除",
    "wiz.go": "トレース開始",
    "wiz.cancel": "キャンセル",
    "wiz.done": "ウィザード完了。高さは 24 固定、トレース開始",

    "ctx.brush": "ブラシ",
    "ctx.contiguous": "連続",
    "ctx.connectivity": "近傍",
    "ctx.line-hint": "Shift で水平/垂直/45° に制限",
    "ctx.filled": "塗り",
    "ctx.hollow": "枠",
    "ctx.rect-toggle": "(U で切替)",
    "ctx.marquee-hint": "矢印キーで微調整 · Esc で解除",
    "ctx.move-hint": "ドラッグで移動。未選択なら全体を移動",
    "ctx.picker-hint": "キャンバスをクリックで文字取得。Alt+クリックで参考画像から色取得",

    "pick.picked": "取得 {ch} (rgb {rgb})",
    "pick.add-confirm": "色 rgb({rgb}) はパレットにありません。追加しますか?",
    "pick.added": "パレットに追加 {ch} (rgb {rgb})",

    "flip.h-confirm":
      "左右反転は左向き規約 (guide 5.1) を壊します。既存 sprite はすべて左向きです。続行しますか?",

    "save.materialize-confirm":
      "保存すると {slug} は独立設定として確定します (現在は {parent} から派生)。" +
      "以後、親への家族修正は自動反映されません。続行しますか?",
    "save.l11-fail": "L11 検証失敗: 親の base 文字がパレットにありません",
    "save.saving": "保存中...",
    "save.written": "{file} に書き込みました\nsuggest commit: {commit}",
    "save.unchanged": "表示に変化なし。書き込みませんでした",

    "status.unsaved": "未保存",
    "status.saved": "保存済み",
    "status.offline": "オフライン (保存すると dump をダウンロード)",
    "status.new": "新規スプライト",

    "tool.pencil": "鉛筆",
    "tool.eraser": "消しゴム",
    "tool.bucket": "塗り",
    "tool.line": "直線",
    "tool.rect": "矩形",
    "tool.marquee": "選択",
    "tool.move": "移動",
    "tool.picker": "スポイト",
    "hint.pencil": "B 鉛筆",
    "hint.eraser": "E 消しゴム",
    "hint.bucket": "G 塗りつぶし",
    "hint.line": "L 直線",
    "hint.rect": "U 矩形 (もう一度 U で塗り切替)",
    "hint.marquee": "M 範囲選択",
    "hint.move": "V 選択を移動",
    "hint.picker": "I / Alt スポイト",

    "gallery.title": "pixelart ギャラリー",
    "gallery.search-ph": "slug / 英語 / 中文 / 日本語名で検索",
    "gallery.all": "すべて",
    "gallery.done": "完了",
    "gallery.todo": "未完了",
    "gallery.undrawn": "未描画",

    "pal.add-title": "色を追加",
    "pal.over-hint": "8 色を超えています。guide 5.5 は 5-8 色を推奨",
    "pal.exhausted": "パレットの文字を使い切りました (A-Z a-z 0-9)",
    "pal.add-confirm": "パレットに追加 {ch} = rgb({rgb})?",

    "ref.head": "世代別の原図",
    "ref.side": "並べて表示",
    "ref.overlay": "重ねる",
    "ref.ab": "交互 (A 長押し)",
    "ref.opacity": "下絵の不透明度 ",
    "ref.offset": "オフセット",
    "ref.hint-overlay": "下絵をキャンバスの下に敷きました。キャンバスでトレース",
    "ref.hint-ab": "キャンバスに戻る。A 長押しで原図、離すと sprite",

    "api.offline":
      "ローカルサーバーなし。grid JSON をダウンロードしました。python3 pixelart/apply_grid.py <file> で適用してください",
  },
};

const LANGS = ["en", "zh", "ja"];

function detect() {
  for (const tag of navigator.languages || [navigator.language || "en"]) {
    const p = tag.toLowerCase().slice(0, 2);
    if (LANGS.includes(p)) return p;
  }
  return "en";
}

let current = localStorage.getItem(STORAGE_KEY);
if (!LANGS.includes(current)) current = detect();

const listeners = [];

export function getLang() {
  return current;
}

export function setLang(lang) {
  if (!LANGS.includes(lang) || lang === current) return;
  current = lang;
  localStorage.setItem(STORAGE_KEY, lang);
  document.documentElement.lang = lang === "zh" ? "zh-CN" : lang;
  for (const cb of listeners) cb();
}

export function onLangChange(cb) {
  listeners.push(cb);
}

// t("key", {slug: "x"}); {var} tokens interpolate; missing keys fall
// through to English, then to the key itself (a bug shows as the key).
export function t(key, vars) {
  const dict = DICTS[current];
  let s = (dict && dict[key]) ?? DICTS.en[key] ?? key;
  if (vars) {
    for (const [k, v] of Object.entries(vars)) {
      s = s.replaceAll(`{${k}}`, v);
    }
  }
  return s;
}

// Fill every [data-i18n] (textContent), [data-i18n-ph] (placeholder), and
// [data-i18n-title] (title attribute).
export function applyDom(root = document) {
  document.documentElement.lang = current === "zh" ? "zh-CN" : current;
  root.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });
  root.querySelectorAll("[data-i18n-ph]").forEach((el) => {
    el.placeholder = t(el.dataset.i18nPh);
  });
  root.querySelectorAll("[data-i18n-title]").forEach((el) => {
    el.title = t(el.dataset.i18nTitle);
  });
}

export function langSelector() {
  const sel = document.createElement("select");
  sel.className = "langsel";
  sel.setAttribute("aria-label", "language");
  const names = { en: "EN", zh: "中文", ja: "日本語" };
  for (const l of LANGS) {
    const o = document.createElement("option");
    o.value = l;
    o.textContent = names[l];
    sel.append(o);
  }
  sel.value = current;
  sel.addEventListener("change", () => setLang(sel.value));
  return sel;
}
