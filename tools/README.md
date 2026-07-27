# tools/: ETL pipeline

Turns vendored + fetched sources into `data/` and `icons/`.

## Pipeline

```
fetch_external.py → fetch_item_icons.py → extract_mhgu.py → extract_mh4u.py → clean_mhst2.py → split_sprites.py → build.py → normalize.py → clean_halo.py → clean_background.py → validate.py / audit.py
   (network)         (item type icons)    (mhgu db→json)   (mh4u db→json)   (mhst2 frame)    (fandom raw)      (join)   (48px/32c/enh)  (strip halo)  (zero RGB@α0)        (reports)
```

The default style keeps icons **transparent** (no background fill). For the
optional filled-square-card variant, insert `fill_background.py` between
`build.py` and `normalize.py`; see [Background styles](#background-styles).

| Script | Purpose | Reads | Writes |
|---|---|---|---|
| `fetch_external.py` | fetch APIs + Fandom monster icons | network | `source/api_cache/`, gitignored `source/fandom-raw/` |
| `fetch_item_icons.py` | fetch generic item-type icons (Scale/Hide/Potion...) from Fandom SVGs | network | `source/item-icons/` (SVGs + manifest), gitignored `source/fandom-raw/item-icons/` |
| `extract_mhgu.py` | extract MHGU SQLite db → JSON | `source/MHGenDatabase/mhgu.db` | `source/api_cache/mhgu_monsters.json` |
| `extract_mh4u.py` | extract MH4U SQLite db → JSON | `source/MH4UDatabase/mh4u.db` | `source/api_cache/mh4u_monsters.json` |
| `clean_mhst2.py` | remove dark frame from MHDB MHST2 icons | `source/monster-hunter-DB/icons/MHST2-*` | `source/mhst2-cleaned/` |
| `split_sprites.py` | slug-rename Fandom raw icons by game | `source/fandom-raw` manifest | `source/fandom-processed/` |
| `build.py` | join baseline roster + icons + numeric data + item-type icons | `source/` | `data/`, `icons/` |
| `normalize.py` | resize to 48px square, enhance contrast/sharpness, quantize to 32 colors | `icons/` | `icons/` (in place) |
| `clean_halo.py` | strip the feathered white edge (flood-fill from border through semi-transparent near-white px) | `icons/` | `icons/` (in place) |
| `clean_background.py` | zero RGB on alpha=0 pixels (clear residue from quantize) | `icons/` | `icons/` (in place) |
| `validate.py` | integrity + coverage report (every icon resolves, no orphans) | `data/`, `icons/` | stdout |
| `audit.py` | completeness: counts vs official + API cross-check + transparency residue | `data/`, `tools/official_counts.json`, `source/api_cache/`, `icons/` | stdout |
| `common.py` | shared slug/icon-ref helpers | (none) | (none) |
| `item_kind.py` | infer an item's generic icon type from its name (for MHW items w/o kind field) | (none) | (none) |
| `generate_i18n.py` | generate/update localized translations (ja/zh) from wilds API or AI; not part of CI | network (optional) | `source/i18n/*.json` |

Optional (off by default):

| Script | Purpose | Reads | Writes |
|---|---|---|---|
| `fill_background.py` | **style 2**: flood-fill the keyed-out bg ring into a full square card | `icons/` | `icons/` (in place) |

## Icon spec

Every output icon gets normalized to one spec (set in `normalize.py`):

- **48×48 square**, transparent background (the subject floats on the
  terminal's own bg). For the filled-card variant see
  [Background styles](#background-styles).
- **32-color palette**, quantized with no dithering (keeps the flat pixel-art
  regions flat).
- **Contrast enhanced** (sharpen + contrast×1.3 + saturation×1.4) before
  quantizing, to claw back the detail the downscaling eats.
- 48px is just what we store. zukan shrinks it at runtime (NEAREST) to 32 for
  detailed viewing or 24 for compact bash-startup art; one downscale from 48
  loses almost nothing, so a single stored size covers both.

Bundle: ~3.9MB for 873 monster icons + ~3.1MB for 1664 item icons (~7.0MB total).

## Background styles

There are two supported looks; **transparent is the default**.

- **Style 1, transparent (default).** Icons keep their alpha channel. The
  monster floats on whatever color the terminal/background is. This is what
  the pipeline above produces, and what CI publishes.

- **Style 2, filled square card.** Flood-fill each icon's keyed-out
  background ring into a full opaque square, recreating the in-game
  hunter's-notebook card. Use it when you want every icon to fill its cell
  with its original card color (MHFU green, MH4U gold, Rise near-white, …).

To build style 2 locally, insert one step between `build.py` and
`normalize.py`:

```bash
python3 build.py
python3 fill_background.py    # style 2 only: fill bg ring → full square card
python3 normalize.py          # 48px square + contrast enhance + 32 colors
python3 clean_background.py   # zero RGB on transparent pixels
```

CI publishes style 1 (transparent). To publish style 2 instead, add the
`fill_background.py` step back into
`.github/actions/run-pipeline/action.yml`.

## Local rebuild

Run from the `tools/` directory (commands use relative paths):

```bash
pip install -r requirements.txt
python3 fetch_external.py      # --only {api,fandom} to limit
python3 fetch_item_icons.py    # item-type icons (Scale/Hide/Potion...) from Fandom SVGs
python3 extract_mhgu.py        # extract MHGU db → JSON
python3 extract_mh4u.py        # extract MH4U db → JSON
python3 clean_mhst2.py         # clean MHDB MHST2 dark frames
python3 split_sprites.py       # slug-rename Fandom raw
python3 build.py
python3 normalize.py           # 48px square + contrast enhance + 32 colors (transparent bg)
python3 clean_halo.py          # strip feathered white edge (Rise/Sunbreak)
python3 clean_background.py    # zero RGB on transparent pixels
python3 validate.py            # internal consistency
python3 audit.py               # completeness vs official counts + APIs + residue
```

The default build keeps icons transparent. For the filled-card look (**style 2**),
run `python3 fill_background.py` between `build.py` and `normalize.py`; see
[Background styles](#background-styles).

`normalize.py` resizes to 48px, bumps contrast/sharpness/saturation to make up
for the downscaling, and quantizes to 32 colors.

`clean_background.py` clears leftover bg color from the RGB channels of
fully-transparent pixels: monster-hunter-DB's source icons for a few games
(MHFU green, MHGU blue, MH4U gold, Rise/Sunbreak near-white) keyed the
background to alpha 0 but never cleared its color, which `audit.py` flags as
residue.

`validate.py` just checks the build hangs together (every icon ref resolves, no
orphan files). `audit.py` asks a different question: is the database actually
*complete*? It lines up monster-hunter-DB's per-game large-monster count
against the franchise's recognized totals (`tools/official_counts.json`) and
cross-checks the MHW/Wilds rosters against the JSON APIs. If a game falls more
than `SHRINK_TOLERANCE` short of official, it exits non-zero and catches
regressions when monster-hunter-DB gets re-vendored.

Each source in `fetch_external.py` runs on its own, so one getting blocked
doesn't stop the rest; the build just goes ahead with whatever got fetched.

## CI

Two workflows in `.github/workflows/`:
- `check-upstream.yml`, weekly: re-fetches upstream sources, opens a PR if
  anything changed (detected via diff in source/ intermediates).
- `release.yml`, triggers when a PR merges to master: runs the full pipeline
  and publishes `data/` + `icons/` as a tar.gz Release artifact for zukan.

Both share `.github/actions/run-pipeline/action.yml` (composite action) for the
pipeline steps. Manual dispatch is available for both.

## Icon priority chain (build.py)

For each (monster, game) the build grabs the first icon it can find:

1. cleaned MHDB MHST2 icons (mhst2 only), dark frame removed
2. vendored official MH4U bestiary icons (mh4u only), a strict superset of
   MHDB's mh4u set: it also covers Seregios, Shah Dalamadur, and every Apex
   variant. For the overlap the art is the same source as MHDB, so picking
   ours first only fills gaps.
3. Fandom, same game, **mhrise only**: MHDB's Rise icons are a monochrome
   ink style that doesn't render as character art, so Fandom's colored art is
   preferred where available (Fandom's mhrise set is partial, so MHDB still
   fills the gaps; see #4). Fandom slugs carry a `-NNN` wiki sequence suffix
   that's stripped to match (`rathalos-001` → `rathalos`); when multiple
   variants exist, `-001` is the canonical pick.
4. monster-hunter-DB baseline (its own game references)
5. Fandom, same game. **mho (Monster Hunter Online) is Fandom-only**: MHDB
   carries no MHO monsters and ships no `MHO-` icons, so every MHO icon comes
   from `source/fandom-processed/mho/`.
6. Fandom, any game (cross-matched by slug)

Each output's `games[].icon_source` records which one got used.

## Roster supplement (build.py)

monster-hunter-DB is the baseline roster, but it omits some monsters other
sources cover. `build_monsters` fills those gaps in two ways:

- **MH4U**: six MH4U bosses (the Apex variants it doesn't list under other
  games) get a synthesized entry with one mh4u game, drawn from the MH4U db
  (icon from the vendored bestiary set, numeric data from the same db).
  Small/Minion monsters are skipped so the roster doesn't gain unremarkable
  fauna MHDB chose not to carry.
- **MHO**: Monster Hunter Online isn't in MHDB at all. Its 78 monsters (the
  Fandom set, with `-NN` variant suffixes collapsed) split into 42 shared
  with other games and 36 MHO-exclusive. Shared monsters get an MHO game
  entry attached to their existing record in `_build_monster_record`;
  exclusives get a synthesized record from `_mho_supplement`. MHO has no
  numeric data source, so its records carry icons only.

The summary prints how many of each were added each run.

## Idempotency

`clean_mhst2.py`, `split_sprites.py`, and `build.py` wipe their output dirs
before writing, so re-running gives identical results. `build.py` writes JSON
with sorted records for clean diffs.
