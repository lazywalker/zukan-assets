"""Endemic life: rocky-moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rocky-moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (150, 144, 134, 255)
CONFIG["palette"]["D"] = (112, 106, 98, 255)
