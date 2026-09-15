"""Endemic life: blastoad.
Derived from the archetype base; palette carries the species identity."""
from _toad import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blastoad"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 90, 90, 255)
CONFIG["palette"]["D"] = (112, 62, 62, 255)
CONFIG["palette"]["C"] = (210, 160, 160, 255)
CONFIG["palette"]["G"] = (240, 170, 80, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(9, 8, 10), (9, 17, 19)], "G", "D"),
]
