"""Paratoad: a pale toad covered in raised pustules; pop them for paralysis."""
from _toad import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "paratoad"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (196, 168, 150, 255)  # pale toad skin
CONFIG["palette"]["D"] = (150, 122, 106, 255)  # darker
CONFIG["palette"]["C"] = (234, 214, 194, 255)  # belly
CONFIG["palette"]["G"] = (240, 170, 110, 255)  # pustules

CONFIG["spans"] = {
    **_base["spans"],
    6: [(9, 11), (14, 16), (18, 19)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # raised pustules along the back
    ("runs", [(6, 9, 11), (6, 14, 16), (6, 18, 19)], "G"),
    ("put", 10, 8, "G"),
    ("put", 11, 13, "G"),
    ("put", 10, 17, "G"),
    ("put", 12, 11, "G"),
]
