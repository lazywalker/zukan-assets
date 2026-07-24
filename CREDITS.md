# Credits

> **© CAPCOM.** All Monster Hunter icons, sprites, descriptions, and game data
> in this repository are property of CAPCOM, used for non-commercial fan
> purposes. Raw source files are **not redistributed** (gitignored); only
> processed outputs and scripts are committed. Full legal notice:
> [LICENSE](LICENSE). Rights holders: open an issue for prompt removal.

## Sources used

### Icons

| Source | URL | Role | Terms |
|---|---|---|---|
| monster-hunter-DB | https://github.com/CrimsonNynja/monster-hunter-DB | the backbone roster + most per-game icons (854 PNGs, 9 titles) | MIT (code, data) — © Capcom |
| Monster Hunter Fandom wiki | https://monsterhunter.fandom.com/wiki/Category:Monster_Icons | fills icon gaps across games, pulled via the MediaWiki API | CC BY-SA; raw files gitignored |

### Item-type icons

| Source | URL | Role | Terms |
|---|---|---|---|
| Monster Hunter Fandom wiki | https://monsterhunter.fandom.com/wiki/Category:5th_Generation_Item_Icons | generic per-type item illustrations (Scale/Hide/Potion...), vendored as SVG in source/item-icons/ | CC BY-SA (community art, not Capcom); see source/item-icons/README.md |

### Numeric data + items

| Source | URL | Role | Terms |
|---|---|---|---|
| mhw-db.com | https://mhw-db.com | MHW + Iceborne: descriptions, weaknesses, resistances, ailments, locations, rewards, items | open JSON API |
| wilds.mhdb.io | https://wilds.mhdb.io | Wilds: same fields, plus parts, hitzones, tips, item recipes | open JSON API |
| GatheringHallStudios MHGenDatabase | https://github.com/gatheringhallstudios/MHGenDatabase | MHGU: weakness ratings (1-6), hitzones by body part, status thresholds, base HP, trap effectiveness; covers the returning MHFU/MH3U/MH4U roster | © Capcom (data) |

## Investigated but not used

Looked at these while researching and ended up passing on them. Kept around for
reference in case we revisit. Full notes in [source/SOURCES.md](source/SOURCES.md).

| Source | URL | Reason for exclusion |
|---|---|---|
| MHWorldData | https://github.com/gatheringhallstudios/MHWorldData | Vendored early on as an MHW icon reference, but nothing in the build actually reads it. monster-hunter-DB already covers all the MHW icons, and the detailed hitzone CSVs never got merged (the MHGU db does hitzones now, with a wider roster). Dropped it to save 19MB. |
| CAPCOM official MHST2 Monstie Icons | https://www.monsterhunter.com/mha/en/st2_monstericon_dl/ | Each icon is a monster painted on a textured gold badge, and getting the badge off automatically just doesn't work reliably (the gold bleeds into the warm-colored monsters, and semantic segmentation treats badge+monster as one blob). Tried three things (median reconstruction, chroma-key, rembg) — all left residue. Using the cleaned monster-hunter-DB icons instead. |
| The Spriters Resource (MHXX) | https://www.spriters-resource.com/3ds/monsterhunterxx/ | The "Monster Icons" asset is an overlapping honeycomb collage poster, not a grid sprite sheet — zero transparent gutters, so you can't split it into individual icons. The site also 403s any scripted access (curl/requests). mhgu is already fully covered by monster-hunter-DB's clean transparent pixel icons anyway. |
| MHW_Icons_SVG | https://github.com/OthelloRhin/MHW_Icons_SVG | No monster icons at all — just gameplay/UI icons (crowns, decorations, weapons, armor). Checked the whole dir. |
| monsterbuddy-assets | https://github.com/te1/monsterbuddy-assets | MHST2 assets, but the cleaned monster-hunter-DB icons are better. |
| Pidgi.net | https://pidgi.net/wiki/Category:Monster_Hunter_series_creatures | 128 creature subcategories, but the metadata is sparse and it overlaps the Fandom wiki. |
| Reddit fan-made MHRise Vector HD icons | https://www.reddit.com/r/MonsterHunter/comments/x87g08/ | Vector/HD fan remakes, not pixel art — doesn't suit terminal half-block rendering. |
| Monster Hunter Diary: Poka Poka Airou Village | https://en.wikipedia.org/wiki/Monster_Hunter_Diary | The protagonists are Felynes, not monsters, and there's no systematic sprite rip. Not really usable as a monster-icon source. |

## License of this repository

Code and ETL scripts are MIT; the assets stay © CAPCOM. See [LICENSE](LICENSE).
