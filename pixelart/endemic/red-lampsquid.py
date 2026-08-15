"""Endemic life: red-lampsquid.
Derived from the archetype base; palette carries the species identity."""
from _lampsquid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "red-lampsquid"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 70, 64, 255)
CONFIG["palette"]["D"] = (112, 48, 44, 255)
CONFIG["palette"]["L"] = (238, 100, 88, 255)
