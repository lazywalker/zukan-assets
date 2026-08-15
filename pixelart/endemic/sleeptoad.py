"""Endemic life: sleeptoad.
Derived from the archetype base; palette carries the species identity."""
from _toad import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "sleeptoad"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 120, 150, 255)
CONFIG["palette"]["D"] = (80, 88, 114, 255)
CONFIG["palette"]["C"] = (170, 180, 210, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 8, 10, "K"),
    ("put", 8, 17, "K"),
    ("put", 9, 11, "K"),
    ("put", 9, 16, "K"),
]
