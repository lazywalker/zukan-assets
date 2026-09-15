#!/usr/bin/env python3
"""Grid-level round trip between sprite configs and the web editor.

The editor edits two primitives: mask (the authored silhouette, the same
thing spans encode) and explicit (sparse cell -> palette char overrides).
This module is the only place that converts between those primitives and
CONFIG dicts / source text:

    editor_state(cfg)   config -> {mask, explicit} for the data bundle
    synthesize(...)     mask + explicit -> view grid; the JS editor mirrors
                        these rules exactly (editor/js/state.js)
    decompile(payload)  mask + explicit -> (CONFIG dict, source text)

Final pixels are not the config: the stroke pass grows a K ring outside the
silhouette and fills can paint over it, so a grid cannot be written back as
spans directly (a naive rewrite re-expands the outline). Decompile rebuilds
fills from the view instead, and every result is fed back through
spritekit.build_grid and compared cell by cell before the caller may write
anything; a mismatch raises. That assert is what lets the JS editor stay a
thin view over the Python engine.

Mask rows travel as hex strings: the row integer is sum(bit << (w-1-c)), so
column 0 is the most significant bit of the first nibble.
"""

import spritekit as sk


class DecompileError(Exception):
    """Payload cannot be turned into a valid config."""


def pack_row(bits, w):
    n = 0
    for c, b in enumerate(bits):
        if b:
            n |= 1 << (w - 1 - c)
    return f"{n:0{(w + 3) // 4}x}"


def unpack_rows(hex_rows, w, h):
    if len(hex_rows) != h:
        raise DecompileError(f"mask has {len(hex_rows)} rows, size says {h}")
    rows = []
    for r, hx in enumerate(hex_rows):
        try:
            n = int(hx, 16)
        except ValueError:
            raise DecompileError(f"mask row {r} is not hex: {hx!r}") from None
        if n >> w:
            raise DecompileError(f"mask row {r} wider than {w} columns: {hx!r}")
        rows.append([bool((n >> (w - 1 - c)) & 1) for c in range(w)])
    return rows


def touches_mask(mask, r, c):
    h, w = len(mask), len(mask[0])
    return any(
        0 <= r + dr < h and 0 <= c + dc < w and mask[r + dr][c + dc]
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
    )


def synthesize(mask, explicit, w, h, base):
    """View grid from editor state; mirrors editor/js/state.js.

    Mask cells show their explicit char or base. Transparent cells touching
    the mask show K (the stroke ring) unless explicitly overridden. Every
    other cell is transparent regardless of stale explicit entries.
    """
    rows = []
    for r in range(h):
        row = []
        for c in range(w):
            if mask[r][c]:
                ch = base
            elif touches_mask(mask, r, c):
                ch = "K"
            else:
                ch = "."
            e = explicit.get((r, c))
            if ch != "." and e:
                ch = e
            row.append(ch)
        rows.append("".join(row))
    return rows


def editor_state(cfg):
    """Config -> editor state {mask, explicit} for the data bundle."""
    w, h = cfg["size"]
    mask = [[cell == "#" for cell in row] for row in sk._mask(cfg)]
    grid = sk.build_grid(cfg)
    base = cfg["base"]
    explicit = {}
    for r in range(h):
        for c in range(w):
            ch = grid[r][c]
            if mask[r][c]:
                if ch != base:
                    explicit[f"{r},{c}"] = ch
            elif ch not in (".", "K"):
                explicit[f"{r},{c}"] = ch
    return {"mask": [pack_row(row, w) for row in mask], "explicit": explicit}


def spans_from_mask(mask):
    spans = {}
    for r, row in enumerate(mask):
        runs = []
        c = 0
        while c < len(row):
            if row[c]:
                a = c
                while c < len(row) and row[c]:
                    c += 1
                runs.append((a, c - 1))
            else:
                c += 1
        if runs:
            spans[r] = runs
    return spans


def fills_from_view(view, mask, base):
    """View grid -> fill ops.

    Same-char runs are split at mask boundaries: a K run crossing from the
    stroke ring into in-mask K detail must not be treated as one stroke
    segment, or the in-mask half is silently dropped (rathalos brow).
    """
    runs = {}
    puts = []
    h, w = len(view), len(view[0])
    for r in range(h):
        c = 0
        while c < w:
            ch = view[r][c]
            inside = mask[r][c]
            a = c
            while c < w and view[r][c] == ch and mask[r][c] == inside:
                c += 1
            if ch == ".":
                continue
            if inside:
                if ch != base:
                    runs.setdefault(ch, []).append((r, a, c - 1))
            elif ch != "K":
                puts.append((r, a, view[r][a:c]))
    return [("runs", cells, ch) for ch, cells in runs.items()] + [
        ("put", r, a, chars) for r, a, chars in puts
    ]


def parse_explicit(raw, w, h):
    explicit = {}
    for key, ch in raw.items():
        try:
            r, c = (int(x) for x in key.split(","))
        except ValueError:
            raise DecompileError(f"bad explicit key {key!r}") from None
        if not (0 <= r < h and 0 <= c < w):
            raise DecompileError(f"explicit out of bounds: {key}")
        if not isinstance(ch, str) or len(ch) != 1:
            raise DecompileError(f"bad explicit char for {key}: {ch!r}")
        if ch == ".":
            raise DecompileError(f"explicit '.' at {key}; erase removes mask cells")
        explicit[(r, c)] = ch
    return explicit


def decompile(payload):
    """Editor payload -> (CONFIG dict, source text).

    Raises DecompileError on anything that would not rebuild identically.
    """
    w, h = payload["size"]
    base = payload["base"]
    palette = {ch: tuple(rgba) for ch, rgba in payload["palette"].items()}
    if base not in palette:
        raise DecompileError(f"base char {base!r} not in palette")
    palette.setdefault(".", (0, 0, 0, 0))
    mask = unpack_rows(payload["mask"], w, h)
    explicit = parse_explicit(payload["explicit"], w, h)

    # drop entries the view rules ignore (cells that stopped touching the
    # mask after an erase), so client/server view comparisons stay clean
    explicit = {
        (r, c): ch
        for (r, c), ch in explicit.items()
        if mask[r][c] or touches_mask(mask, r, c)
    }

    view = synthesize(mask, explicit, w, h, base)
    used = {ch for row in view for ch in row} - {"."}
    missing = used - set(palette)
    if missing:
        raise DecompileError(f"chars missing from palette: {sorted(missing)}")

    if payload.get("view") is not None and list(payload["view"]) != view:
        for r, (ours, theirs) in enumerate(zip(view, payload["view"])):
            if ours != theirs:
                raise DecompileError(
                    f"client view drift at row {r}: sent {theirs!r}, rules say {ours!r}"
                )

    cfg = {
        "name": payload["slug"],
        "size": (w, h),
        "compare_to": payload.get("compare_to") or "",
        "palette": palette,
        "base": base,
        "spans": spans_from_mask(mask),
    }
    fills = fills_from_view(view, mask, base)
    if fills:
        cfg["fills"] = fills

    rebuilt = sk.build_grid(cfg)
    if rebuilt != [list(row) for row in view]:
        raise DecompileError(f"{cfg['name']}: round-trip mismatch, refusing to write")
    return cfg, source_text(cfg, payload.get("docstring") or "")


def _wrap_list(items, close, cont_pad):
    """`[items]` + close over one or more lines, breaking near col 74.

    items are tuples rendered "(a, b)", or plain strings. Returns physical
    lines; the caller indents the first one.
    """
    pieces = []
    for item in items:
        if isinstance(item, tuple):
            pieces.append("(" + ", ".join(str(x) for x in item) + ")")
        else:
            pieces.append(item)
    lines = []
    cur = ""
    for piece in pieces:
        nxt = f"{cur}, {piece}" if cur else piece
        if cur and len(cont_pad) + len(nxt) + len(close) > 76:
            lines.append(cur + ",")
            cur = piece
        else:
            cur = nxt
    lines.append(cur + close)
    return lines


def _q(s):
    return f'"{s}"'


def source_text(cfg, docstring=""):
    out = []
    if docstring.strip():
        out.append(f'"""{docstring.strip()}"""')
        out.append("")
    w, h = cfg["size"]
    out.append("CONFIG = {")
    out.append(f'    "name": {_q(cfg["name"])},')
    out.append(f'    "size": ({w}, {h}),')
    if cfg.get("compare_to"):
        out.append(f'    "compare_to": {_q(cfg["compare_to"])},')
    out.append('    "palette": {')
    for ch, (r, g, b, a) in cfg["palette"].items():
        out.append(f"        {_q(ch)}: ({r}, {g}, {b}, {a}),")
    out.append("    },")
    out.append(f'    "base": {_q(cfg["base"])},')
    out.append('    "spans": {')
    rows = sorted(cfg["spans"])
    kw = len(str(rows[-1])) if rows else 1
    for r in rows:
        lines = _wrap_list(cfg["spans"][r], "],", "")
        out.append(f"        {str(r).rjust(kw)}: [{lines[0]}")
        for cont in lines[1:]:
            out.append(f"        {' ' * (kw + 3)}{cont}")
    out.append("    },")
    if cfg.get("fills"):
        out.append('    "fills": [')
        for op in cfg["fills"]:
            if op[0] == "runs":
                lines = _wrap_list(op[1], f'], "{op[2]}"),', "")
                out.append(f'        ("runs", [{lines[0]}')
                for cont in lines[1:]:
                    out.append(f"                  {cont}")
            else:
                out.append(f'        ("put", {op[1]}, {op[2]}, "{op[3]}"),')
        out.append("    ],")
    out.append("}")
    return "\n".join(out) + "\n"
