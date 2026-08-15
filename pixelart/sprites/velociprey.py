"""Velociprey, bird wyvern. The blue raptor (velocidrome's pack member):
hunched running pose with an arched back bump, raised tail, small crest.
Derives from velocidrome's lunge but hunches up instead."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "velociprey"
CONFIG["compare_to"] = "../icons/mh4u/velociprey.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (110, 140, 185, 255)  # blue raptor scales
CONFIG["palette"]["S"] = (60, 85, 130, 255)    # darker stripes

# hunched run: arched back, raised tail, smaller crest
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(9, 11)],
    6:  [(0, 12), (30, 33)],
    7:  [(0, 12), (29, 33)],
    8:  [(1, 11), (12, 26), (28, 33)],
    9:  [(3, 12), (13, 27), (28, 32)],
    10: [(5, 13), (14, 28), (27, 31)],
    11: [(6, 14), (15, 29)],
}

CONFIG["fills"] = [
    # small flat crest
    ("runs", [(4, 9, 11)], "F"),
    # cream jaw
    ("runs", [(6, 0, 3), (7, 0, 3)], "C"),
    # dark mouth line
    ("runs", [(8, 1, 3)], "S"),
    # eye
    ("put", 6, 5, "W"),
    # darker stripes over the arched back
    ("runs", [(8, 16, 17), (8, 21, 22), (9, 19, 20), (9, 24, 25),
              (10, 22, 23)], "S"),
    # cream underbelly
    ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)],
     "C"),
    # frill spikes along the raised tail top
    ("runs", [(7, 30, 31), (8, 30, 31), (9, 29, 30)], "F"),
    # tail underside shade
    ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
     "S"),
    # claws
    ("put", 21, 10, "W"),
    ("put", 21, 12, "W"),
    ("put", 21, 18, "W"),
    ("put", 21, 20, "W"),
]
