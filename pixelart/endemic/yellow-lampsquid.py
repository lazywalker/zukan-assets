"""Endemic life: yellow-lampsquid.
Derived from the archetype base; palette carries the species identity."""
from _lampsquid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "yellow-lampsquid"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (190, 160, 60, 255)
CONFIG["palette"]["D"] = (148, 122, 42, 255)
CONFIG["palette"]["L"] = (248, 226, 120, 255)
