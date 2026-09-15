"""Gobul, leviathan. The anglerfish puffer, drawn face-planted like its
icon: a brown-red spiky dome with pale bone spines and small yellow eyes
on top, and a huge dark mouth filling the lower half, ringed by a pale
rim with pale teeth and a dark tongue."""

CONFIG = {
    "name": "gobul",
    "size": (34, 24),
    "compare_to": "../icons/mh3u/gobul.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "C": (228, 218, 206, 255),   # pale rim / bone spines
        "B": (150, 84, 60, 255),     # brown-red dome
        "D": (120, 45, 52, 255),     # dark red tongue / shade
        "E": (40, 20, 24, 255),      # mouth interior
        "Y": (240, 210, 70, 255),    # yellow lure / eyes
        "W": (246, 242, 230, 255),
    },
    "base": "C",
    "spans": {
        0:  [(16, 17)],                          # lure bulb
        1:  [(16, 17)],                          # stalk
        2:  [(11, 11), (13, 20), (22, 22)],      # spines + dome top
        3:  [(9, 10), (11, 22), (23, 24)],
        4:  [(7, 8), (10, 23), (25, 26)],
        5:  [(6, 6), (9, 24), (27, 27)],
        6:  [(8, 25)],
        7:  [(7, 26)],
        8:  [(6, 27)],                           # dome base / upper jaw
        9:  [(5, 28)],                           # mouth opens
        10: [(5, 28)],
        11: [(4, 29)],
        12: [(4, 29), (1, 2), (31, 32)],         # side fins
        13: [(4, 29), (1, 3), (30, 32)],
        14: [(4, 29), (1, 2), (31, 32)],
        15: [(5, 28)],
        16: [(5, 28)],
        17: [(6, 27)],                           # lower rim
        18: [(8, 25)],                           # chin
    },
    "fills": [
        # brown-red spiky dome
        ("runs", [(2, 13, 20), (3, 11, 22), (4, 10, 23), (5, 9, 24),
                  (6, 8, 25), (7, 7, 26), (8, 6, 27)], "B"),
        # yellow lure bulb
        ("runs", [(0, 16, 17), (1, 16, 17)], "Y"),
        # angry yellow eyes with dark pupils
        ("runs", [(5, 10, 12), (5, 21, 23)], "D", "B"),
        ("runs", [(6, 10, 11), (6, 22, 23)], "Y", "B"),
        ("put", 6, 11, "K"),
        ("put", 6, 22, "K"),
        # dark mouth interior
        ("runs", [(9, 7, 26), (10, 7, 26), (11, 6, 27), (12, 6, 27),
                  (13, 6, 27), (14, 6, 27), (15, 6, 27), (16, 6, 27)],
         "E"),
        # pale teeth hanging from both jaws
        ("runs", [(9, 9, 10), (9, 15, 16), (9, 21, 22), (10, 12, 13),
                  (10, 18, 19), (16, 9, 10), (16, 15, 16), (16, 21, 22),
                  (15, 12, 13), (15, 18, 19)], "W", "E"),
        # dark tongue rising from the throat
        ("runs", [(13, 12, 21), (14, 13, 20), (15, 14, 19)], "D", "E"),
        ("runs", [(14, 15, 18)], "E", "D"),
        # dark side fins
        ("runs", [(12, 1, 2), (12, 31, 32), (13, 1, 3), (13, 30, 32),
                  (14, 1, 2), (14, 31, 32)], "D"),
        # chin shading
        ("runs", [(18, 8, 12), (18, 21, 25)], "D"),
    ],
}
