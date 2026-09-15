"""Endemic life: clothfly.
Derived from the archetype base; palette carries the species identity."""
from _butterfly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "clothfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (204, 194, 152, 255)
CONFIG["palette"]["D"] = (160, 148, 110, 255)
