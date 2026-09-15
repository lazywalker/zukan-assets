"""Endemic life: rowdy-moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rowdy-moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (200, 150, 110, 255)
CONFIG["palette"]["D"] = (152, 110, 78, 255)
CONFIG["palette"]["F"] = (90, 52, 40, 255)
