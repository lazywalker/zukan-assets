"""Endemic life: butterflame.
Derived from the archetype base; palette carries the species identity."""
from _butterfly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "butterflame"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (210, 130, 60, 255)
CONFIG["palette"]["D"] = (164, 94, 40, 255)
CONFIG["palette"]["W"] = (250, 200, 110, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(7, 7, 8), (8, 6, 7), (7, 18, 19), (8, 19, 20)], "W", "B"),
]
