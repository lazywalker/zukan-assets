"""Endemic life: gustcrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gustcrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (120, 150, 140, 255)
CONFIG["palette"]["D"] = (88, 114, 106, 255)
CONFIG["palette"]["C"] = (208, 224, 214, 255)
