"""Cactuar cutting: a tiny cactus sprout with a face."""
from cactuar import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "cactuar-cutting"
CONFIG["size"] = (16, 24)

CONFIG["spans"] = {
    **_base["spans"],
    4:  [(6, 9)],
    5:  [(6, 10)],
    6:  [(6, 10)],
    7:  [(5, 11)],
    8:  [(5, 11)],
    9:  [(5, 11)],
    10: [(5, 11)],
    11: [(5, 11)],
    12: [(5, 11)],
    13: [(5, 11)],
    14: [(5, 11)],
    15: [(5, 11)],
    16: [(6, 10)],
    17: [(7, 8), (10, 10)],
    18: [(7, 7), (10, 10)],
}

CONFIG["fills"] = [
    # face dots (the tiny face has room for one eye)
    ("put", 7, 11, "B"),
    ("runs", [(9, 11, 11)], "B"),
    # left spines only (the canvas is narrower than the parent's)
    ("runs", [(9, 8, 8), (11, 8, 8), (13, 8, 8)], "W"),
    # right edge shading
    ("runs", [(7, 9, 11), (9, 11, 11), (11, 11, 11), (13, 11, 11)], "D"),
]
