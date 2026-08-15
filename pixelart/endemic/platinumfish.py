"""Endemic life: platinumfish.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "platinumfish"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 204, 210, 255)
CONFIG["palette"]["D"] = (160, 164, 172, 255)
CONFIG["palette"]["C"] = (240, 240, 242, 255)
