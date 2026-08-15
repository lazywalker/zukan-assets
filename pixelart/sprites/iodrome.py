"""Iodrome, bird wyvern leader. Purple poison-dog variant with a longer
snout: purple scales, purple frill, orange eye. Derives from great-jaggi
with a longer-snout span patch and palette swap."""
from great_jaggi import CONFIG as _base

CONFIG = {
    "name": "iodrome",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/iodrome.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (145, 90, 155, 255),   # purple scales
        "C": (200, 160, 205, 255),  # pale underbelly
        "F": (120, 70, 130, 255),   # purple frill
        "D": (100, 55, 110, 255),   # dark purple: snout tip, spots
        "S": (100, 55, 110, 255),   # inherited jaggi mouth-line color
        "W": (246, 242, 230, 255),  # eye
    },
    "base": "O",
    "spans": {**_base["spans"],
        6:  [(0, 12), (31, 32)],              # longer snout
        7:  [(0, 12), (30, 33)],
        8:  [(1, 11), (29, 33)],
    },
    "fills": list(_base["fills"]) + [
        # dark snout tip + orange eye over the base spots
        ("runs", [(6, 0, 2), (7, 0, 2)], "D"),
        ("put", 7, 5, "W"),
        ("put", 7, 6, "W"),
    ],
}
