"""Apceros, herbivore. The shelled grazer, drawn in the dome front of its
icon: a brown shell dome with pale spikes sticking out around the rim, a
cream frilled face peeking out below, and stubby legs."""

CONFIG = {
    "name": "apceros",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/apceros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (140, 100, 60, 255),    # brown shell
        "D": (100, 68, 40, 255),     # dark shell shade
        "C": (222, 200, 160, 255),   # pale spikes / face
        "E": (60, 40, 30, 255),      # dark face shade
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(8, 8), (14, 15), (21, 21)],        # spike tips
        3:  [(6, 9), (13, 16), (20, 23)],
        4:  [(5, 10), (12, 17), (19, 24)],
        5:  [(4, 11), (11, 18), (18, 25)],
        6:  [(4, 25)],                           # shell
        7:  [(3, 26)],
        8:  [(3, 26)],
        9:  [(3, 26)],
        10: [(3, 26)],
        11: [(4, 25)],                           # shell rim
        12: [(5, 24), (10, 19)],                 # rim + face top
        13: [(5, 24), (10, 19)],
        14: [(6, 23), (10, 19)],
        15: [(6, 23), (11, 18)],                 # face base
        16: [(7, 22)],
        17: [(8, 10), (13, 16), (19, 21)],       # legs
        18: [(8, 10), (13, 16), (19, 21)],
    },
    "fills": [
        # pale spikes around the shell rim
        ("runs", [(2, 8, 8), (2, 14, 15), (2, 21, 21), (3, 6, 7),
                  (3, 13, 14), (3, 16, 16), (3, 22, 23), (4, 5, 6),
                  (4, 13, 14), (4, 23, 24), (5, 4, 5), (5, 24, 25)],
         "C", "B"),
        # shell dome shading
        ("runs", [(4, 10, 11), (5, 8, 10), (6, 4, 8), (7, 3, 7),
                  (8, 3, 7), (9, 3, 7), (10, 3, 7), (4, 18, 19),
                  (5, 19, 21), (6, 21, 25), (7, 22, 26), (8, 22, 26),
                  (9, 22, 26), (10, 22, 26)], "D", "B"),
        # pale scute lines across the shell
        ("runs", [(6, 12, 17), (7, 11, 18), (8, 11, 18), (9, 11, 18),
                  (10, 11, 18)], "C", "B"),
        ("runs", [(6, 14, 15), (8, 14, 15), (10, 14, 15)], "D", "C"),
        # cream frilled face with dark eyes
        ("runs", [(12, 10, 19), (13, 10, 19), (14, 10, 19), (15, 11, 18)],
         "C", "B"),
        ("put", 13, 12, "K"),
        ("put", 13, 17, "K"),
        # dark beak line
        ("runs", [(14, 13, 16)], "E", "C"),
        # dark legs with pale claws
        ("runs", [(17, 8, 10), (17, 19, 21), (18, 8, 10), (18, 19, 21),
                  (17, 13, 16), (18, 13, 16)], "D"),
        ("put", 18, 8, "W"),
        ("put", 18, 21, "W"),
    ],
}
