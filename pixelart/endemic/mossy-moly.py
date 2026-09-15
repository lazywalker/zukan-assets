"""Endemic life: mossy-moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "mossy-moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (150, 160, 110, 255)
CONFIG["palette"]["D"] = (112, 120, 80, 255)
CONFIG["palette"]["F"] = (66, 74, 52, 255)
