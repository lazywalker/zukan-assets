"""Endemic life: brewhare.
Derived from the archetype base; palette carries the species identity."""
from _hare import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "brewhare"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 110, 80, 255)
CONFIG["palette"]["D"] = (112, 80, 56, 255)
CONFIG["palette"]["C"] = (208, 182, 152, 255)
