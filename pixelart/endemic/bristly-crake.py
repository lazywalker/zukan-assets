"""Endemic life: bristly-crake.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bristly-crake"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 120, 90, 255)
CONFIG["palette"]["D"] = (110, 86, 62, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 5, 9, "D"),
    ("put", 6, 8, "D"),
    ("put", 6, 13, "D"),
]
