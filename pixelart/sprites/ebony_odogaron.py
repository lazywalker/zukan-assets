"""Ebony Odogaron, fanged wyvern subspecies. The blackened hound: dark
grey armor over the odogaron frame, ears taller, and hackles bristling
up along the back."""
from odogaron import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ebony-odogaron"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (72, 66, 76, 255)     # dark grey body
CONFIG["palette"]["D"] = (48, 44, 52, 255)     # darker stripes

# taller ears + hackle spikes along the back
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(2, 3), (6, 7)],
    9:  [(1, 8), (11, 11), (14, 14), (17, 17)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # hackles
    ("runs", [(9, 11, 11), (9, 14, 14), (9, 17, 17)], "D"),
]
