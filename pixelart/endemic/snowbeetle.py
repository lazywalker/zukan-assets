"""Endemic life: snowbeetle.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "snowbeetle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (220, 228, 236, 255)
CONFIG["palette"]["D"] = (176, 186, 200, 255)
