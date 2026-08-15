"""Endemic life: orange-spiritbird.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "orange-spiritbird"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (230, 140, 70, 255)
CONFIG["palette"]["D"] = (176, 102, 46, 255)
CONFIG["palette"]["C"] = (250, 210, 160, 255)
CONFIG["palette"]["G"] = (255, 230, 160, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(11, 16, 21), (12, 18, 22)], "G", "D"),
]
