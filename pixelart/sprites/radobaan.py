"""Radobaan, brute wyvern. Uragaan's bone-armored cousin: the rolling
boulder wrapped in pale bone discs with dark gaps between them, bone
spikes bristling radially off the shell, the face buried in a bone plate
with tiny dark eyes, bone spikes on the tail."""
from uragaan import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "radobaan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = {
    ".": (0, 0, 0, 0),
    "K": (24, 20, 22, 255),
    "R": (95, 84, 76, 255),     # dark gray-brown body
    "D": (68, 60, 54, 255),     # darker shade
    "C": (236, 226, 204, 255),  # bone discs and face plate
    "L": (150, 136, 122, 255),  # belly band
    "W": (246, 242, 230, 255),
}

# bone spikes bristling radially off the shell
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(13, 14), (19, 20)],
    4:  [(9, 9), (25, 25)],
    6:  [(6, 6), (7, 27), (28, 28)],
}

CONFIG["fills"] = [
    # big bone disc cap across the back
    ("runs", [(3, 13, 21), (4, 11, 23), (5, 9, 25)], "C"),
    # dark gaps splitting the cap into three discs
    ("runs", [(3, 17, 17), (4, 17, 17), (5, 17, 17)], "D", "C"),
    ("runs", [(4, 21, 21), (5, 21, 21)], "D", "C"),
    # bone color on the radial spikes
    ("runs", [(2, 13, 14), (2, 19, 20), (4, 9, 9), (4, 25, 25),
              (6, 6, 6), (6, 28, 28)], "C"),
    # mud patches on the lower body
    ("runs", [(6, 14, 15), (7, 19, 21), (8, 16, 18)], "D"),
    # bone plate burying the face, continuous with the chin
    ("runs", [(8, 1, 3), (9, 0, 6), (10, 0, 6), (11, 0, 6), (12, 0, 6),
              (13, 1, 4)], "C"),
    # tiny eye and nostril on the bone plate
    ("put", 9, 5, "K"),
    ("put", 11, 6, "K"),
    # belly band along the bottom edge
    ("runs", [(15, 6, 12), (16, 6, 16), (17, 7, 18)], "L"),
    # bone spikes on the tail
    ("runs", [(13, 29, 32), (14, 29, 33)], "C"),
    ("runs", [(14, 31, 32)], "D", "C"),
    # rear leg darker
    ("runs", [(19, 18, 22), (20, 18, 22), (21, 18, 22)], "D"),
    # claws
    ("put", 22, 8, "W"),
    ("put", 22, 10, "W"),
    ("put", 22, 18, "W"),
    ("put", 22, 20, "W"),
]
