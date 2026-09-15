"""Endemic life: augurfly.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "augurfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 110, 90, 255)
CONFIG["palette"]["D"] = (64, 82, 64, 255)
CONFIG["palette"]["G"] = (200, 230, 150, 255)
