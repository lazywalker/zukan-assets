"""Endemic life: flashfly.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "flashfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 116, 140, 255)
CONFIG["palette"]["G"] = (250, 240, 140, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 16, 22), (11, 15, 23), (12, 16, 21)], "G", "D"),
]
