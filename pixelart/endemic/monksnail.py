"""Endemic life: monksnail.
Derived from the archetype base; palette carries the species identity."""
from _snail import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "monksnail"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 110, 150, 255)
CONFIG["palette"]["D"] = (112, 82, 112, 255)
CONFIG["palette"]["C"] = (196, 208, 150, 255)
