"""Endemic life: emerald-helmcrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "emerald-helmcrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (80, 150, 110, 255)
CONFIG["palette"]["D"] = (58, 112, 82, 255)
CONFIG["palette"]["C"] = (190, 230, 206, 255)
