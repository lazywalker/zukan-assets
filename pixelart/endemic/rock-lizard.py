"""Endemic life: rock-lizard.
Derived from the archetype base; palette carries the species identity."""
from _gekko import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rock-lizard"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 140, 120, 255)
CONFIG["palette"]["D"] = (114, 104, 88, 255)
CONFIG["palette"]["C"] = (200, 190, 168, 255)
