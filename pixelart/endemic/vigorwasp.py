"""Endemic life: vigorwasp.
Derived from the archetype base; palette carries the species identity."""
from _wasp import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "vigorwasp"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
