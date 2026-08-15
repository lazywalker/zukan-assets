"""Banbaro, brute wyvern. The moose: giant two-pronged antlers sweeping
up and back from a small dark head, a bulky navy-blue body with a cream
belly band, thick legs, short tail."""

CONFIG = {
    "name": "banbaro",
    "size": (40, 24),
    "compare_to": "../icons/mhwi/banbaro.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (62, 74, 112, 255),    # navy-blue body
        "D": (44, 54, 86, 255),     # darker shade
        "C": (216, 208, 190, 255),  # cream belly band / antler inner
        "H": (90, 80, 92, 255),     # antler dark
        "O": (225, 150, 70, 255),   # eye
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        1:  [(3, 7), (15, 19)],               # antler prong tips
        2:  [(2, 8), (14, 20)],
        3:  [(2, 9), (13, 21)],
        4:  [(2, 10), (13, 20)],
        5:  [(2, 9), (12, 19)],               # antler bases + head top
        6:  [(1, 13), (10, 22)],
        7:  [(0, 14), (10, 25)],              # muzzle + back
        8:  [(0, 15), (9, 27)],
        9:  [(1, 16), (9, 28)],
        10: [(2, 30)],
        11: [(3, 31)],
        12: [(4, 32)],
        13: [(4, 32)],
        14: [(5, 31)],
        15: [(6, 30)],
        16: [(7, 29)],
        17: [(9, 13), (17, 21), (25, 28)],    # legs
        18: [(9, 13), (17, 21), (25, 28)],
        19: [(9, 12), (18, 20), (25, 27)],
        20: [(9, 12), (18, 20), (25, 27)],
        21: [(9, 9), (11, 11), (18, 18), (20, 20), (25, 25), (27, 27)],
    },
    "fills": [
        # dark antler palms, split by a clear gap down to the skull
        ("runs", [(1, 3, 7), (2, 2, 8), (3, 2, 9), (4, 2, 10),
                  (5, 2, 7)], "H"),
        ("runs", [(1, 15, 19), (2, 14, 20), (3, 13, 21), (4, 13, 20),
                  (5, 12, 19)], "H"),
        ("runs", [(2, 4, 6), (3, 4, 6), (2, 16, 18), (3, 15, 18),
                  (4, 15, 17)], "C", "H"),
        # orange eye on the dark head
        ("put", 6, 3, "O"),
        # dark muzzle tip
        ("runs", [(7, 0, 2), (8, 0, 2)], "D"),
        # cream belly band along the bottom edge
        ("runs", [(13, 5, 24), (14, 6, 24), (15, 7, 23), (16, 8, 22)],
         "C"),
        # back shade
        ("runs", [(9, 12, 26), (10, 14, 28), (11, 16, 29)], "D"),
        # legs darker
        ("runs", [(17, 17, 21), (18, 17, 21), (19, 18, 20),
                  (20, 18, 20)], "D"),
        ("runs", [(17, 25, 28), (18, 25, 28), (19, 25, 27),
                  (20, 25, 27)], "D"),
        # claws
        ("put", 21, 9, "W"),
        ("put", 21, 11, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 20, "W"),
        ("put", 21, 25, "W"),
        ("put", 21, 27, "W"),
    ],
}
