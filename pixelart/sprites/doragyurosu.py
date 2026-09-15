"""Doragyurosu, bird wyvern. The pale sickle: malfestio's owl frame in
moonlight white with gold sickle wings swept one row higher."""
from malfestio import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "doragyurosu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (222, 218, 206, 255)  # moonlight plumage
CONFIG["palette"]["D"] = (168, 162, 146, 255)  # darker plumage
CONFIG["palette"]["Y"] = (222, 178, 82, 255)   # gold collar / sickles
CONFIG["palette"]["E"] = (108, 98, 78, 255)    # dark tan face

# gold sickle wings swept one row higher
CONFIG["spans"] = {
    **_base["spans"],
    10: [(4, 6), (25, 27)],
    11: [(4, 7), (24, 27)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(10, 4, 6), (10, 25, 27), (11, 4, 7), (11, 24, 27)], "Y"),
]
