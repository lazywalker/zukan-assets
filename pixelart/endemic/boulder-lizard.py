"""Endemic life: boulder-lizard.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "boulder-lizard"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (130, 124, 116, 255)
CONFIG["palette"]["D"] = (96, 90, 84, 255)
CONFIG["palette"]["C"] = (176, 170, 160, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(13, 4, 9), (14, 5, 10), (15, 6, 10)], "D", "B"),
]
