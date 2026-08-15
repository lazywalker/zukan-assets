"""Endemic life: lanterbug.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lanterbug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (100, 90, 80, 255)
CONFIG["palette"]["D"] = (72, 64, 56, 255)
CONFIG["palette"]["G"] = (250, 180, 90, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 18, 23), (11, 17, 23), (12, 18, 22)], "G", "D"),
]
