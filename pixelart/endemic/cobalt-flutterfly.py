"""Endemic life: cobalt-flutterfly.
Derived from the archetype base; palette carries the species identity."""
from _butterfly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "cobalt-flutterfly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 120, 190, 255)
CONFIG["palette"]["D"] = (62, 86, 146, 255)
