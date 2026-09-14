# pixelart/: hand-drawn pixel sprite set

A second, opt-in icon set: natively small pixel art (height 24, width
per sprite, roughly 16-52; near-black outline, flat fills, transparent
background) drawn by hand in this repo's config format. Covers every
monster (378 configs in `sprites/`) plus the endemic life set (132 configs
in `endemic/`). Release PNGs are emitted at each sprite's native size,
never scaled or padded. Contrast with `icons/`, which holds
screenshot-derived game card icons at 48 x 48. Sprites render crisp at
terminal sizes where downscaled game icons turn muddy.

## How it works

- `spritekit.py`: engine, hand-authored silhouette spans per row, an
  auto-stroke pass (1px transparent channels between parts fill in as the
  black separation lines), then declarative flat fills.
- `sprites/<name>.py`: one config per monster: `spans` (silhouette runs),
  `fills` (recolor/put ops), `palette`. Palette-only subspecies are ~10-line
  configs importing their base.
- `endemic/<name>.py`: the endemic life set, same format; several species
  derive from shared archetype bases (`_fish.py`, `_toad.py, ...).
- `build_sprites.py`: driver,
  - no flags: dev previews + contact sheet (local only, gitignored)
  - `--out DIR`: release output; one native-size transparent PNG per sprite,
    named by slug (`rathalos.png`, `azure-rathalos.png`, ...)
  - `--check DIR`: byte-compare DIR against a fresh build
  - `--endemic`: build the `endemic/` set instead of `sprites/` (slugs
    validated against `data/endemic_life.json`)

## Web editor

A browser drawing board over the same monster configs. Aseprite-style tools
and shortcuts, every generation's original icon next to the sprite, saves
write straight back to `sprites/<name>.py` through the same build rules.

    make editor          # rebuild data bundle + serve at http://localhost:8642
    make editor-static   # self-contained bundle (editor + icons) for hosting
    make test            # round-trip + save-chain self-checks

Division of labor: grids are always computed by `spritekit` (the JS never
re-implements the engine, it renders precomputed grids from
`build_editor_data.py`), and config files are only ever written by Python
(`decompile.py` reverses the editor's mask + overrides into spans + fills,
asserting the rebuild matches cell for cell before anything is written).
Without the local server the editor still works: save degrades to
downloading a grid JSON that `apply_grid.py` applies through the identical
path. `editor/selftest.html` runs the pure JS helper assertions.

## Pipeline contract

The configs are the source of truth; `icons-pixelart/` is a deterministic
build product, gitignored like `data/` and `icons/` and built at release
time (see `.github/workflows/release.yml`). Every sprite name must be a
slug in `data/monsters.json` (`data/endemic_life.json` for the endemic
set); enforced on every build. Coverage is complete: all 378 monsters and
132 endemic life entries; zukan still falls back to `icons/` per creature
as a safety net.

## Adding a monster

1. `cp sprites/<closest-archetype>.py sprites/<slug>.py`, edit name/spans/
   fills/palette (side view facing left, near-black outline, flat fills,
   subject fully inside the frame).
2. `python3 build_sprites.py <slug>` and eyeball the preview + contact
   sheet: build, look, tweak, repeat.
3. `python3 build_sprites.py --out ../icons-pixelart` to refresh the set;
   `--endemic --out ../icons-pixelart/endemic` for the endemic set.
4. `--check` passes byte-identical rebuilds; the pixelart-check workflow
   runs the equivalent in CI.
