"""Endemic life: phantom-flutterfly.
Derived from the archetype base; palette carries the species identity."""
from _butterfly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "phantom-flutterfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 120, 170, 255)
CONFIG["palette"]["D"] = (104, 88, 132, 255)
CONFIG["palette"]["W"] = (222, 210, 240, 255)
