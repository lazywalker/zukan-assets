"""Endemic life: hellbill.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hellbill"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (96, 70, 70, 255)
CONFIG["palette"]["D"] = (66, 46, 46, 255)
CONFIG["palette"]["C"] = (150, 110, 110, 255)
CONFIG["palette"]["R"] = (220, 90, 70, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(7, 6, 7)], "R", "Y"),
]
