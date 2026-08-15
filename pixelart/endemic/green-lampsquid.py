"""Endemic life: green-lampsquid.
Derived from the archetype base; palette carries the species identity."""
from _lampsquid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "green-lampsquid"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
