"""Endemic life: echobat.
Derived from the archetype base; palette carries the species identity."""
from _bat import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "echobat"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
