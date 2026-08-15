"""Endemic life: scale-lizard.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "scale-lizard"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (120, 140, 160, 255)
CONFIG["palette"]["D"] = (88, 106, 126, 255)
CONFIG["palette"]["C"] = (186, 200, 214, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(13, 6, 24), (14, 7, 26), (15, 8, 27), (16, 9, 28), (17, 10, 29), (18, 11, 30)], "C", "D"),
]
