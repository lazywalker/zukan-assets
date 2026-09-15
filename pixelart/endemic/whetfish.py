"""Endemic life: whetfish.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "whetfish"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 150, 158, 255)
CONFIG["palette"]["D"] = (110, 110, 120, 255)
CONFIG["palette"]["C"] = (208, 196, 168, 255)
CONFIG["palette"]["S"] = (216, 196, 150, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(8, 6, 19), (9, 4, 19), (10, 4, 19)], "S", "B"),
]
