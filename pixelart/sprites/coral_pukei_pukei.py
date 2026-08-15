"""Coral Pukei-Pukei, pukei-pukei subspecies. Cream body, coral-pink face
rim, and the signature oversized coral fan tail: one row taller than the
base bird's fins, with the cyan water tongue kept."""
from pukei_pukei import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "coral-pukei-pukei"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (225, 212, 195, 255)  # cream body
CONFIG["palette"]["R"] = (222, 120, 118, 255)  # coral face rim / tail fins
CONFIG["palette"]["L"] = (238, 198, 190, 255)  # pale rose belly
CONFIG["palette"]["T"] = (115, 190, 205, 255)  # cyan water tongue

# oversized fan tail: top edge pushed up and out
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(2, 9), (11, 15)],
    10: [(3, 10), (11, 17)],
    11: [(4, 11), (12, 19)],
    12: [(4, 12), (13, 20)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # coral color over the enlarged fan top
    ("runs", [(9, 12, 15), (10, 13, 16), (11, 14, 15)], "R"),
]
