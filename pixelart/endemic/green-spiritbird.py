"""Endemic life: green-spiritbird.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "green-spiritbird"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 190, 130, 255)
CONFIG["palette"]["D"] = (78, 144, 96, 255)
CONFIG["palette"]["C"] = (200, 240, 210, 255)
CONFIG["palette"]["G"] = (230, 255, 200, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(11, 16, 21), (12, 18, 22)], "G", "D"),
]
