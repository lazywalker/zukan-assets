"""Endemic life: pilot-hare.
Derived from the archetype base; palette carries the species identity."""
from _hare import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pilot-hare"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (180, 170, 150, 255)
CONFIG["palette"]["D"] = (136, 126, 108, 255)
