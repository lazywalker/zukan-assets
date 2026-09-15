"""Endemic life: moonlight-gekko.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "moonlight-gekko"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 205, 225, 255)
CONFIG["palette"]["D"] = (158, 164, 192, 255)
CONFIG["palette"]["C"] = (236, 238, 248, 255)
