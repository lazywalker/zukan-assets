"""Endemic life: escuregot.
Derived from the archetype base; palette carries the species identity."""
from _snail import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "escuregot"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 130, 90, 255)
CONFIG["palette"]["D"] = (80, 98, 66, 255)
CONFIG["palette"]["C"] = (214, 222, 172, 255)
