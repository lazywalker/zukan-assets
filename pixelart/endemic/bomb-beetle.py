"""Endemic life: bomb-beetle.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bomb-beetle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (80, 86, 72, 255)
CONFIG["palette"]["D"] = (56, 62, 52, 255)
CONFIG["palette"]["G"] = (220, 90, 60, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 10, 12), (11, 17, 19), (12, 8, 10), (13, 19, 21)], "G", "B"),
]
