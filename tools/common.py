"""Shared helpers for zukan-assets tools."""

from __future__ import annotations

import re

# Monster names that contain hyphens as part of the name itself
# (Ahtal-Ka, Pukei-Pukei, Tobi-Kadachi). Hyphens are preserved; spaces,
# apostrophes, periods, colons are normalized away.

# chars removed entirely (cf. pokeget's special-char handling)
_DROP = set("'.:")


def slugify(name: str) -> str:
    """Normalize a monster name to a lowercase slug for filenames.

    Rules:
      - lowercase
      - spaces and underscores -> '-'
      - apostrophes, periods, colons removed (Safi'jiiva -> safijiiva)
      - hyphens preserved (Ahtal-Ka -> ahtal-ka)
      - collapse repeated hyphens
    """
    s = name.strip().lower()
    out: list[str] = []
    for ch in s:
        if ch in _DROP:
            continue
        if ch in (" ", "_"):
            out.append("-")
        else:
            out.append(ch)
    slug = "".join(out)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


# Full game-name -> short-prefix mapping, matching the monster-hunter-DB
# `games[].game` strings and our `icons/<prefix>/` directories.
GAME_PREFIX = {
    "Monster Hunter Freedom Unite": "mhfu",
    "Monster Hunter 3 Ultimate": "mh3u",
    "Monster Hunter 4 Ultimate": "mh4u",
    "Monster Hunter Generations Ultimate": "mhgu",
    "Monster Hunter World": "mhw",
    "Monster Hunter Iceborne": "mhwi",
    "Monster Hunter Rise": "mhrise",
    "Monster Hunter Sunbreak": "mhrs",
    "Monster Hunter Wilds": "mhwilds",
    "Monster Hunter Stories": "mhst",
    "Monster Hunter Stories 2": "mhst2",
}

# The 7 known typo'd icon references in monster-hunter-DB/monsters.json.
# Each maps the broken image filename -> the corrected one present in
# source/monster-hunter-DB/icons/.
ICON_TYPO_FIXES = {
    "MHSWilds-Omega_Planetes_Icon.png": "MHWilds-Omega_Planetes_Icon.png",
    "MHWs_Piragill_Icon.png": "MHWilds-Piragill_Icon.png",
    "MHRS-Shagaru_Magala_Icon.png": "MHRS-Shagaru_Magala_Icon.png",  # genuinely missing
    "MHST-Vespoid_Icon.png": "MHST-Vespoid_Icon.png",  # genuinely missing
    "MHFU-Yian_Garuga_Icon": "MHFU-Yian_Garuga_Icon.png",  # dropped ext
    "FrontierGen-Remobra_Icon.png": "FrontierGen-Remobra_Icon.png",  # frontier, skip
}


def fix_icon_ref(ref: str) -> str | None:
    """Apply known typo fixes; return None if the ref should be dropped."""
    if ref in ICON_TYPO_FIXES:
        fixed = ICON_TYPO_FIXES[ref]
        return None if fixed == ref and ref in {
            "MHRS-Shagaru_Magala_Icon.png",
            "MHST-Vespoid_Icon.png",
            "FrontierGen-Remobra_Icon.png",
        } else fixed
    return ref


def icon_ref_to_game(ref: str) -> str | None:
    """Derive the game prefix from a monster-hunter-DB icon filename.

    e.g. 'MHFU-Rathalos_Icon.png' -> 'mhfu'. Returns None if unknown.
    """
    prefix_map = {
        "MHFU": "mhfu",
        "MH3U": "mh3u",
        "MH4U": "mh4u",
        "MHGU": "mhgu",
        "MHGen": "mhgu",
        "MHST": "mhst",
        "MHST2": "mhst2",
        "MHW": "mhw",
        "MHWI": "mhwi",
        "MHRise": "mhrise",
        "MHRS": "mhrs",
        "MHWilds": "mhwilds",
        "MHSWilds": "mhwilds",
    }
    code = ref.split("-", 1)[0]
    return prefix_map.get(code)


def icon_ref_to_monster_slug(ref: str) -> str:
    """Derive the monster slug from a monster-hunter-DB icon filename.

    'MHFU-Rathalos_Icon.png' -> 'rathalos'
    'MH4U-Azure_Rathalos_Icon.png' -> 'azure-rathalos'
    """
    stem = ref.rsplit(".", 1)[0]  # drop .png
    if "-" in stem:
        _, rest = stem.split("-", 1)
    else:
        rest = stem
    rest = rest.replace("_Icon", "")
    rest = rest.replace("_", " ").strip()
    return slugify(rest)
