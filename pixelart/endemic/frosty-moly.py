"""Endemic life: frosty-moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "frosty-moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (200, 220, 240, 255)
CONFIG["palette"]["D"] = (156, 180, 206, 255)
