"""Endemic life: quetzalcobra.
Derived from the archetype base; palette carries the species identity."""
from _cobra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "quetzalcobra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 160, 140, 255)
CONFIG["palette"]["D"] = (64, 120, 104, 255)
CONFIG["palette"]["H"] = (170, 220, 190, 255)
CONFIG["palette"]["G"] = (230, 250, 210, 255)

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(6, 5, 6), (7, 4, 5), (8, 3, 4)], "G", "H"),
]
