"""Endemic life: pink-parexus.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pink-parexus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (226, 160, 180, 255)
CONFIG["palette"]["D"] = (184, 118, 146, 255)
CONFIG["palette"]["C"] = (244, 210, 220, 255)
