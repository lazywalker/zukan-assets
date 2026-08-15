"""Arbiter Estrellian, estrellian variant. The white judge: pale silver
hide with gold star spots, and the shoulder wing grown into a tall
two-pointed fan with a gold halo spark above it."""
from estrellian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "arbiter-estrellian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (196, 194, 188, 255)  # pale silver hide
CONFIG["palette"]["D"] = (158, 156, 150, 255)  # darker silver
CONFIG["palette"]["R"] = (236, 178, 88, 255)   # gold horns
CONFIG["palette"]["r"] = (206, 150, 70, 255)   # darker far horn
CONFIG["palette"]["Y"] = (236, 178, 88, 255)   # gold star spots

# wing fan grown into one tall gold point
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(3, 5), (8, 9), (11, 13)],
    4:  [(2, 5), (7, 14)],
    5:  [(1, 6), (7, 14)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the tall wing point gilded like a halo blade
    ("runs", [(3, 11, 13), (4, 11, 14), (5, 11, 14)], "Y"),
    ("runs", [(4, 7, 10), (5, 7, 10)], "D"),
]
