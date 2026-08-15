"""Endemic life: gilded-spiribug.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gilded-spiribug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (170, 150, 70, 255)
CONFIG["palette"]["D"] = (128, 112, 50, 255)
CONFIG["palette"]["G"] = (250, 220, 120, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 16, 22), (11, 15, 23)], "G", "D"),
]
