"""Endemic life: tricktoad.
Derived from the archetype base; palette carries the species identity."""
from _toad import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "tricktoad"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 120, 90, 255)
CONFIG["palette"]["D"] = (112, 88, 64, 255)
CONFIG["palette"]["C"] = (204, 180, 146, 255)
