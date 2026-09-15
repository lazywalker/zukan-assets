"""Radobaan, brute wyvern. Uragaan's bone-armored cousin: the rolling
boulder wrapped in pale bone discs split by dark gaps, bone spikes
bristling off the shell rim, the face buried in a bone plate with tiny
dark eyes, and a pale belly band."""
from uragaan import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "radobaan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = {
    ".": (0, 0, 0, 0),
    "K": (24, 20, 22, 255),
    "B": (95, 84, 76, 255),     # dark gray-brown body
    "D": (68, 60, 54, 255),     # darker shade
    "C": (236, 226, 204, 255),  # bone discs and face plate
    "L": (150, 136, 122, 255),  # belly band
    "W": (246, 242, 230, 255),
}
CONFIG["base"] = "B"

# bone spikes bristling off the shell rim
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(15, 15), (18, 18)],
    5:  [(8, 8), (9, 24), (25, 25)],
    7:  [(6, 6), (7, 26), (27, 27)],
    9:  [(4, 4), (5, 28), (29, 29)],
}

CONFIG["fills"] = [
    # bone disc cap across the whole dome
    ("runs", [(2, 14, 19), (3, 12, 21), (4, 10, 23), (5, 9, 24),
              (6, 8, 25), (7, 7, 26), (8, 6, 27), (9, 5, 28)], "C"),
    # dark gaps splitting the cap into three discs
    ("runs", [(2, 16, 16), (3, 15, 16), (4, 15, 15), (2, 19, 19),
              (3, 20, 21), (4, 21, 21)], "D", "C"),
    ("runs", [(5, 13, 13), (6, 12, 12), (7, 11, 11), (5, 22, 22),
              (6, 23, 23), (7, 24, 24)], "D", "C"),
    # bone color on the radial spikes
    ("runs", [(1, 15, 15), (1, 18, 18), (5, 8, 8), (5, 25, 25),
              (7, 6, 6), (7, 27, 27), (9, 4, 4), (9, 29, 29)], "C"),
    # mud patches on the lower dome
    ("runs", [(8, 12, 14), (8, 20, 22), (9, 14, 15), (9, 18, 19)], "D",
     "C"),
    # bone plate burying the face, continuous with the chin
    ("runs", [(10, 5, 28), (11, 4, 29), (12, 4, 29), (13, 4, 29)], "C"),
    # tiny eyes and nostrils on the bone plate
    ("put", 11, 12, "K"),
    ("put", 11, 21, "K"),
    ("put", 12, 15, "D"),
    ("put", 12, 18, "D"),
    # dark jaw slit under the plate
    ("runs", [(13, 10, 23)], "D", "C"),
    # pale belly band along the bottom edge
    ("runs", [(15, 6, 27), (16, 5, 28), (17, 6, 27)], "L"),
    # stubby dark legs with pale claws
    ("runs", [(19, 8, 12), (19, 21, 25), (20, 8, 12), (20, 21, 25),
              (21, 8, 11), (21, 22, 25), (19, 16, 17), (20, 16, 17)],
     "D"),
    ("put", 21, 9, "W"),
    ("put", 21, 11, "W"),
    ("put", 21, 22, "W"),
    ("put", 21, 24, "W"),
]
