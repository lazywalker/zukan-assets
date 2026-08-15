"""Endemic life: wildspire-gekko.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wildspire-gekko"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (170, 150, 90, 255)
CONFIG["palette"]["D"] = (132, 114, 64, 255)
CONFIG["palette"]["C"] = (220, 204, 150, 255)
