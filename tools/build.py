#!/usr/bin/env python3
"""Build data/ and icons/ from all sources.

Pipeline:
  1. Load monster-hunter-DB monsters.json as the baseline roster (337).
  2. For each (monster, game) icon reference, resolve it to a processed icon
     using the priority chain:
       cleaned MHST2 (mhst2) -> monster-hunter-DB baseline
       -> Fandom (any game) -> mark missing.
  3. Copy the chosen icon to icons/<game>/<slug>.png.
  4. Merge per-game hunter-notes text from the baseline.
  5. Merge mhw-db (MHW/Iceborne), wilds.mhdb.io (Wilds), and MHGU db
     (Generations Ultimate) numeric data: description, weaknesses,
     resistances, ailments, locations, rewards, hitzones, status, HP.
  6. Build items.json from both APIs.
  7. Build endemic_life.json from the baseline.

Outputs are deterministic; re-running produces identical bytes (sorted keys).
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from common import (  # noqa: E402
    GAME_EXPANSION_ICON,
    GAME_PREFIX,
    ICON_TYPO_FIXES,
    fix_icon_ref,
    icon_ref_to_game,
    icon_ref_to_monster_slug,
    slugify,
)
from item_kind import item_icon_kind_color  # noqa: E402

# The Wilds API's `icon.kind` and item_kind.infer_kind use one vocabulary, but
# the Fandom type-icon set uses another (set by wiki editors). Map the former
# onto the latter so resolves land on an icon that actually exists. Anything
# not listed is passed through unchanged.
KIND_ALIASES = {
    "certificate": "ticket",      # guild certs / commendations -> ticket art
    "medulla": "monster-part",    # marrow/medulla/nucleus -> generic monster part
    "gem": "monster-part",        # gems/jewels/mantles -> generic monster part
    "powder": "sac",              # dust/powder -> sac illustration
    "extract": "sac",             # fluids/extracts -> sac
    "phial": "bottle",            # phials/vials -> bottle
    "plant": "herb",              # plant matter -> herb
    "seed": "seed",
    "mushroom": "mushroom-edible",
    "fish": "fish-edible",
    "meat": "meat-edible",
    "bug": "bug-edible",
    "lens": "monster-part",       # eye/lens -> generic monster part
    "feather": "monster-part",
    "smoke": "smoke-bomb",
    "drug": "medicine",           # demondrug/dash juice -> medicine
    "pill": "pill-edible",
    "honey": "nectar",
    "voucher": "ticket",
    "ammo-special": "slinger-ammo",
    "knife": "slinger-ammo",
    "web": "spiderweb",
    "paintball": "empty-coating",
    "crystal": "crystal",
    "ore": "ore",
    "mystery-material": "monster-part",
    "mystery-decoration": "decoration",
    "mystery-artian": "monster-part",
}

SOURCE = ROOT / "source"
MHDB = SOURCE / "monster-hunter-DB"
API_CACHE = SOURCE / "api_cache"
FANDOM_OUT = SOURCE / "fandom-processed"
MHST2_CLEANED = SOURCE / "mhst2-cleaned"
ITEM_ICONS = SOURCE / "item-icons"  # rendered generic item-type icons
I18N_DIR = SOURCE / "i18n"          # localized name/desc overlay (committed)

DATA = ROOT / "data"
ICONS = ROOT / "icons"

# Game-name strings that map to MHW+Iceborne for mhw-db data merging.
MHW_GAMES = {"Monster Hunter World", "Monster Hunter Iceborne"}
WILDS_GAMES = {"Monster Hunter Wilds"}


def load_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text())


def copy_icon(src: Path, dest: Path) -> None:
    """Copy an icon to dest as PNG, rendering it first if the source is SVG.

    Most sources are already PNG, but some Fandom icons ship as SVG; copying
    those verbatim to a .png path would produce an invalid file (SVG bytes
    under a .png name), so render via resvg-py when the extension is .svg.
    """
    if src.suffix.lower() == ".svg":
        import resvg_py

        png = resvg_py.svg_to_bytes(svg_path=str(src), width=128, height=128)
        dest.write_bytes(png)
    else:
        shutil.copy2(src, dest)


def _fandom_clean_slug(slug: str) -> str:
    """Normalize a Fandom manifest slug to match MHDB monster slugs.

    Fandom wiki filenames carry a 3-digit sequence suffix (e.g. Rathalos
    'MHR-Rathalos_Icon_001.png' -> slug 'rathalos-001'). MHDB monsters use the
    bare name ('rathalos'), so we strip the trailing '-NNN'. Only mhrise icons
    carry this suffix; other games are unaffected.
    """
    return re.sub(r"-\d{3}$", "", slug)


def build_icon_lookup() -> dict:
    """Build per-source {game_prefix: {slug: path}} lookups from processed dirs."""
    lookups: dict[str, dict[str, dict[str, Path]]] = {}

    def add(source: str, game: str, slug: str, path: Path):
        lookups.setdefault(source, {}).setdefault(game, {})[slug] = path

    # Cleaned MHST2 icons (dark frame removed) — preferred mhst2 source.
    mhst2_man = load_json(MHST2_CLEANED / "_manifest.json") or []
    for rec in mhst2_man:
        add("mhst2-cleaned", "mhst2", rec["slug"], MHST2_CLEANED / rec["filename"])

    # Fandom icons are organised by game already. Strip the '-NNN' sequence
    # suffix (see _fandom_clean_slug); when a monster has multiple variants
    # (-001, -002, ...), prefer -001 as the canonical icon.
    fandom_man = load_json(FANDOM_OUT / "_manifest.json") or []
    fandom_seen: dict[str, dict[str, Path]] = {}  # {game: {clean_slug: path}}
    for rec in fandom_man:
        game = rec["game"]
        raw_slug = rec["slug"]
        path = FANDOM_OUT / rec["filename"]
        clean = _fandom_clean_slug(raw_slug)
        is_canonical = raw_slug.endswith("-001")
        slot = fandom_seen.setdefault(game, {})
        # Prefer -001; otherwise keep the first seen (deterministic via sorted manifest).
        if clean not in slot or is_canonical:
            slot[clean] = path
    for game, slot in fandom_seen.items():
        lookups.setdefault("fandom", {})[game] = slot

    return lookups


def build_item_icon_lookup() -> dict[str, dict[str, Path]]:
    """Build a {kind: {color: path}} lookup from source/item-icons/_manifest.json.

    Returns an empty dict if the manifest is missing (e.g. fetch_item_icons.py
    hasn't run); build_items treats that as 'no item icons available'.
    """
    data = load_json(ITEM_ICONS / "_manifest.json")
    # Manifest is {source, fetched_at, icon_count, icons:[...]}; fall back to a
    # flat array for robustness if the shape ever differs.
    if isinstance(data, dict):
        records = data.get("icons", [])
    elif isinstance(data, list):
        records = data
    else:
        records = []
    out: dict[str, dict[str, Path]] = {}
    for rec in records:
        out.setdefault(rec["kind"], {})[rec["color"]] = ITEM_ICONS / rec["svg"]
    return out


def resolve_item_icon(name: str, wilds_icon: dict | None,
                      lookup: dict[str, dict[str, Path]]) -> tuple[Path, str] | None:
    """Resolve an item to its generic type-icon file, or None.

    Wilds items use their real {kind, color}; MHW items get an inferred kind
    and the default neutral color. Returns (path, kind) on hit.
    """
    kc = item_icon_kind_color(name, wilds_icon=wilds_icon)
    if kc is None:
        return None
    kind, color = kc
    # The Fandom icon set names kinds differently from the Wilds API / infer
    # rules; alias onto the vocabulary that actually has an illustration.
    kind = KIND_ALIASES.get(kind, kind)
    color_map = lookup.get(kind)
    if not color_map:
        return None
    # Try the exact color, then fall back to a neutral white if absent.
    path = color_map.get(color) or color_map.get("white")
    if path is None:
        # Any color variant of this kind is still the right illustration.
        path = next(iter(color_map.values()))
    return path, kind


def baseline_icon_path(ref: str) -> Path | None:
    """Resolve a monster-hunter-DB icon ref to its source PNG, if present."""
    ref = fix_icon_ref(ref)
    if ref is None:
        return None
    return MHDB / "icons" / ref


def choose_icon(
    slug: str,
    game: str,
    mhdb_ref: str | None,
    lookups: dict,
) -> tuple[Path | None, str | None]:
    """Pick the best icon for (slug, game). Returns (source_path, origin).

    Priority is source-specific so a higher-quality derived source can outrank
    the monster-hunter-DB baseline where it overlaps:
      - mhst2: cleaned MHDB (dark frame removed) > raw monster-hunter-DB > fandom
      - mhrise: Fandom (clean colored art) > monster-hunter-DB (its Rise icons
        are a monochrome ink style that doesn't render as character art)
      - other games: monster-hunter-DB > fandom
    """
    # Build the ordered candidate list for this game.
    candidates: list[tuple[str, Path | None]] = []

    # Special sources that outrank the baseline for their game.
    if game == "mhst2":
        p = lookups.get("mhst2-cleaned", {}).get(game, {}).get(slug)
        candidates.append(("mhst2-cleaned", p))

    # mhrise: prefer Fandom's colored icons over MHDB's ink-style ones.
    if game == "mhrise":
        candidates.append(("fandom", lookups.get("fandom", {}).get(game, {}).get(slug)))

    # monster-hunter-DB baseline.
    if mhdb_ref:
        candidates.append(("monster-hunter-DB", baseline_icon_path(mhdb_ref)))

    # Fandom fallback for the same game.
    candidates.append(("fandom", lookups.get("fandom", {}).get(game, {}).get(slug)))

    for origin, path in candidates:
        if path and path.exists():
            return path, origin

    # Last resort: Fandom across all games (slug-only match).
    for gmap in lookups.get("fandom", {}).values():
        if slug in gmap and gmap[slug].exists():
            return gmap[slug], f"fandom(cross:{game})"
    return None, None


def merge_numeric(baseline: dict) -> dict:
    """Attach mhw-db, wilds, and/or mhgu numeric data to a monster by name."""
    name = baseline["name"]
    enriched = {}

    # mhw-db covers MHW + Iceborne.
    mhw = load_json(API_CACHE / "mhw_monsters.json") or []
    m = next((x for x in mhw if x["name"] == name), None)
    if m:
        enriched["mhw"] = {
            "description": m.get("description"),
            "species": m.get("species"),
            "elements": m.get("elements", []),
            "weaknesses": m.get("weaknesses", []),
            "resistances": m.get("resistances", []),
            "ailments": m.get("ailments", []),
            "locations": m.get("locations", []),
            "rewards": m.get("rewards", []),
        }

    # wilds covers Wilds.
    wilds = load_json(API_CACHE / "wilds_monsters.json") or []
    w = next((x for x in wilds if x["name"] == name), None)
    if w:
        enriched["wilds"] = {
            "description": w.get("description"),
            "species": w.get("species"),
            "elements": w.get("elements", []),
            "weaknesses": w.get("weaknesses", []),
            "resistances": w.get("resistances", []),
            "ailments": w.get("ailments", []),
            "locations": w.get("locations", []),
            "rewards": w.get("rewards", []),
            "parts": w.get("parts", []),
            "tips": w.get("tips", []),
            "features": w.get("features"),
        }

    # mhgu covers the Generations Ultimate roster (returning MHFU/MH3U/MH4U
    # monsters). Provides weakness ratings (1-6), hitzones by body part,
    # status thresholds, base HP, and trap/item effectiveness — fields the
    # two APIs lack for older games.
    mhgu = load_json(API_CACHE / "mhgu_monsters.json") or []
    g = next((x for x in mhgu if x["name"] == name), None)
    if g:
        enriched["mhgu"] = {
            "species": None,  # MHGU db has no species field
            "base_hp": g.get("base_hp"),
            "weakness": g.get("weakness", []),
            "traps": g.get("traps"),
            "hitzones": g.get("hitzones", []),
            "ailments": g.get("ailments", []),
            "status": g.get("status", []),
            "habitats": g.get("habitats", []),
        }

    return enriched


def build_monsters(lookups: dict, stats: dict) -> list[dict]:
    raw = load_json(MHDB / "monsters.json")
    monsters = raw["monsters"] if isinstance(raw, dict) else raw

    out: list[dict] = []
    seen_slugs: set[str] = set()
    for m in monsters:
        name = m["name"]
        slug = slugify(name)
        if slug in seen_slugs:
            stats.setdefault("duplicates", []).append(name)
            continue
        seen_slugs.add(slug)
        is_large = m.get("isLarge", False)
        games_out: list[dict] = []
        for g in m.get("games", []):
            game_full = g["game"]
            ref = g.get("image")
            stats["icon_refs"] += 1
            # game_full is authoritative for which game the monster belongs to.
            # The icon-ref prefix only overrides it for true expansions: MHDB
            # records Iceborne (MHWI-) icons under "Monster Hunter World" and
            # Sunbreak (MHRS-) icons under "Monster Hunter Rise", and we keep
            # the expansion subdir to preserve that distinction. Every other
            # prefix mismatch is a cross-borrow (e.g. a "Monster Hunter
            # Generations Ultimate" entry reusing a MH4U- icon) and must NOT
            # override game_full — doing so used to put MHGU monsters under
            # mh4u/, hiding them from the mhgu listing.
            base = GAME_PREFIX.get(game_full)
            icon_game = icon_ref_to_game(ref) if ref else None
            # Keep the expansion subdir only when the icon prefix actually is
            # the expansion's (and is recognized). icon_game can be None for
            # unparseable refs (MHWs_, FrontierGen-, MH4-), in which case the
            # None == None check below would false-positive — guard with `and`.
            if icon_game and icon_game == GAME_EXPANSION_ICON.get(game_full):
                game = icon_game
            else:
                game = base
            if game is None:
                stats["unknown_game"].append((name, game_full))
                game = slugify(game_full)
            icon, origin = choose_icon(slug, game, ref, lookups)
            entry = {
                "game": game,
                "game_full": game_full,
                "info": g.get("info"),
                "danger": g.get("danger"),
            }
            if icon and icon.exists():
                dest = ICONS / game / f"{slug}.png"
                dest.parent.mkdir(parents=True, exist_ok=True)
                copy_icon(icon, dest)
                entry["icon"] = f"{game}/{slug}.png"
                entry["icon_source"] = origin
                stats["resolved"] += 1
                stats["origin"][origin] = stats["origin"].get(origin, 0) + 1
            else:
                stats["missing"].append((name, game_full, ref))
            games_out.append(entry)

        record = {
            "id": m.get("_id", {}).get("$oid"),
            "name": name,
            "slug": slug,
            "type": m.get("type"),
            "species": None,
            "is_large": is_large,
            "sub_species": m.get("subSpecies", []),
            "elements": m.get("elements", []),
            "ailments": m.get("ailments", []),
            "weakness": m.get("weakness", []),
            "games": games_out,
        }
        numeric = merge_numeric(m)
        if numeric:
            record["numeric"] = numeric
            if numeric.get("mhw", {}).get("species"):
                record["species"] = numeric["mhw"]["species"]
            elif numeric.get("wilds", {}).get("species"):
                record["species"] = numeric["wilds"]["species"]
        out.append(record)

    out.sort(key=lambda r: r["name"].lower())
    stats["monster_count"] = len(out)
    return out


def build_items(item_lookup: dict[str, dict[str, Path]], stats: dict) -> list[dict]:
    mhw_items = load_json(API_CACHE / "mhw_items.json") or []
    wilds_items = load_json(API_CACHE / "wilds_items.json") or []

    seen: dict[str, dict] = {}
    for it in mhw_items:
        seen.setdefault(it["name"].lower(), {
            "name": it["name"],
            "slug": slugify(it["name"]),
            "description": it.get("description"),
            "rarity": it.get("rarity"),
            "value": it.get("value"),
            "carry_limit": it.get("carryLimit"),
            "sources": [],
        })["sources"].append({"game": "mhw", "id": it.get("id")})

    for it in wilds_items:
        key = it["name"].lower()
        rec = seen.get(key)
        entry = {"game": "wilds", "id": it.get("id")}
        if rec is None:
            rec = {
                "name": it["name"],
                "slug": slugify(it["name"]),
                "description": it.get("description"),
                "rarity": it.get("rarity"),
                "value": it.get("value"),
                "carry_limit": it.get("carryLimit"),
                "sources": [entry],
            }
            seen[key] = rec
        else:
            rec["sources"].append(entry)
        # Wilds items carry extra icon + recipe metadata; attach it.
        if it.get("icon"):
            rec.setdefault("wilds_icon", it["icon"])
        if it.get("recipes"):
            rec.setdefault("wilds_recipes", it["recipes"])

    out = sorted(seen.values(), key=lambda r: r["name"].lower())

    # Attach generic type icons (one illustration per kind, e.g. all Scales
    # share the Scale icon). Wilds items use their real kind/color; MHW items
    # get an inferred kind. Icons land under icons/items/<slug>.png.
    item_icon_dir = ICONS / "items"
    if item_lookup:
        item_icon_dir.mkdir(parents=True, exist_ok=True)
    stats.setdefault("item_icon_refs", len(out))
    stats.setdefault("item_icons_resolved", 0)
    stats.setdefault("item_icon_origin", {})
    for rec in out:
        if not item_lookup:
            break
        hit = resolve_item_icon(rec["name"], rec.get("wilds_icon"), item_lookup)
        if hit is None:
            continue
        icon_path, kind = hit
        dest = item_icon_dir / f"{rec['slug']}.png"
        copy_icon(icon_path, dest)
        rec["icon"] = f"items/{rec['slug']}.png"
        rec["icon_source"] = f"item-type:{kind}"
        stats["item_icons_resolved"] += 1
        stats["item_icon_origin"][kind] = stats["item_icon_origin"].get(kind, 0) + 1

    return out


def build_endemic_life() -> list[dict]:
    raw = load_json(MHDB / "endemicLife.json")
    life = raw["endemicLife"] if isinstance(raw, dict) else raw
    out = []
    for e in life or []:
        games = []
        for g in e.get("game", []):
            games.append({
                "game": GAME_PREFIX.get(g.get("game"), slugify(g.get("game", ""))),
                "game_full": g.get("game"),
                "info": g.get("info"),
                "icon_ref": g.get("image"),
            })
        out.append({
            "name": e.get("name"),
            "slug": slugify(e.get("name", "")),
            "games": games,
        })
    out.sort(key=lambda r: (r["name"] or "").lower())
    return out


def apply_i18n(records: list[dict], i18n_path: Path) -> None:
    """Overlay localized name/desc onto records without touching English fields.

    The i18n files are committed static data (source/i18n/*.json), generated
    locally via tools/generate_i18n.py — not part of the ETL fetch/extract
    pipeline. If the file is missing, records stay English-only.
    """
    if not i18n_path.exists():
        return
    i18n = json.loads(i18n_path.read_text())
    for rec in records:
        t = i18n.get(rec.get("slug"))
        if t:
            rec["i18n"] = t


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    # Reset icons/ output for idempotency.
    for d in ICONS.iterdir():
        if d.is_dir():
            for f in d.glob("*"):
                if f.is_file():
                    f.unlink()

    lookups = build_icon_lookup()
    stats: dict = {
        "icon_refs": 0,
        "resolved": 0,
        "missing": [],
        "origin": {},
        "unknown_game": [],
    }

    monsters = build_monsters(lookups, stats)
    apply_i18n(monsters, I18N_DIR / "monsters.json")
    (DATA / "monsters.json").write_text(
        json.dumps(monsters, ensure_ascii=False, indent=2, sort_keys=False)
    )

    items = build_items(build_item_icon_lookup(), stats)
    apply_i18n(items, I18N_DIR / "items.json")
    (DATA / "items.json").write_text(
        json.dumps(items, ensure_ascii=False, indent=2, sort_keys=False)
    )

    endemic = build_endemic_life()
    (DATA / "endemic_life.json").write_text(
        json.dumps(endemic, ensure_ascii=False, indent=2, sort_keys=False)
    )

    numeric_mhw = sum(1 for m in monsters if m.get("numeric", {}).get("mhw"))
    numeric_wilds = sum(1 for m in monsters if m.get("numeric", {}).get("wilds"))
    numeric_mhgu = sum(1 for m in monsters if m.get("numeric", {}).get("mhgu"))

    print("== build summary ==")
    print(f"  monsters: {stats['monster_count']}")
    dupes = stats.get("duplicates", [])
    if dupes:
        print(f"  duplicates skipped: {len(dupes)} — {', '.join(dupes)}")
    print(f"  icon refs: {stats['icon_refs']}")
    print(f"  resolved: {stats['resolved']}")
    print(f"  missing: {len(stats['missing'])}")
    print(f"  by source: {stats['origin']}")
    print(f"  items: {len(items)}")
    if stats.get("item_icon_refs"):
        print(f"  item icons: {stats['item_icons_resolved']}/{stats['item_icon_refs']}")
    print(f"  endemic life: {len(endemic)}")
    print(f"  mhw numeric merge: {numeric_mhw}")
    print(f"  wilds numeric merge: {numeric_wilds}")
    print(f"  mhgu numeric merge: {numeric_mhgu}")

    # Persist stats for validate.py and CI summaries.
    stats["items"] = len(items)
    stats["endemic_life"] = len(endemic)
    stats["numeric_mhw"] = numeric_mhw
    stats["numeric_wilds"] = numeric_wilds
    stats["numeric_mhgu"] = numeric_mhgu
    (DATA / "_build_stats.json").write_text(json.dumps(stats, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
