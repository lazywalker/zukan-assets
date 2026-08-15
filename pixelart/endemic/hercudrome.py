"""Hercudrome: a rhinoceros beetle with a big branching horn on its head.
Gold and prism variants share this skeleton."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hercudrome"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (90, 80, 120, 255)    # violet shell
CONFIG["palette"]["D"] = (64, 56, 90, 255)     # darker
CONFIG["palette"]["C"] = (222, 190, 120, 255)  # pale horn

CONFIG["spans"] = {
    **_base["spans"],
    4: [(14, 20)],
    5: [(13, 21)],
    6: [(9, 13), (16, 22)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the big pale horn
    ("runs", [(4, 14, 20), (5, 13, 21), (6, 16, 22)], "C"),
    ("put", 6, 13, "D"),
]
