"""Endemic life: petricanths.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "petricanths"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 136, 128, 255)
CONFIG["palette"]["D"] = (104, 100, 94, 255)
CONFIG["palette"]["C"] = (180, 176, 168, 255)
