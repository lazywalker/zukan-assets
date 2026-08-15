"""Endemic life: spiny-moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "spiny-moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (180, 160, 130, 255)
CONFIG["palette"]["D"] = (136, 118, 94, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 8, 10, "W"),
    ("put", 9, 14, "W"),
    ("put", 8, 17, "W"),
    ("put", 9, 20, "W"),
]
