"""Endemic life: climbing-joyperch.
Derived from the archetype base; palette carries the species identity."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "climbing-joyperch"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 140, 70, 255)
CONFIG["palette"]["D"] = (160, 104, 48, 255)
CONFIG["palette"]["C"] = (230, 190, 130, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 9, 10), (12, 11, 12), (14, 10, 11), (16, 12, 13)], "K", "B"),
]
