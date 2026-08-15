"""Endemic life: forest-gekko.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "forest-gekko"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
