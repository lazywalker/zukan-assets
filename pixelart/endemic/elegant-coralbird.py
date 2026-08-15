"""Endemic life: elegant-coralbird.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "elegant-coralbird"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (176, 84, 112, 255)
CONFIG["palette"]["D"] = (134, 58, 82, 255)
CONFIG["palette"]["C"] = (226, 170, 190, 255)
