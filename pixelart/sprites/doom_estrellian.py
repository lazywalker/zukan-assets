"""Doom Estrellian, estrellian variant. The black doom: crimson-black hide
with red star spots, and the crescent horns grown into long cruel
scythes with a fanged jaw."""
from estrellian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "doom-estrellian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (52, 40, 52, 255)     # crimson-black hide
CONFIG["palette"]["D"] = (36, 28, 38, 255)     # darkest hide
CONFIG["palette"]["R"] = (222, 84, 66, 255)    # red scythe horns
CONFIG["palette"]["r"] = (170, 50, 44, 255)    # darker far horn
CONFIG["palette"]["Y"] = (222, 84, 66, 255)    # red star spots

# scythe horns grown one row taller, plus a fang under the snout
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 5)],
    2:  [(3, 5)],
    6:  [(0, 8), (8, 13)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the taller horn reaches the extra row
    ("runs", [(1, 4, 5), (2, 3, 5)], "R"),
    ("put", 6, 8, "W"),
]
