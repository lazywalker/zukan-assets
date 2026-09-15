"""Endemic life: felicicrow.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "felicicrow"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (70, 66, 74, 255)
CONFIG["palette"]["D"] = (48, 44, 52, 255)
CONFIG["palette"]["C"] = (110, 104, 114, 255)
