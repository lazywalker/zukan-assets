# tools/ — ETL pipeline

Turns vendored + fetched sources into `data/` and `icons/`.

## Pipeline

```
fetch_external.py → fetch_item_icons.py → extract_mhgu.py → clean_mhst2.py → split_sprites.py → build.py → fill_background.py → normalize.py → clean_background.py → validate.py / audit.py
   (network)         (item type icons)    (mhgu db→json)   (mhst2 frame)    (fandom raw)      (join)   (fill bg ring)   (48px/32c/enh)  (zero RGB@α0)        (reports)
```

| Script | Purpose | Reads | Writes |
|---|---|---|---|
| `fetch_external.py` | fetch APIs + Fandom monster icons | network | `source/api_cache/`, gitignored `source/fandom-raw/` |
| `fetch_item_icons.py` | fetch generic item-type icons (Scale/Hide/Potion...) from Fandom SVGs | network | `source/item-icons/` (SVGs + manifest), gitignored `source/fandom-raw/item-icons/` |
| `extract_mhgu.py` | extract MHGU SQLite db → JSON | `source/MHGenDatabase/mhgu.db` | `source/api_cache/mhgu_monsters.json` |
| `clean_mhst2.py` | remove dark frame from MHDB MHST2 icons | `source/monster-hunter-DB/icons/MHST2-*` | `source/mhst2-cleaned/` |
| `split_sprites.py` | slug-rename Fandom raw icons by game | `source/fandom-raw` manifest | `source/fandom-processed/` |
| `build.py` | join baseline roster + icons + numeric data + item-type icons | `source/` | `data/`, `icons/` |
| `fill_background.py` | flood-fill the keyed-out bg ring into a full square card | `icons/` | `icons/` (in place) |
| `normalize.py` | resize to 48px square, enhance contrast/sharpness, quantize to 32 colors | `icons/` | `icons/` (in place) |
| `clean_background.py` | zero RGB on alpha=0 pixels (clear residue from quantize) | `icons/` | `icons/` (in place) |
| `validate.py` | integrity + coverage report (every icon resolves, no orphans) | `data/`, `icons/` | stdout |
| `audit.py` | completeness: counts vs official + API cross-check + transparency residue | `data/`, `tools/official_counts.json`, `source/api_cache/`, `icons/` | stdout |
| `common.py` | shared slug/icon-ref helpers | — | — |
| `item_kind.py` | infer an item's generic icon type from its name (for MHW items w/o kind field) | — | — |
| `generate_i18n.py` | generate/update localized translations (ja/zh) from wilds API or AI; not part of CI | network (optional) | `source/i18n/*.json` |

## Icon spec

Every output icon gets normalized to one spec (set in `normalize.py`):

- **48×48 square**, with the partial background ring flood-filled out to a full
  card (MH icons are card-style illustrations, not isolated sprites, so the
  whole frame stays).
- **32-color palette**, quantized with no dithering (keeps the flat pixel-art
  regions flat).
- **Contrast enhanced** (sharpen + contrast×1.3 + saturation×1.4) before
  quantizing, to claw back the detail the downscaling eats.
- 48px is just what we store. zukan shrinks it at runtime (NEAREST) to 32 for
  detailed viewing or 24 for compact bash-startup art; one downscale from 48
  loses almost nothing, so a single stored size covers both.

Bundle: ~3.3MB for 731 monster icons + ~3.1MB for 1664 item icons (~6.4MB total).

## Local rebuild

Run from the `tools/` directory (commands use relative paths):

```bash
pip install -r requirements.txt
python3 fetch_external.py      # --only {api,fandom} to limit
python3 fetch_item_icons.py    # item-type icons (Scale/Hide/Potion...) from Fandom SVGs
python3 extract_mhgu.py        # extract MHGU db → JSON
python3 clean_mhst2.py         # clean MHDB MHST2 dark frames
python3 split_sprites.py       # slug-rename Fandom raw
python3 build.py
python3 fill_background.py     # fill partial bg ring → full square card
python3 normalize.py           # 48px square + contrast enhance + 32 colors
python3 clean_background.py    # zero RGB on transparent pixels
python3 validate.py            # internal consistency
python3 audit.py               # completeness vs official counts + APIs + residue
```

`fill_background.py` fills out the partial background (MHDB icons come with a
keyed-out rounded ring) into a full square card. `normalize.py` then resizes to
48px, bumps contrast/sharpness/saturation to make up for the downscaling, and
quantizes to 32 colors.

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
than `SHRINK_TOLERANCE` short of official, it exits non-zero — catches
regressions when monster-hunter-DB gets re-vendored.

Each source in `fetch_external.py` runs on its own, so one getting blocked
doesn't stop the rest; the build just goes ahead with whatever got fetched.

## CI

Two workflows in `.github/workflows/`:
- `check-upstream.yml` — weekly: re-fetches upstream sources, opens a PR if
  anything changed (detected via diff in source/ intermediates).
- `release.yml` — triggers when a PR merges to master: runs the full pipeline
  and publishes `data/` + `icons/` as a tar.gz Release artifact for zukan.

Both share `.github/actions/run-pipeline/action.yml` (composite action) for the
pipeline steps. Manual dispatch is available for both.

## Icon priority chain (build.py)

For each (monster, game) the build grabs the first icon it can find:

1. cleaned MHDB MHST2 icons (mhst2 only), dark frame removed
2. monster-hunter-DB baseline (its own game references)
3. Fandom, same game
4. Fandom, any game (cross-matched by slug)

Each output's `games[].icon_source` records which one got used.

## Idempotency

`clean_mhst2.py`, `split_sprites.py`, and `build.py` wipe their output dirs
before writing, so re-running gives identical results. `build.py` writes JSON
with sorted records for clean diffs.
