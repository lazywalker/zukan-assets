#!/usr/bin/env python3
"""Build the editor data bundle (editor/_data/data.json).

The bundle is everything the pure-frontend editor needs: precomputed
grids + editor state per sprite, a monsters.json projection for search
and the gallery, the games table, and coverage groups. The JS side never
re-implements the engine; it renders these grids and edits mask/explicit.

    python3 pixelart/build_editor_data.py              # dev bundle
    python3 pixelart/build_editor_data.py --static DIR # publishable copy

Dev mode points icon URLs at ../../icons/ (the repo checkout, served by
editor_server.py). Static mode rewrites them to icons/ and copies every
referenced icon into DIR so the bundle can be dropped on any host.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

import decompile
import spritekit as sk

HERE = Path(__file__).resolve().parent
EDITOR = HERE / "editor"
DATA_JSON = EDITOR / "_data" / "data.json"
MONSTERS_JSON = HERE.parent / "data" / "monsters.json"
ICONS = HERE.parent / "icons"

# zukan color::GAMES plus mho (in the data, absent from zukan's table).
# No expansion folding here: the reference strip shows every generation
# separately, unlike the zukan card's Games line.
GAMES = {code: {"abbr": abbr, "full": full} for code, abbr, full in [
    ("mhfu", "MHFU", "Monster Hunter Freedom Unite"),
    ("mh3u", "MH3U", "Monster Hunter 3 Ultimate"),
    ("mh4u", "MH4U", "Monster Hunter 4 Ultimate"),
    ("mhgu", "MHGU", "Monster Hunter Generations Ultimate"),
    ("mhw", "MHW", "Monster Hunter World"),
    ("mhwi", "MHWI", "Monster Hunter World: Iceborne"),
    ("mhrise", "MHRise", "Monster Hunter Rise"),
    ("mhrs", "MHRS", "Monster Hunter Rise: Sunbreak"),
    ("mhwilds", "MHWilds", "Monster Hunter Wilds"),
    ("mhst", "MHST", "Monster Hunter Stories"),
    ("mhst2", "MHST2", "Monster Hunter Stories 2"),
    ("mho", "MHO", "Monster Hunter Online"),
]}
GAME_ORDER = list(GAMES)

# same order as zukan's best_icon_path: Stories art reads best small
ICON_PREFERENCE = ["mhst2", "mhst", "mh4u", "mh3u", "mhfu", "mhgu",
                   "mhwilds", "mhwi", "mhw", "mhrise", "mhrs"]

SKELETONS = ["rathalos", "zinogre", "tigrex", "great-jaggi", "kulu-ya-ku",
             "anjanath", "vaal-hazak", "kirin", "namielle", "xenojiiva"]


def sprite_bundles():
    out = []
    mods = {}
    import importlib

    sys.path.insert(0, str(HERE / "sprites"))
    for p in sorted((HERE / "sprites").glob("*.py")):
        if not p.stem.startswith("_"):
            mods[p.stem] = importlib.import_module(p.stem)
    for stem, mod in mods.items():
        cfg = mod.CONFIG
        state = decompile.editor_state(cfg)
        parent = getattr(mod, "_base", None)
        out.append({
            "slug": cfg["name"],
            "module": stem,
            "size": list(cfg["size"]),
            "base": cfg["base"],
            "palette": {ch: list(rgba) for ch, rgba in cfg["palette"].items()},
            "mask": state["mask"],
            "explicit": state["explicit"],
            "grid": ["".join(row) for row in sk.build_grid(cfg)],
            "compare_to": cfg.get("compare_to", ""),
            "derived_from": parent["name"] if parent else "",
            "docstring": (mod.__doc__ or "").strip(),
        })
    return out


def monster_bundles():
    monsters = json.loads(MONSTERS_JSON.read_text())
    out = []
    for m in monsters:
        games = [{"game": g["game"], "icon": g["icon"]}
                 for g in m.get("games", []) if g.get("icon")]
        primary = ""
        for game in ICON_PREFERENCE:
            if any(g["game"] == game for g in games):
                primary = next(g["icon"] for g in games if g["game"] == game)
                break
        if not primary and games:
            primary = games[0]["icon"]
        out.append({
            "slug": m["slug"],
            "name": m["name"],
            "zh": m.get("i18n", {}).get("zh", {}).get("name", ""),
            "ja": m.get("i18n", {}).get("ja", {}).get("name", ""),
            "type": m.get("type", ""),
            "games": games,
            "primary_icon": primary,
        })
    return out


def build(icon_base):
    sprites = sprite_bundles()
    monsters = monster_bundles()
    done = {s["slug"] for s in sprites}
    slugs = {m["slug"] for m in monsters}
    orphans = done - slugs
    if orphans:
        sys.exit(f"sprites missing from monsters.json: {sorted(orphans)}")
    return {
        "icon_base": icon_base,
        "games": GAMES,
        "game_order": GAME_ORDER,
        "skeletons": [s for s in SKELETONS if s in done],
        "sprites": sprites,
        "monsters": monsters,
        "coverage": {
            "done": sorted(done),
            "todo": sorted(slugs - done),
        },
    }


def write_bundle(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(f"{path} ({len(data['sprites'])} sprites, "
          f"{len(data['monsters'])} monsters)")


def build_static(dest):
    dest = Path(dest)
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for item in EDITOR.iterdir():
        if item.name.startswith("_") and item.name != "_data":
            continue
        if item.is_dir():
            shutil.copytree(item, dest / item.name)
        else:
            shutil.copy2(item, dest / item.name)
    write_bundle(build(icon_base="icons/"), dest / "_data" / "data.json")
    data = json.loads((dest / "_data" / "data.json").read_text())
    copied = 0
    for m in data["monsters"]:
        for g in m["games"]:
            src = ICONS / g["icon"]
            target = dest / "icons" / g["icon"]
            if src.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, target)
                copied += 1
    print(f"static bundle: {dest} ({copied} icons)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--static", nargs="?", const=HERE / "editor-dist", type=Path,
                    help="also emit a self-contained bundle with icons copied in")
    args = ap.parse_args()
    if args.static:
        build_static(args.static)
    else:
        write_bundle(build(icon_base="../../icons/"), DATA_JSON)


if __name__ == "__main__":
    main()
