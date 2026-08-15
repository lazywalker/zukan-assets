"""Endemic life: red-spiritbird.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "red-spiritbird"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 70, 60, 255)
CONFIG["palette"]["D"] = (150, 46, 40, 255)
CONFIG["palette"]["C"] = (238, 160, 150, 255)
CONFIG["palette"]["G"] = (255, 190, 170, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(11, 16, 21), (12, 18, 22)], "G", "D"),
]
