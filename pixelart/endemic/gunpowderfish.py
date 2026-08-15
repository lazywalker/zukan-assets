"""Endemic life: gunpowderfish.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gunpowderfish"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (70, 74, 86, 255)
CONFIG["palette"]["D"] = (48, 52, 62, 255)
CONFIG["palette"]["C"] = (110, 114, 126, 255)
CONFIG["palette"]["G"] = (230, 140, 60, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(9, 28, 29), (10, 28, 29), (11, 28, 29)], "G", "D"),
]
