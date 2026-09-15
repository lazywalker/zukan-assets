"""Endemic life: gloom-gekko.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gloom-gekko"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 90, 110, 255)
CONFIG["palette"]["D"] = (64, 64, 82, 255)
CONFIG["palette"]["C"] = (150, 152, 170, 255)
