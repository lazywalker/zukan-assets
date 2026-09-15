"""Endemic life: downy-crake.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "downy-crake"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (204, 194, 172, 255)
CONFIG["palette"]["D"] = (160, 148, 126, 255)
CONFIG["palette"]["C"] = (236, 228, 208, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 5, 10, "D"),
    ("put", 6, 9, "D"),
    ("put", 6, 14, "D"),
]
