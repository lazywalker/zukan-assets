#!/usr/bin/env python3
"""Map a Monster Hunter item name to its generic icon (kind, color).

MH item icons are shared per type, not per item: every "Anjanath Scale" and
"Rathalos Scale" use the same Scale illustration. The Wilds API hands us this
{kind, color} directly, but the MHW API (mhw-db) has no such field — so for
MHW items we infer the kind from the (highly regular) naming conventions:
"<Monster> <BodyPart>" for materials, or a consumable keyword (Potion, Herb...).

Color can't be reliably inferred from name or rarity (the Wilds data shows no
stable rarity→color mapping), so MHW items default to a neutral color.

Used by build.py to look up an icon in source/item-icons/_manifest.json.
"""

from __future__ import annotations

import re

# Default color for MHW items, where no color info exists. "white" is the most
# common Wilds color and reads as a neutral rarity tier.
DEFAULT_COLOR = "white"

# Ordered rules: (regex, kind). First match wins. Patterns are matched
# case-insensitively against the lowercased item name. Monster-material body
# parts come first (they're the bulk of MHW items), then consumables.
#
# Patterns use plain substring matching (no \b word boundaries) because MH
# material names are compounds — "Hardfang", "Thickhide", "Fellwing" — so a
# word-boundary anchored `fang` would miss `hardfang`. Substring `fang` catches
# both. Order matters: more specific patterns first to avoid mis-routing.
RULES: list[tuple[str, str]] = [
    # --- monster materials (by body-part root word) ---
    (r"hardfang|fang|tusk|gouge", "claw"),
    (r"hardclaw|claw|talon", "claw"),
    (r"hardhorn|temperhorn|crownhorn|horn|antler|spire", "horn"),
    (r"thickhide|finehide|ebonshell|hide|pelt|fur|skin|fleece|scalp|sinew", "hide"),
    (r"scale|shard|layer|scalp", "scale"),
    (r"spineshell|oilshell|shell|carapace|cortex|plate|chine", "shell"),
    (r"fellwing|grandfin|cutwing|wing|webbing|membrane|fin$", "wing"),
    (r"tailedge|tail|coil|segment|flail", "tail"),
    (r"frenzybone|dragonbone|nosebone|solidbone|wildbone|icebone|crimsonbone|bone|skull|jaw|beak", "bone"),
    (r"gem|jewel|manteau|phala|gemme|feystone", "gem"),
    (r"marrow|medulla|nucleus|sac|gland|node|lash", "medulla"),
    (r"lens|eye|retina|cathode|shocker", "lens"),
    (r"feather|plume|plumage", "feather"),
    (r"fluid|blood|saliva|tear|extract|sap|nectar|catalyst|reagent", "extract"),
    (r"phial|vial", "phial"),
    (r"powder|dust|ash", "powder"),
    (r"mane|whisker|hair|beard", "hide"),
    (r"ridge|crown|spire", "shell"),
    (r"streamstone|stone|ore|crystal|coal|rock|ingot|geode", "ore"),
    (r"treasure|pallium|scute|nugget|surspike|dragonhold|mud|husk|beak|crook|ripper|fuse|mass|spike", "monster-part"),
    (r"whisker|fur", "hide"),
    # --- consumables / craftables ---
    (r"potion|medicament|mega", "potion"),
    (r"herb|saffi|plant|sprout|flower|leaf", "plant"),
    (r"seed|bean|nut|acorn", "seed"),
    (r"parashroom|toadstool|mushroom|fungus", "mushroom"),
    (r"honey", "honey"),
    (r"bug|insect|beetle|butterfly|spider|firefly", "bug"),
    (r"trap|pitfall|capture", "trap"),
    (r"bomb|barrel|gunpowder|dung", "bomb"),
    (r"whetstone|sharpener", "whetstone"),
    (r"ammo|coating|slinger", "ammo-special"),
    (r"knife|stone", "knife"),
    (r"gillie|temporal|rocksteady|booster|mantle|specialist tool|tool", "mantle"),
    (r"book|scroll|manual|tome|guide|letter", "book"),
    (r"coin|ticket|voucher|pass|print|badge|melding|fireworks|appreciation", "voucher"),
    (r"armor sphere|armorstone|armorskin|armorcharm|armortalon|sphere|charm|talisman", "armor-sphere"),
    (r"decoration|deco|razor", "mystery-decoration"),
    (r"meat|steak|ration|jerky|drink|drink", "meat"),
    (r"egg", "egg"),
    (r"fish|squid|shrimp|sushi|bait", "fish"),
    (r"paintball|paint", "paintball"),
    (r"web|silk|thread", "web"),
    (r"demondrug|armorskin|drug|juice", "drug"),
    (r"pill|tablet", "pill"),
    (r"smoke", "smoke"),
    (r"fragment|relic|ancient", "mystery-material"),
    (r"weapon$|weapon$", "voucher"),
]


def infer_kind(name: str) -> str | None:
    """Return the icon kind slug for an item name, or None if no rule matches.

    The returned kind matches the Wilds API's `icon.kind` namespace and the
    `kind` field in source/item-icons/_manifest.json.
    """
    n = name.lower()
    for pattern, kind in RULES:
        if re.search(pattern, n):
            return kind
    return None


def item_icon_kind_color(name: str, *, has_wilds_icon: bool = False,
                         wilds_icon: dict | None = None) -> tuple[str, str] | None:
    """Resolve (kind, color) for an item.

    Wilds items pass through their real kind/color. MHW items get an inferred
    kind and the default neutral color. Returns None if no icon can be found.
    """
    if wilds_icon and wilds_icon.get("kind") and wilds_icon["kind"] not in ("unknown", "question"):
        return wilds_icon["kind"], wilds_icon.get("color", DEFAULT_COLOR)
    kind = infer_kind(name)
    if kind is None:
        return None
    return kind, DEFAULT_COLOR
