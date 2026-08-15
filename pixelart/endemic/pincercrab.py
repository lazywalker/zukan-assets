"""Endemic life: pincercrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pincercrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 110, 130, 255)
CONFIG["palette"]["D"] = (112, 80, 98, 255)
CONFIG["palette"]["C"] = (222, 196, 210, 255)
