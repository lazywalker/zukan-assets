"""Endemic life: giganha.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "giganha"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 60, 70, 255)
CONFIG["palette"]["D"] = (100, 40, 52, 255)
CONFIG["palette"]["C"] = (196, 116, 118, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 11, 4, "W"),
    ("put", 11, 6, "W"),
    ("put", 12, 4, "W"),
    ("put", 12, 6, "W"),
]
