"""Endemic life: carrier-ant.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "carrier-ant"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 100, 70, 255)
CONFIG["palette"]["D"] = (104, 72, 48, 255)
CONFIG["palette"]["W"] = (226, 216, 196, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 10, 12), (3, 16, 18)], "W"),
]
