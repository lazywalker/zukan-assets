"""Endemic life: goldspring-macaque.
Derived from the archetype base; palette carries the species identity."""
from _macaque import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "goldspring-macaque"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 160, 80, 255)
CONFIG["palette"]["D"] = (152, 118, 56, 255)
CONFIG["palette"]["C"] = (240, 216, 160, 255)
