"""Endemic life: poisontoad.
Derived from the archetype base; palette carries the species identity."""
from _toad import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "poisontoad"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (120, 140, 80, 255)
CONFIG["palette"]["D"] = (88, 104, 56, 255)
CONFIG["palette"]["C"] = (186, 200, 140, 255)
CONFIG["palette"]["G"] = (150, 80, 160, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 8, 9), (11, 14, 15), (12, 9, 10), (12, 18, 19)], "G", "B"),
]
