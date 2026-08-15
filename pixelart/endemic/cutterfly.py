"""Endemic life: cutterfly.
Derived from the archetype base; palette carries the species identity."""
from _butterfly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "cutterfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (176, 176, 186, 255)
CONFIG["palette"]["D"] = (134, 134, 146, 255)
