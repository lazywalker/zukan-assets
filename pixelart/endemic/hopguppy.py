"""Endemic life: hopguppy.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hopguppy"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 180, 190, 255)
CONFIG["palette"]["D"] = (76, 140, 152, 255)
CONFIG["palette"]["C"] = (210, 236, 236, 255)
