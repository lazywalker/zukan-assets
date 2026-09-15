"""Endemic life: shiny-gold-helmcrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shiny-gold-helmcrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (240, 210, 120, 255)
CONFIG["palette"]["D"] = (198, 164, 82, 255)
CONFIG["palette"]["C"] = (252, 240, 180, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 8, 12, "W"),
    ("put", 9, 16, "W"),
]
