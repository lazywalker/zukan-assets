"""Endemic life: peepersects.
Derived from the archetype base; palette carries the species identity."""
from _butterfly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "peepersects"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 160, 120, 255)
CONFIG["palette"]["D"] = (80, 120, 88, 255)
CONFIG["palette"]["W"] = (240, 230, 150, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(6, 7, 9), (6, 17, 19), (7, 7, 9), (7, 17, 19)], "W", "B"),
]
