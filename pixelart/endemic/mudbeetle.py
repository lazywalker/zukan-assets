"""Endemic life: mudbeetle.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "mudbeetle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 90, 70, 255)
CONFIG["palette"]["D"] = (80, 64, 50, 255)
CONFIG["palette"]["C"] = (160, 140, 110, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(9, 8, 20), (10, 6, 22), (11, 5, 22)], "C", "B"),
]
