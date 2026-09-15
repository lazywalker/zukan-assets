"""Endemic life: wirebug.
Derived from the archetype base; palette carries the species identity."""
from _wirebug import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wirebug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
