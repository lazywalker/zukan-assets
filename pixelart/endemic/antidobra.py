"""Endemic life: antidobra.
Derived from the archetype base; palette carries the species identity."""
from _cobra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "antidobra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (120, 90, 150, 255)
CONFIG["palette"]["D"] = (88, 64, 112, 255)
CONFIG["palette"]["H"] = (190, 160, 220, 255)
