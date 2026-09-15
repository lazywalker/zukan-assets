"""Endemic life: golden-lampsquid.
Derived from the archetype base; palette carries the species identity."""
from _lampsquid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "golden-lampsquid"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (222, 178, 82, 255)
CONFIG["palette"]["D"] = (178, 138, 58, 255)
CONFIG["palette"]["L"] = (252, 232, 150, 255)
