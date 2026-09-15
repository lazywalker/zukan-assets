"""Endemic life: regitrice.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "regitrice"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 170, 120, 255)
CONFIG["palette"]["D"] = (152, 126, 86, 255)
