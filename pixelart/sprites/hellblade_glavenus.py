"""Hellblade Glavenus, glavenus deviant. The burning blade: charcoal body,
crimson crown, and the tail blade wreathed in fire with a flame burst off
its top edge."""
from glavenus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hellblade-glavenus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (62, 54, 60, 255)     # charcoal body
CONFIG["palette"]["D"] = (44, 38, 44, 255)     # darker charcoal
CONFIG["palette"]["N"] = (178, 52, 44, 255)    # crimson crown / plates
CONFIG["palette"]["B"] = (238, 122, 42, 255)   # burning blade
CONFIG["palette"]["E"] = (250, 190, 70, 255)   # fire core

# flame burst off the blade's top edge
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(23, 26)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # fire core along the blade and the burst
    ("runs", [(3, 23, 26), (4, 25, 26), (5, 24, 26), (6, 22, 24),
              (7, 20, 21)], "E", "B"),
]
