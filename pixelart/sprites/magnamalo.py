"""Magnamalo, fanged wyvern. The armored samurai tiger: hunched purple
quadruped on the zinogre frame, gold plating on horns, back, shoulder and
hip, a gaping fanged jaw, and the tail swept up with a flame-orange tip."""

CONFIG = {
    "name": "magnamalo",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/magnamalo.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (105, 62, 122, 255),   # purple armor body
        "D": (74, 40, 90, 255),     # darker purple shade
        "G": (235, 190, 80, 255),   # gold plating
        "F": (232, 92, 58, 255),    # flame orange
        "W": (245, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        1:  [(3, 4), (7, 8)],                 # horn tips
        2:  [(2, 5), (6, 9), (28, 29)],       # horns + tail tip spike
        3:  [(1, 10), (14, 15), (18, 19), (26, 29)],
        4:  [(1, 11), (13, 22), (24, 30)],
        5:  [(1, 12), (12, 23), (23, 31)],
        6:  [(0, 12), (12, 23), (24, 30)],    # snout to col 0
        7:  [(0, 12), (12, 30)],
        8:  [(4, 8), (10, 26)],               # mouth gap cols 0-3
        9:  [(2, 26)],
        10: [(9, 25)],
        11: [(9, 25)],
        12: [(10, 25)],
        13: [(10, 25)],
        14: [(10, 24)],
        15: [(10, 22)],
        16: [(11, 20)],
        17: [(12, 15), (19, 22)],
        18: [(12, 15), (19, 22)],
        19: [(12, 14), (19, 21)],
        20: [(12, 14), (19, 21)],
        21: [(11, 13), (19, 21)],
        22: [(11, 11), (13, 13), (19, 19), (21, 21)],
    },
    "fills": [
        # gold horns, taller than zinogre's crown
        ("runs", [(1, 3, 4), (1, 7, 8), (2, 2, 5), (2, 6, 9), (3, 1, 9)],
         "G"),
        # back spikes gold
        ("runs", [(3, 14, 15), (3, 18, 19), (4, 13, 13), (4, 17, 17),
                  (4, 20, 21), (5, 12, 22)], "G"),
        # shoulder + foreleg plates
        ("runs", [(9, 14, 18), (10, 12, 17), (11, 12, 17), (12, 12, 17),
                  (13, 12, 16), (14, 12, 15), (15, 12, 15)], "G"),
        ("runs", [(16, 12, 15)], "D"),
        # hip plate
        ("runs", [(9, 21, 25), (10, 21, 25), (11, 21, 25)], "G"),
        ("runs", [(12, 22, 25)], "D"),
        # tail: gold edge, flame-orange tip
        ("runs", [(2, 28, 29), (3, 27, 29), (4, 26, 28), (5, 25, 28),
                  (6, 28, 30), (7, 27, 30)], "G"),
        ("runs", [(2, 28, 29), (3, 28, 29)], "F"),
        # gaping jaw: fangs + dark gape
        ("put", 7, 0, "W"),
        ("put", 8, 1, "W"),
        ("put", 8, 3, "W"),
        # eye
        ("put", 5, 2, "F"),
        # belly shade
        ("runs", [(14, 10, 11), (15, 10, 13), (16, 11, 14)], "D"),
        ("runs", [(14, 22, 24), (15, 20, 23)], "D"),
        # claws
        ("put", 22, 11, "W"),
        ("put", 22, 13, "W"),
        ("put", 22, 19, "W"),
        ("put", 22, 21, "W"),
    ],
}
