"""Endemic life: glass-parexus.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "glass-parexus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 224, 224, 255)
CONFIG["palette"]["D"] = (150, 186, 190, 255)
CONFIG["palette"]["C"] = (240, 248, 246, 255)
