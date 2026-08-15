"""Endemic life: pearlspring-macaque.
Derived from the archetype base; palette carries the species identity."""
from _macaque import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pearlspring-macaque"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (186, 176, 198, 255)
CONFIG["palette"]["D"] = (140, 130, 154, 255)
CONFIG["palette"]["C"] = (232, 226, 240, 255)
