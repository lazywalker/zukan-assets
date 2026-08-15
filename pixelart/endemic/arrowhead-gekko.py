"""Endemic life: arrowhead-gekko.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "arrowhead-gekko"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (170, 90, 70, 255)
CONFIG["palette"]["D"] = (130, 64, 48, 255)
CONFIG["palette"]["C"] = (224, 190, 160, 255)
CONFIG["palette"]["W"] = (240, 224, 200, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 2, 6), (11, 1, 6)], "W", "B"),
]
