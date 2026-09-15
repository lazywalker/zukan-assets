"""Endemic life: forest-pteryx.
Derived from the archetype base; palette carries the species identity."""
from _raptor import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "forest-pteryx"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (120, 140, 90, 255)
CONFIG["palette"]["D"] = (88, 104, 64, 255)
CONFIG["palette"]["C"] = (200, 210, 170, 255)
