"""Genprey, bird wyvern. The yellow-green raptor (gendrome's pack
member): crestless drooping head carried low, sniffing the ground.
Derives from velocidrome but drops the crest and lowers the head."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "genprey"
CONFIG["compare_to"] = "../icons/mh4u/genprey.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (246, 242, 230, 255)   # white belly / glints
CONFIG["palette"]["O"] = (170, 180, 90, 255)   # yellow-green scales
CONFIG["palette"]["F"] = (190, 200, 120, 255)  # frill
CONFIG["palette"]["S"] = (125, 130, 60, 255)   # darker stripes

# crestless grazing pose: head mass drops one row, snout at row 7
CONFIG["spans"] = {
    **_base["spans"],
    3:  [],
    4:  [],
    5:  [(7, 12)],
    6:  [(1, 13), (31, 32)],
    7:  [(0, 13), (30, 33)],
    8:  [(1, 12), (29, 33)],
    9:  [(3, 12), (13, 25), (29, 32)],
}

CONFIG["fills"] = [
    # cream muzzle, drooped low
    ("runs", [(7, 0, 3), (8, 1, 3)], "C"),
    # dark mouth line
    ("runs", [(8, 1, 2)], "S"),
    # eye, low on the drooped head
    ("put", 7, 6, "W"),
    # darker stripes on the body
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
