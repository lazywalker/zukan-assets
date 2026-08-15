"""Talioth, bird wyvern. The sleek stalker: a slim tan raptor with a
feather crest, dark stripes down the back, and a long straight tail."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "talioth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (192, 142, 82, 255)   # tan feathers
CONFIG["palette"]["F"] = (156, 110, 60, 255)   # dark crest
CONFIG["palette"]["C"] = (222, 196, 158, 255)  # pale belly
CONFIG["palette"]["S"] = (140, 96, 50, 255)    # dark stripes

# feather crest taller, two rows
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(7, 10)],
    4:  [(6, 11)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # dark stripes down the back
    ("runs", [(8, 14, 15), (9, 16, 17), (10, 18, 19), (11, 20, 21),
              (12, 22, 23)], "S"),
    ("runs", [(3, 7, 10), (4, 6, 11)], "F"),
]
