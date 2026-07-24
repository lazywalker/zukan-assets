# Sources — investigation notes

Notes on every source I looked at for zukan-assets: what's in it, the license,
coverage, schema, and why it made the cut (or didn't). Kept so this is all
reproducible and easy to revisit later.

## Used

### monster-hunter-DB (baseline roster + icons)
- **URL:** https://github.com/CrimsonNynja/monster-hunter-DB
- **Vendored commit:** `566883a729757a83b596b6ba9963132a9d19afca`
- **License:** MIT (code, data); assets © Capcom.
- **Contents:** `monsters.json` (337 monsters: 257 large, 80 small),
  `endemicLife.json` (133), `quests.json` (936), and `icons/` (854 PNGs).
- **Coverage:** MHFU, MH3U, MH4U, MHGU, MHW (+Iceborne), MHRise (+Sunbreak),
  MHWilds, MHST, MHST2.
- **Monster schema:** `_id.$oid`, `name`, `type`, `isLarge`, `subSpecies[]`,
  `elements[]`, `ailments[]`, `weakness[]`, `games[]` (each: `game`,
  `image`, `info`, `danger`).
- **Role:** the backbone roster + most per-game icons. Each `games[].info`
  is the in-game hunter-notes text, and it's the only place we get cross-game
  descriptive text (the APIs below only cover MHW and Wilds).
- **Known issues:** 7 icon-reference typos (e.g. `MHSWilds-` → `MHWilds-`,
  missing `.png`), patched in `tools/common.py::ICON_TYPO_FIXES`.

### mhw-db.com (MHW + Iceborne numeric data + items)
- **URL:** https://mhw-db.com
- **License:** open JSON API.
- **Endpoints:** `GET /monsters`, `GET /items`.
- **Monster schema (verified, e.g. Anjanath):**
  `id`, `type`, `species`, `elements[]`, `name`, `description`, `ailments[]`
  (each with `recovery`/`protection` substructures), `locations[]`,
  `resistances[]` (element + condition), `weaknesses[]` (element + stars +
  condition), `rewards[]` (item object with rarity/value/name/description +
  conditions[] with type=carve/wound/reward, rank, quantity, chance, subtype).
- **Item schema:** `id`, `name`, `description`, `rarity`, `value`, `carryLimit`.
- **Counts:** 58 monsters, 1186 items (as of fetch).
- **Role:** the main source of structured numeric data for MHW/Iceborne —
  weaknesses (with star ratings), resistances (with conditions), the full
  ailment mechanics, reward tables, and the item database. Merged by monster
  name.

### wilds.mhdb.io (Monster Hunter Wilds numeric data + items)
- **URL:** https://wilds.mhdb.io
- **License:** open JSON API.
- **Endpoints:** `GET /en/monsters`, `GET /en/items`.
- **Monster schema (verified, e.g. Nu Udra):**
  `name`, `description`, `kind`, `species`, `size` (base/mini/silver/gold),
  `elements[]`, `weaknesses[]` (element/status + level + condition + kind),
  `resistances[]` (element/effect + condition + kind), `ailments[]`,
  `locations[]`, `parts[]`, `rewards[]`, `tips[]`, `features`.
- **Item schema:** as mhw-db plus `icon` (id/kind/color) and `recipes[]`
  (output + inputs).
- **Counts:** 34 monsters, 773 items (as of fetch).
- **Role:** structured data for the Wilds roster (Nu Udra, Arkveld, Zoh Shia,
  and the rest), which mhw-db doesn't cover.

### GatheringHallStudios MHGenDatabase (MHGU numeric data)
- **URL:** https://github.com/gatheringhallstudios/MHGenDatabase
- **Vendored commit:** `6ec3ce73f4f4def80f04413094fa0fc033787ee2`
- **License:** © Capcom (data); no explicit OSS license file in the repo.
- **Contents:** a compiled SQLite db (`mhgu.db`, 39 tables) from the MHGU
  Database Android app. The monster tables are extracted by
  `tools/extract_mhgu.py` into `source/api_cache/mhgu_monsters.json`.
- **Monster tables extracted:**
  `monsters` (129: name, class, base_hp), `monster_weakness` (element ratings
  0-6 for fire/water/thunder/ice/dragon/poison/paralysis/sleep + trap/item
  effectiveness), `monster_damage` (hitzones per body part: cut/impact/shot/
  elements/ko), `monster_status` (poison/sleep/paralysis buildup thresholds:
  initial/increase/max/duration/damage), `monster_ailment` (roar/wind/tremor),
  `monster_habitat` (location + start/move/rest areas).
- **Counts:** 129 monsters (covers returning MHFU/MH3U/MH4U roster).
- **Role:** fills the numeric-data gap for the older games no JSON API
  covers. Once merged, numeric coverage jumps from 27% (92 monsters, MHW +
  Wilds only) to 57% (191 monsters). Brings hitzones, status thresholds, HP,
  and trap effectiveness, fields the two APIs don't have. Merged by monster
  name (same join as mhw-db/wilds).

### Monster Hunter Fandom wiki (cross-game gap-fill)
- **URL:** https://monsterhunter.fandom.com/wiki/Category:Monster_Icons
- **License:** CC BY-SA; icons © Capcom.
- **Contents:** the `Category:Monster_Icons` tree has 16 game-specific
  subcategories (MHFU, MH3U, MH4U, MHXX, MHGen, MHW, MHWI, MHRise, plus MH3,
  MH3G, MH4, MHP3, MHO, MHFG, MHR, and an SVG set) plus ~240 files at the top
  level (mostly Frontier). Total icons fetched into the hundreds.
- **API:** MediaWiki `action=query&list=categorymembers` (subcat + file,
  paginated) then `prop=imageinfo&iiprop=url` to resolve original media URLs.
  Crawled with a 1s delay and a browser User-Agent.
- **Role:** fallback for the icon gaps the other sources miss. **Raw files
  are gitignored**; slug-renamed copies get committed per game.
- **Actual usage:** of the ~1053 committed files, only 3 end up in the build
  (remobra, shagaru-magala, vespoid) — monster-hunter-DB's coverage is high
  enough that the Fandom fallback almost never triggers. The rest sit unused
  but are worth keeping: Fandom icons are a viable fallback for *any* future
  MHDB gap, not just these three. Both transparent and opaque (RGB) Fandom
  icons work — `fill_background.py` flood-fills the transparent ones into a
  square card and leaves the opaque ones as-is (they're already full cards),
  so transparency is not a discriminator between the two sources. MHDB wins
  on coverage and stylistic consistency, not on background handling.

## Investigated but not used

### MHWorldData (MHW reference — vendored early, later removed)
- **URL:** https://github.com/gatheringhallstudios/MHWorldData
- **Vendored commit (at time of removal):** `be7362213d7d1e30b794e3b58d3f87712035658d`
- **License:** MIT (code), © Capcom (data/images).
- **Contents:** Python tool + curated CSVs + 87 monster icons (512×512).
- **Excluded because:** monster-hunter-DB already
  covers all the MHW icons, and the detailed hitzone CSVs never got merged (the
  MHGU db does hitzones now, with a wider roster). Dropped it to save 19MB of
  dead weight.

### CAPCOM official MHST2 Monstie Icons
- **URL:** https://www.monsterhunter.com/mha/en/st2_monstericon_dl/
- **License statement (verbatim from page):** "We've prepared icons for all 91
  Monsties that appear in Monster Hunter Stories 2: Wings of Ruin, free to
  download and use!" with the caveat "**do not edit, repost, or redistribute
  these images**."
- **Contents:** 91 official icons, each a monster painted on a textured gold
  circular badge with a "MONSTER HUNTER STORIES 2" rim.
- **Excluded because:** the gold badge just won't come off cleanly with
  automated background removal. Tried three things and they all left
  unacceptable residue on the warmest-colored monsters (Anjanath etc.):
  1. per-pixel median badge reconstruction + deviation masking → 37% gold
     residue (the badge has internal gradients the median can't track per-icon);
  2. + chroma-key gold suppression → 16% residue (the gold bleeds into the
     warm monster parts);
  3. rembg (U²-Net semantic segmentation) → 59% residue (the model treats
     badge+monster as one blob; it's trained on photographic foregrounds).
  The cleaned monster-hunter-DB MHST2 icons (dark frame stripped by a darkness
  threshold, see `clean_mhst2.py`) are transparent and clean, so we use those
  instead.

### The Spriters Resource (MHXX/MHGU sprite sheets)
- **URLs:**
  - https://www.spriters-resource.com/3ds/monsterhunterxx/asset/112754/ (MHXX monster icons)
  - https://www.spriters-resource.com/3ds/monsterhunterxx/ (game index)
- **License:** community rip; site terms permit personal-project use, not
  redistribution.
- **Excluded because:** the "Monster Icons" asset is an **overlapping
  honeycomb-style collage poster**, not a grid sprite sheet. Looked at the
  downloaded 266×783 PNG: **zero** fully-transparent rows or columns (the
  icons overlap edge to edge), and 48% of pixels are semi-transparent
  (anti-aliased overlap). You can't split it into individual icons by any
  transparent-gutter method. On top of that the site returns HTTP 403 for any
  scripted access (curl/requests), even from residential IPs. And mhgu is
  already fully covered by the monster-hunter-DB baseline, whose MHGU icons are
  clean transparent pixel art (verified — e.g. Ahtal-Ka 62×62, transparent
  background).

### MHW_Icons_SVG
- **URL:** https://github.com/OthelloRhin/MHW_Icons_SVG (`242f7e8`)
- **License:** MIT.
- **Contents:** 353 SVG files covering crowns, decorations (ranks 1–4), 14
  weapon types (ranks 1–12), hunter armor, mantles/boosters, and traps.
- **Excluded because:** it contains **no monster icons at all** — only
  gameplay/UI/equipment icons. Checked the whole directory.

### monsterbuddy-assets
- **URL:** https://github.com/te1/monsterbuddy-assets
- **Contents:** assets for the Monster Buddy MHST2 companion app, including
  cropped monster images.
- **Excluded because:** its MHST2 icons are superseded by the official CAPCOM
  set, which is better quality and explicitly licensed.

### Pidgi.net
- **URL:** https://pidgi.net/wiki/Category:Monster_Hunter_series_creatures
- **Contents:** 128 creature subcategories.
- **Excluded because:** the metadata is sparse and it overlaps the Fandom wiki,
  which is easier to crawl via its MediaWiki API.

### Reddit fan-made MHRise Vector HD icons
- **URL:** https://www.reddit.com/r/MonsterHunter/comments/x87g08/
- **Contents:** every MHRise large-monster icon remade as vector HD art.
- **Excluded because:** the goal is pixel-style icons for terminal half-block
  rendering; HD vector art doesn't really fit that use case.

### Monster Hunter Diary: Poka Poka Airou Village
- **URL:** https://en.wikipedia.org/wiki/Monster_Hunter_Diary
- **Contents:** a Felyne-centric spin-off. Suggested as a pixel-art source.
- **Excluded because:** the protagonists are Felynes, not monsters, and there's
  no systematic monster sprite rip — just scattered cat-PNG clipart. Not really
  usable as a monster-icon source.

## Accessibility notes for the fetch step

Network reachability from CI/datacenter IPs varies by host:

| Host | Reachable from datacenter? | Notes |
|---|---|---|
| mhw-db.com | yes | plain JSON |
| wilds.mhdb.io | yes | plain JSON |
| monsterhunter.fandom.com (API) | yes | needs a browser User-Agent |

`fetch_external.py` hits each source on its own, so one getting blocked
doesn't kill the rest. The GitHub Actions runner usually reaches all of them.

## Item / equipment icons

A separate investigation into whether the "zukan" (bestiary) could cover items
and gear beyond monsters. Findings, kept for the next time this comes up:

### Item-type icons — USED (5th gen only)

MH item icons are **generic per type**, not per item: every Scale shares one
illustration, every Hide another, colored by rarity. The Fandom wiki hosts a
clean SVG set under `Category:5th_Generation_Item_Icons` (~3021 SVGs covering
MHW + Wilds, each `5thGen Item Icon-{Type} {Color}.svg`). `fetch_item_icons.py`
pulls these, renders to PNG via resvg-py, and writes `source/item-icons/`.

These SVGs are **community-drawn generic art, not CAPCOM assets**, so they're
vendored into the repo directly (both `.svg` source and rendered `.png`),
unlike the CAPCOM monster icons which stay gitignored. Change detection uses
the Fandom CDN's ETag: each re-run sends `If-None-Match` per icon, so an
unchanged SVG returns 304 with no body and costs no bandwidth — periodic
re-fetches stay cheap and polite to the wiki.

Coverage of the 1791 items in `items.json`: ~93%. Wilds items carry their real
`{kind, color}` straight from the API (`wilds_icon` field); MHW items (no such
field) get an inferred kind from naming rules in `item_kind.py` (~91% hit)
then mapped onto the Fandom icon vocabulary via `KIND_ALIASES` in build.py.
The ~7% unmapped are one-off named items (Bluegleam, Commendation...) where
guessing is worse than no icon.

### Equipment (weapons/armor) — NOT viable

- **mhw-db** ships weapon/armor icons on its CDN (`assets.mhw-db.com`,
  reachable, 128px PNG) — but only ~41% of armor and only for MHW.
- **No source for MHGU or Wilds gear icons.** monsterhunterwiki.org has them
  but sits behind Cloudflare (403 on datacenter IPs, like Spriters/CAPCOM).
- Gear icons are per-piece art (not generic), so the type-icon trick doesn't
  apply; counts are huge (MHW alone: 1299 weapons + 1677 armor).
- Decision: gear stays out of zukan. The name means *monster bestiary*; gear
  would need its own project with its own icon sourcing.

### Older-generation item icons — NOT viable

The Fandom type-icon set is 5th-gen only (`Category:4th/3rd/2nd/1st_Generation_Item_Icons`
all empty). MHGU/MH4U/MH3U items have no equivalent clean source, so they stay
icon-less in `items.json` (data only). MHGU's own db (`mhgu.db`) has the item
*data* (21k rows in `items`) but no icons.
