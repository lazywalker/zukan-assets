"""Endemic life: wailnard.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wailnard"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (214, 160, 150, 255)
CONFIG["palette"]["D"] = (170, 118, 110, 255)
CONFIG["palette"]["C"] = (240, 208, 200, 255)
