"""Ioprey, bird wyvern. The red-orange raptor (iodrome's pack member):
crestless head with a bulging poison sac under the chin. Derives from
velocidrome but drops the crest and swells the throat."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ioprey"
CONFIG["compare_to"] = "../icons/mh4u/ioprey.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (246, 242, 230, 255)   # white belly / glints
CONFIG["palette"]["O"] = (190, 110, 80, 255)   # red-orange scales
CONFIG["palette"]["F"] = (210, 130, 100, 255)  # frill
CONFIG["palette"]["S"] = (140, 70, 50, 255)    # darker stripes

# crestless head with a swollen throat bulging down-forward
CONFIG["spans"] = {
    **_base["spans"],
    3:  [],
    4:  [],
    5:  [(7, 12)],
    6:  [(1, 12), (31, 32)],
    7:  [(0, 12), (30, 33)],
    8:  [(0, 12), (29, 33)],
    9:  [(0, 12), (13, 25), (29, 32)],
    10: [(1, 13), (14, 26), (28, 31)],
}

CONFIG["fills"] = [
    # cream muzzle
    ("runs", [(7, 0, 3), (8, 0, 2)], "C"),
    # dark mouth line
    ("runs", [(8, 1, 2)], "S"),
    # eye
    ("put", 7, 6, "W"),
    # orange poison sac glowing on the throat
    ("runs", [(8, 3, 4), (9, 1, 3), (10, 2, 4)], "F"),
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
