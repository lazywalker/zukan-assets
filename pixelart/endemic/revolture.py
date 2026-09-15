"""Endemic life: revolture.
Derived from the archetype base; palette carries the species identity."""
from _wasp import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "revolture"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["L"] = (220, 130, 120, 255)
CONFIG["palette"]["D"] = (172, 94, 86, 255)
CONFIG["palette"]["B"] = (110, 80, 56, 255)
