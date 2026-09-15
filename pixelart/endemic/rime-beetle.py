"""Endemic life: rime-beetle.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rime-beetle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 180, 200, 255)
CONFIG["palette"]["D"] = (112, 144, 168, 255)
CONFIG["palette"]["C"] = (224, 238, 246, 255)
