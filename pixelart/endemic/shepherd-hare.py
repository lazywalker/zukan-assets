"""Endemic life: shepherd-hare.
Derived from the archetype base; palette carries the species identity."""
from _hare import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shepherd-hare"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (160, 140, 110, 255)
CONFIG["palette"]["D"] = (120, 104, 80, 255)
