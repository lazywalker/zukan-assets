"""Endemic life: moon-slug.
Derived from the archetype base; palette carries the species identity."""
from _slug import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "moon-slug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (210, 214, 230, 255)
CONFIG["palette"]["D"] = (170, 176, 198, 255)
CONFIG["palette"]["C"] = (236, 238, 246, 255)
