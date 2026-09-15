"""Endemic life: nitrotoad.
Derived from the archetype base; palette carries the species identity."""
from _toad import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nitrotoad"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 110, 140, 255)
CONFIG["palette"]["D"] = (64, 80, 106, 255)
CONFIG["palette"]["C"] = (160, 180, 206, 255)
CONFIG["palette"]["G"] = (214, 120, 60, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(9, 8, 10), (9, 17, 19)], "G", "D"),
]
