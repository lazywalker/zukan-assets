"""Doragyurosu, bird wyvern. The pale sickle: malfestio's owl frame in
moonlight white with gold sickle wings."""
from malfestio import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "doragyurosu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (222, 218, 206, 255)  # moonlight plumage
CONFIG["palette"]["D"] = (168, 162, 146, 255)  # darker plumage
CONFIG["palette"]["O"] = (222, 178, 82, 255)   # gold chest collar
CONFIG["palette"]["N"] = (108, 98, 78, 255)    # dark tufts / bars

# gold sickle wings swept higher
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(12, 13)],
    2:  [(5, 6), (12, 14)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the raised sickle tips gilded
    ("runs", [(1, 12, 13), (2, 12, 14)], "O"),
]
