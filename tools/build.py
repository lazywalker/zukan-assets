#!/usr/bin/env python3
"""Build data/ and icons/ from all sources.

Pipeline:
  1. Load monster-hunter-DB monsters.json as the baseline roster.
  2. Supplement the roster with MH4U bosses MHDB omits (Apex variants) from
     the MH4U db, so they get an icon + numeric data.
  3. For each (monster, game) icon reference, resolve it to a processed icon
     using the priority chain:
       cleaned MHST2 (mhst2) -> vendored MH4U bestiary (mh4u)
       -> monster-hunter-DB baseline -> Fandom (any game) -> mark missing.
  4. Copy the chosen icon to icons/<game>/<slug>.png.
  5. Merge per-game hunter-notes text from the baseline.
  6. Merge mhw-db (MHW/Iceborne), wilds.mhdb.io (Wilds), MHGU db
     (Generations Ultimate), and MH4U db numeric data: description,
     weaknesses, resistances, ailments, locations, rewards, hitzones,
     status, HP.
  7. Build items.json from both APIs.
  8. Build endemic_life.json from the baseline.

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
MH4U_ICONS = SOURCE / "mh4u-icons"  # vendored official MH4U bestiary icons
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

    Fandom wiki filenames carry a 3-digit sequence suffix (Rathalos
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

    # Cleaned MHST2 icons (dark frame removed), preferred mhst2 source.
    mhst2_man = load_json(MHST2_CLEANED / "_manifest.json") or []
    for rec in mhst2_man:
        add("mhst2-cleaned", "mhst2", rec["slug"], MHST2_CLEANED / rec["filename"])

    # Vendored official MH4U bestiary icons. Covers the full MH4U roster
    # including the Apex variants and Seregios that MHDB is missing.
    mh4u_man = load_json(MH4U_ICONS / "_manifest.json") or []
    for rec in mh4u_man:
        add("mh4u-icons", "mh4u", rec["slug"], MH4U_ICONS / rec["filename"])

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

    Returns an empty dict if the manifest is missing (fetch_item_icons.py
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
      - mh4u: vendored official MH4U bestiary icons > monster-hunter-DB > fandom
        (the vendored set is a strict superset: MHDB is missing Seregios, Shah
        Dalamadur, and every Apex variant)
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

    # mh4u: prefer the vendored official set; it covers the Apex variants and
    # Seregios that MHDB lacks. Same source as MHDB for the overlap, so picking
    # ours first only ever fills gaps, never changes existing icons.
    if game == "mh4u":
        candidates.append(("mh4u-icons", lookups.get("mh4u-icons", {}).get(game, {}).get(slug)))

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
    """Attach mhw-db, wilds, mhgu, and/or mh4u numeric data to a monster by name."""
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
    # status thresholds, base HP, and trap/item effectiveness, fields the
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

    # mh4u covers MH4U natively. Weakness is per-state (Normal/Enraged/Charged),
    # not the flat list mhgu produces, so the shape differs deliberately.
    # Habitats carry a joined location name; hitzones share mhgu's column set.
    mh4u = load_json(API_CACHE / "mh4u_monsters.json") or []
    h4 = next((x for x in mh4u if x["name"] == name), None)
    if h4:
        enriched["mh4u"] = {
            "name_jp": h4.get("name_jp"),
            "class": h4.get("class"),
            "signature_move": h4.get("signature_move"),
            "weakness": h4.get("weakness", {}),
            "hitzones": h4.get("hitzones", []),
            "ailments": h4.get("ailments", []),
            "status": h4.get("status", []),
            "habitats": h4.get("habitats", []),
        }

    return enriched


def _resolve_games(name: str, slug: str, games: list[dict], lookups: dict, stats: dict) -> list[dict]:
    """Turn a source's `games[]` list into the built `games[]` shape, resolving icons.

    Shared by the MHDB roster loop and the MH4U roster supplement so the
    icon-resolution rules (expansion handling, priority chain) stay in one place.
    """
    games_out: list[dict] = []
    for g in games:
        game_full = g["game"]
        ref = g.get("image")
        stats["icon_refs"] += 1
        # game_full is authoritative; the icon-ref prefix overrides it only for
        # true expansions (MHDB files Iceborne under World, Sunbreak under Rise).
        # Other prefix mismatches are cross-borrows (MHGU entry reusing a MH4U-
        # icon) and must not override, or MHGU monsters land under mh4u/.
        base = GAME_PREFIX.get(game_full)
        icon_game = icon_ref_to_game(ref) if ref else None
        # icon_game is None for unparseable refs (MHWs_, FrontierGen-, MH4-);
        # guard with `and` so the None == None check doesn't false-positive.
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
    return games_out


def _mh4u_supplement(seen_slugs: set[str], lookups: dict, stats: dict) -> list[dict]:
    """Synthesize roster entries for MH4U monsters MHDB doesn't list.

    MHDB omits six MH4U bosses (the Apex variants minus those it lists under
    other games, plus Dah'ren Mohran). The MH4U db has their full data and
    we have their icons vendored, so synthesize a minimal MHDB-shaped record
    for each missing Large monster: a single mh4u game entry whose `image`
    is the original upstream filename (so icon_ref_to_game routes it to mh4u
    and choose_icon finds it in the vendored set). Small/Minion monsters are
    skipped to avoid padding the roster with unremarkable fauna MHDB chose
    not to carry.
    """
    mh4u = load_json(API_CACHE / "mh4u_monsters.json") or []
    mh4u_man = {r["slug"]: r for r in (load_json(MH4U_ICONS / "_manifest.json") or [])}
    out: list[dict] = []
    for h4 in mh4u:
        if h4.get("class") != "Large":
            continue
        slug = slugify(h4["name"])
        if slug in seen_slugs:
            continue
        # Only emit if we have an icon to attach; otherwise the entry would
        # be iconless and the data is reachable anyway via numeric.mh4u on
        # any same-named monster from another game.
        man = mh4u_man.get(slug)
        if not man:
            continue
        seen_slugs.add(slug)
        stats.setdefault("mh4u_supplement", []).append(h4["name"])
        synthesized = {
            "name": h4["name"],
            "_id": None,
            "type": None,
            "isLarge": True,
            "games": [{
                "game": "Monster Hunter 4 Ultimate",
                "image": man["source"],  # upstream filename, like MH4U-Seregios_Icon.png
                "info": None,
                "danger": None,
            }],
        }
        out.append(_build_monster_record(synthesized, lookups, stats))
    return out


def _mho_icons() -> dict[str, dict]:
    """Lazy {slug: manifest_record} for MHO Fandom icons, cached for the build run.

    MHO is the one game with no MHDB baseline (its monsters aren't in
    monsters.json and MHDB ships no MHO- icons), so its Fandom set is the
    sole icon source. Two callers: _build_monster_record attaches an MHO game
    entry to any roster monster whose slug is in here (the 42 shared), and
    _mho_supplement synthesizes fresh records for the rest (the 36 exclusive).

    Variant suffixes (-NN, like 'merphistophelin-02') collapse to the base slug;
    the first record wins, same dedup rule build_icon_lookup applies to all
    Fandom games.
    """
    cache = _mho_icons.cache
    if cache is None:
        man = load_json(FANDOM_OUT / "_manifest.json") or []
        deduped: dict[str, dict] = {}
        for r in man:
            if r.get("game") != "mho":
                continue
            slug = re.sub(r"-\d{1,3}$", "", r["slug"])
            deduped.setdefault(slug, r)
        cache = _mho_icons.cache = deduped
    return cache
_mho_icons.cache = None


def _mho_name_from_wiki_title(wiki_title: str) -> str:
    """'File:MHO-Abiorugu Icon.png' -> 'Abiorugu', preserving spaces/case.

    The Fandom manifest has no name field, only wiki_title; the slug loses
    case and word boundaries, so the title is the only source of the real name.
    """
    name = wiki_title.split(":", 1)[-1]      # drop "File:"
    _, rest = name.split("-", 1)              # drop "MHO-"
    rest = rest.rsplit(" Icon", 1)[0]         # drop " Icon.png" / " Icon 02.png"
    return rest


def _mho_game_entry(rec: dict) -> dict:
    """One source-shape games[] entry for an MHO monster, routed via its wiki title."""
    return {
        "game": "Monster Hunter Online",
        # image is the Fandom filename (sans "File:"); icon_ref_to_game routes
        # the MHO- prefix to mho, choose_icon's fandom fallback finds the slug.
        "image": rec["wiki_title"].split(":", 1)[-1],
        "info": None,
        "danger": None,
    }


def _build_monster_record(m: dict, lookups: dict, stats: dict) -> dict:
    """Build one output monster record from a source entry (MHDB or synthesized)."""
    name = m["name"]
    slug = slugify(name)
    # Attach an MHO game entry to any roster monster that has an MHO icon and
    # doesn't already list Monster Hunter Online (the 36 exclusives synthesized
    # by _mho_supplement already carry one, so the any() guard skips them).
    games = list(m.get("games", []))
    mho_rec = _mho_icons().get(slug)
    if mho_rec and not any(g.get("game") == "Monster Hunter Online" for g in games):
        games.append(_mho_game_entry(mho_rec))
        stats.setdefault("mho_game_attach", []).append(name)
    games_out = _resolve_games(name, slug, games, lookups, stats)
    record = {
        "id": m.get("_id", {}).get("$oid") if isinstance(m.get("_id"), dict) else None,
        "name": name,
        "slug": slug,
        "type": m.get("type"),
        "species": None,
        "is_large": m.get("isLarge", False),
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
    return record


def _mho_supplement(seen_slugs: set[str], lookups: dict, stats: dict) -> list[dict]:
    """Synthesize roster entries for MHO monsters MHDB doesn't list at all.

    MHO monsters that MHDB already carries under another game get an MHO game
    entry attached in _build_monster_record, not a fresh record. The slugs left
    over here (not in seen_slugs) are MHO-exclusives: synthesize a minimal
    MHDB-shaped record so they ship with an icon. The Fandom set has no class
    info, so all MHO monsters are treated as Large.
    """
    out: list[dict] = []
    for slug, rec in _mho_icons().items():
        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)
        stats.setdefault("mho_supplement", []).append(slug)
        synthesized = {
            "name": _mho_name_from_wiki_title(rec["wiki_title"]),
            "_id": None,
            "type": None,
            "isLarge": True,
            "games": [_mho_game_entry(rec)],
        }
        out.append(_build_monster_record(synthesized, lookups, stats))
    return out


def build_monsters(lookups: dict, stats: dict) -> list[dict]:
    raw = load_json(MHDB / "monsters.json")
    monsters = raw["monsters"] if isinstance(raw, dict) else raw

    out: list[dict] = []
    seen_slugs: set[str] = set()
    for m in monsters:
        slug = slugify(m["name"])
        if slug in seen_slugs:
            stats.setdefault("duplicates", []).append(m["name"])
            continue
        seen_slugs.add(slug)
        out.append(_build_monster_record(m, lookups, stats))

    # Fill MH4U roster gaps (Apex variants, Dah'ren Mohran) MHDB doesn't carry.
    out.extend(_mh4u_supplement(seen_slugs, lookups, stats))

    # Fill MHO roster gaps (Abiorugu, Baelidae, Estrellian, ...) MHDB doesn't
    # carry at all. MHO monsters MHDB lists under another game already got an
    # MHO game entry attached in _build_monster_record; this adds the rest.
    out.extend(_mho_supplement(seen_slugs, lookups, stats))

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

    # Attach generic type icons (one illustration per kind: all Scales
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


def _resolve_endemic_ref(ref: str) -> str | None:
    """Normalize an endemicLife image ref to its MHDB filename, or None.

    Endemic refs hit four MHDB upstream naming bugs that monster refs don't:
    space vs underscore (Gastronome Tuna_Icon), hyphen vs underscore prefix
    separator (MHWI-Arrowhead, MHW-Flashfly; each is a one-off file whose name
    diverges from its ~60 siblings), the MMHRise typo, and Icon/icon case. Try
    the ref as-is, then each normalization in turn.
    """
    candidates = [ref, ref.replace(" ", "_")]
    # prefix separator: a couple of MHWI-/MHW- refs name files stored MHWI_/MHW_
    for prefix in ("MHWI-", "MHW-"):
        if ref.startswith(prefix):
            candidates.append(prefix.replace("-", "_") + ref[len(prefix):])
    if ref.startswith("MMHRise-"):
        candidates.append("MHRise-" + ref[len("MMHRise-"):])
    for cand in candidates:
        if (MHDB / "icons" / cand).exists():
            return cand
    # case-insensitive fallback (Gold Scalebat ships _icon, MHDB has _Icon)
    for f in (MHDB / "icons").iterdir():
        if f.name.lower() == ref.lower():
            return f.name
    return None


def build_endemic_life(stats: dict) -> list[dict]:
    raw = load_json(MHDB / "endemicLife.json")
    life = raw["endemicLife"] if isinstance(raw, dict) else raw
    endemic_dir = ICONS / "endemic"
    stats["endemic_refs"] = 0
    stats["endemic_resolved"] = 0
    out = []
    for e in life or []:
        slug = slugify(e.get("name", ""))
        games = []
        for g in e.get("game", []):
            entry = {
                "game": GAME_PREFIX.get(g.get("game"), slugify(g.get("game", ""))),
                "game_full": g.get("game"),
                "info": g.get("info"),
                "icon_ref": g.get("image"),
            }
            ref = g.get("image")
            if ref:
                stats["endemic_refs"] += 1
                resolved = _resolve_endemic_ref(ref)
                if resolved:
                    src = MHDB / "icons" / resolved
                    endemic_dir.mkdir(parents=True, exist_ok=True)
                    dest = endemic_dir / f"{slug}.png"
                    copy_icon(src, dest)
                    entry["icon"] = f"endemic/{slug}.png"
                    entry["icon_source"] = "monster-hunter-DB"
                    stats["endemic_resolved"] += 1
                else:
                    stats.setdefault("endemic_missing", []).append((e.get("name"), ref))
            games.append(entry)
        out.append({
            "name": e.get("name"),
            "slug": slug,
            "games": games,
        })
    out.sort(key=lambda r: (r["name"] or "").lower())
    return out


def apply_i18n(records: list[dict], i18n_path: Path) -> None:
    """Overlay localized name/desc onto records without touching English fields.

    The i18n files are committed static data (source/i18n/*.json), generated
    locally via tools/generate_i18n.py, not part of the ETL fetch/extract
    pipeline. If the file is missing, records stay English-only.

    The per-locale `source` provenance field is dropped on copy: it drives
    generate_i18n.py's overwrite guard from source/i18n/*.json, not from this
    output, so it is dead weight downstream.
    """
    if not i18n_path.exists():
        return
    i18n = json.loads(i18n_path.read_text())
    for rec in records:
        t = i18n.get(rec.get("slug"))
        if t:
            rec["i18n"] = {
                lang: {k: v for k, v in entries.items() if k != "source"}
                for lang, entries in t.items()
            }


def main() -> int:
    DATA.mkdir(parents=True, exist_ok=True)
    # Reset icons/ output for idempotency: remove every subdir wholesale so
    # stale game dirs from a previous build (a buggy run that created
    # slugified game_full names like 'monster-hunter-4-ultimate') don't
    # linger once empty. build_monsters recreates the dirs it needs.
    for d in ICONS.iterdir():
        if d.is_dir():
            shutil.rmtree(d, ignore_errors=True)

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

    endemic = build_endemic_life(stats)
    (DATA / "endemic_life.json").write_text(
        json.dumps(endemic, ensure_ascii=False, indent=2, sort_keys=False)
    )

    numeric_mhw = sum(1 for m in monsters if m.get("numeric", {}).get("mhw"))
    numeric_wilds = sum(1 for m in monsters if m.get("numeric", {}).get("wilds"))
    numeric_mhgu = sum(1 for m in monsters if m.get("numeric", {}).get("mhgu"))
    numeric_mh4u = sum(1 for m in monsters if m.get("numeric", {}).get("mh4u"))

    print("== build summary ==")
    print(f"  monsters: {stats['monster_count']}")
    dupes = stats.get("duplicates", [])
    if dupes:
        print(f"  duplicates skipped: {len(dupes)}: {', '.join(dupes)}")
    suppl = stats.get("mh4u_supplement", [])
    if suppl:
        print(f"  mh4u roster supplement: {len(suppl)}: {', '.join(suppl)}")
    mho_new = stats.get("mho_supplement", [])
    if mho_new:
        print(f"  mho roster supplement: {len(mho_new)}: {', '.join(mho_new)}")
    mho_att = stats.get("mho_game_attach", [])
    if mho_att:
        print(f"  mho game attach: {len(mho_att)}")
    print(f"  icon refs: {stats['icon_refs']}")
    print(f"  resolved: {stats['resolved']}")
    print(f"  missing: {len(stats['missing'])}")
    print(f"  by source: {stats['origin']}")
    print(f"  items: {len(items)}")
    if stats.get("item_icon_refs"):
        print(f"  item icons: {stats['item_icons_resolved']}/{stats['item_icon_refs']}")
    print(f"  endemic life: {len(endemic)}")
    if stats.get("endemic_refs"):
        print(f"  endemic icons: {stats['endemic_resolved']}/{stats['endemic_refs']}")
    print(f"  mhw numeric merge: {numeric_mhw}")
    print(f"  wilds numeric merge: {numeric_wilds}")
    print(f"  mhgu numeric merge: {numeric_mhgu}")
    print(f"  mh4u numeric merge: {numeric_mh4u}")

    # Persist stats for validate.py and CI summaries.
    stats["items"] = len(items)
    stats["endemic_life"] = len(endemic)
    stats["numeric_mhw"] = numeric_mhw
    stats["numeric_wilds"] = numeric_wilds
    stats["numeric_mhgu"] = numeric_mhgu
    stats["numeric_mh4u"] = numeric_mh4u
    (DATA / "_build_stats.json").write_text(json.dumps(stats, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
