"""Endemic life: vaporonid.
Derived from the archetype base; palette carries the species identity."""
from _jellyfish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "vaporonid"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 160, 200, 255)
CONFIG["palette"]["D"] = (104, 122, 162, 255)
CONFIG["palette"]["G"] = (214, 228, 250, 255)
