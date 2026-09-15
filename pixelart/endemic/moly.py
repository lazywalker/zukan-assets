"""Endemic life: moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
