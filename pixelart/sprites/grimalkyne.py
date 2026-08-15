"""Grimalkyne, lynian. The wild cat: felyne's frame in a scruffier grey
coat with a leaf skirt shawl, hunched ears wider apart."""
from felyne import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "grimalkyne"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (168, 160, 148, 255)  # scruffy grey fur
CONFIG["palette"]["D"] = (132, 124, 112, 255)  # darker fur
CONFIG["palette"]["N"] = (52, 62, 44, 255)     # dark ear tips
CONFIG["palette"]["R"] = (120, 160, 84, 255)   # leaf green shawl

# leaf shawl across the shoulders
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(2, 17), (17, 18)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(9, 3, 15)], "R"),
]
