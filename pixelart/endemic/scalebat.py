"""Endemic life: scalebat.
Derived from the archetype base; palette carries the species identity."""
from _bat import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "scalebat"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (130, 130, 140, 255)
CONFIG["palette"]["D"] = (94, 94, 104, 255)
CONFIG["palette"]["C"] = (180, 180, 192, 255)
