"""Endemic life: iron-helmcrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "iron-helmcrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (130, 132, 138, 255)
CONFIG["palette"]["D"] = (96, 98, 104, 255)
CONFIG["palette"]["C"] = (190, 192, 198, 255)
