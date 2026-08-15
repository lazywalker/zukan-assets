"""Velocidrome, bird wyvern leader. The sprinter of the great-jaggi
family: blue scales, the head carried low and forward in a lunge with a
long jaw reaching the frame edge, a small flat crest, straight tail.
Differs from jaggi by the lowered lunging head and long jaw."""
from great_jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "velocidrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (90, 130, 180, 255)   # blue scales
CONFIG["palette"]["F"] = (130, 160, 200, 255)  # blue frill
CONFIG["palette"]["C"] = (200, 215, 230, 255)  # pale belly
CONFIG["palette"]["S"] = (55, 80, 120, 255)    # spots / shade

# lunging pose: no tall frill, head low and jaw stretched forward
CONFIG["spans"] = {
    **_base["spans"],
    3:  [],
    4:  [(8, 11)],
    5:  [(6, 12)],
    6:  [(0, 12), (31, 32)],
    7:  [(0, 12), (30, 33)],
    8:  [(1, 11), (29, 33)],
}

CONFIG["fills"] = [
    # small flat crest
    ("runs", [(4, 8, 11)], "F"),
    # long cream jaw
    ("runs", [(6, 0, 3), (7, 0, 3)], "C"),
    # dark mouth line
    ("runs", [(8, 1, 3)], "S"),
    # eye, set high on the lowered head
    ("put", 6, 5, "W"),
    # dark spots on the body
    ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22), (14, 12, 13),
              (14, 23, 24)], "S"),
    # cream underbelly
    ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)],
     "C"),
    # frill spikes on the tail top
    ("runs", [(9, 24, 25), (10, 26, 27), (11, 27, 28)], "F"),
    # tail underside shade
    ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
     "S"),
    # claws
    ("put", 21, 10, "W"),
    ("put", 21, 12, "W"),
    ("put", 21, 18, "W"),
    ("put", 21, 20, "W"),
]
