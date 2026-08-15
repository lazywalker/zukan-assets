"""Wroggi, small bird wyvern. The rose pack hunter: great-wroggi's palette
on the small lunge frame, tail raised and curled, orange poison sacs on
the neck."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wroggi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (200, 105, 100, 255)  # rose scales
CONFIG["palette"]["C"] = (230, 185, 175, 255)  # pale belly
CONFIG["palette"]["S"] = (150, 66, 62, 255)    # dark spots
CONFIG["palette"]["Y"] = (232, 172, 60, 255)   # orange poison sacs

# raised curled tail like the leader
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(0, 12), (30, 32)],
    7:  [(0, 12), (29, 33)],
    8:  [(1, 11), (28, 33)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # orange poison sacs on the neck
    ("runs", [(8, 10, 11), (9, 10, 12)], "Y"),
    ("put", 8, 10, "Y"),
]
