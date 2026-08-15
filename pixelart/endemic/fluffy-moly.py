"""Endemic life: fluffy-moly.
Derived from the archetype base; palette carries the species identity."""
from _moly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "fluffy-moly"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (238, 232, 216, 255)
CONFIG["palette"]["D"] = (198, 190, 172, 255)
