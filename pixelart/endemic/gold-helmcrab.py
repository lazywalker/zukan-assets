"""Endemic life: gold-helmcrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gold-helmcrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (222, 178, 82, 255)
CONFIG["palette"]["D"] = (178, 138, 58, 255)
CONFIG["palette"]["C"] = (246, 224, 150, 255)
