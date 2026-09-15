"""Endemic life: omenfly.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "omenfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 90, 90, 255)
CONFIG["palette"]["D"] = (112, 62, 62, 255)
CONFIG["palette"]["G"] = (235, 150, 120, 255)
