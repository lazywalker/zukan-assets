"""Endemic life: goldenfry.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "goldenfry"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (236, 196, 70, 255)
CONFIG["palette"]["D"] = (200, 150, 40, 255)
CONFIG["palette"]["C"] = (248, 230, 150, 255)
