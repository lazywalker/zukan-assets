# i18n — localized names and descriptions

Translated monster/item names, descriptions, and fixed terms for Japanese (ja)
and Chinese (zh). These are committed static files — build.py overlays them via
`apply_i18n()` without touching any English fields.

## Files

| File | Contents |
|---|---|
| `monsters.json` | 337 monsters × {ja, zh} × {name, desc, source} |
| `items.json` | 1791 items × {ja, zh} × {name, desc, source} |
| `terms.json` | Fixed terms (Type, Element, Ailment, Location, field labels) × {ja, zh} |

## The `source` field

Every translation carries a `source` field that controls overwrite protection:

| Value | Meaning | `generate_i18n.py` behavior |
|---|---|---|
| `official` | From the wilds.mhdb.io `/ja/` API (34 Wilds monsters) | Skipped (preserved) |
| `manual` | Hand-edited or verified by a developer | Skipped (preserved) |
| `ai` | AI-generated, not yet verified | Can be overwritten |

## How to manually fix a translation

1. Edit the entry in `monsters.json` or `items.json` (this directory).
2. Change its `"source"` from `"ai"` to `"manual"`.
3. Commit. Future runs of `generate_i18n.py` will skip it.

## Architecture

This data is an **overlay layer** — it does not participate in the ETL
fetch/extract pipeline. `build.py` reads these files at build time and injects
an `i18n` field into `data/monsters.json` and `data/items.json`. Re-running the
ETL pipeline never overwrites translations.

To regenerate or update: see `tools/generate_i18n.py`.
