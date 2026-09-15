"""Endemic life: thunderbeetle.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "thunderbeetle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (60, 66, 90, 255)
CONFIG["palette"]["D"] = (42, 46, 68, 255)
CONFIG["palette"]["G"] = (240, 210, 90, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 8, 20), (12, 6, 21), (14, 8, 20)], "G", "B"),
]
