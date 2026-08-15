"""Endemic life: blissbill.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blissbill"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (170, 150, 110, 255)
CONFIG["palette"]["D"] = (128, 110, 76, 255)
CONFIG["palette"]["O"] = (230, 150, 60, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(7, 6, 7), (8, 6, 6)], "O", "Y"),
]
