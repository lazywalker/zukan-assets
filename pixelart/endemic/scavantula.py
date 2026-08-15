"""Endemic life: scavantula.
Derived from the archetype base; palette carries the species identity."""
from _spider import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "scavantula"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 120, 90, 255)
CONFIG["palette"]["D"] = (112, 88, 64, 255)
CONFIG["palette"]["C"] = (210, 184, 150, 255)
