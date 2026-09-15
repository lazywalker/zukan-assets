"""Endemic life: woodland-pteryx.
Derived from the archetype base; palette carries the species identity."""
from _raptor import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "woodland-pteryx"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 120, 80, 255)
CONFIG["palette"]["D"] = (104, 88, 56, 255)
