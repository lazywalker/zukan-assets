"""Endemic life: firebeetle.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "firebeetle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (170, 80, 60, 255)
CONFIG["palette"]["D"] = (130, 56, 42, 255)
CONFIG["palette"]["G"] = (250, 160, 80, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 8, 20), (11, 6, 21), (12, 7, 20)], "G", "B"),
]
