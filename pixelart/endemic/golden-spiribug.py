"""Endemic life: golden-spiribug.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "golden-spiribug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (200, 170, 70, 255)
CONFIG["palette"]["D"] = (152, 128, 50, 255)
CONFIG["palette"]["G"] = (255, 236, 150, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 16, 22), (11, 15, 23)], "G", "D"),
]
