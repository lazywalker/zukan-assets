"""Duffel penguine: a penguin carrying a brown duffel bag on its back."""
from _penguin import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "duffel-penguine"
CONFIG["size"] = (28, 24)
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (150, 104, 62, 255)   # duffel bag
CONFIG["palette"]["s"] = (114, 76, 44, 255)    # bag shade

CONFIG["spans"] = {
    **_base["spans"],
    4: [(12, 15)],
    5: [(10, 17)],
    6: [(8, 18)],
    7: [(7, 19)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the duffel bag riding on the back
    ("runs", [(4, 12, 15), (5, 10, 17), (6, 8, 18), (7, 7, 18)], "S"),
    ("runs", [(5, 12, 14), (6, 10, 11), (6, 16, 17)], "s"),
    # bag strap
    ("put", 8, 8, "s"),
    ("put", 9, 7, "s"),
]
