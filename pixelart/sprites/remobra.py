"""Remobra, snake wyvern. The venom serpent: a brown-orange banded snake
body with a cobra-ish head, small bat wings folded at the shoulder, and a
long tapering tail. Small, but the band pattern is the identity."""

CONFIG = {
    "name": "remobra",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/remobra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (168, 112, 62, 255),   # brown-orange bands
        "D": (126, 80, 44, 255),    # darker bands
        "C": (214, 178, 130, 255),  # pale jaw / belly
        "R": (202, 70, 58, 255),    # red wing membrane
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        4:  [(3, 7)],                         # head top
        5:  [(2, 8), (8, 10)],
        6:  [(1, 9), (8, 12)],
        7:  [(1, 9), (8, 14)],                # head + wing
        8:  [(1, 8), (7, 16)],
        9:  [(1, 8), (6, 18)],
        10: [(1, 8), (6, 20)],
        11: [(2, 7), (7, 21)],
        12: [(2, 7), (8, 23)],
        13: [(3, 6), (9, 24)],
        14: [(3, 6), (10, 25)],
        15: [(4, 5), (12, 26)],
        16: [(4, 5), (14, 27)],
        17: [(5, 5), (17, 27)],
        18: [(6, 6), (21, 26)],
        19: [(7, 7), (24, 25)],
    },
    "fills": [
        # red wing membrane with dark struts
        ("runs", [(8, 8, 15), (9, 7, 17), (10, 7, 19), (11, 8, 20),
                  (12, 9, 22)], "R"),
        ("runs", [(10, 10, 10), (11, 11, 11), (12, 12, 12)], "D", "R"),
        # pale eye
        ("put", 6, 3, "W"),
        # pale jaw
        ("runs", [(7, 1, 4), (8, 1, 3)], "C"),
        # dark banding down the whole body
        ("runs", [(9, 8, 9), (10, 9, 10), (11, 10, 11), (12, 11, 12),
                  (13, 12, 13), (14, 13, 14), (15, 15, 16),
                  (16, 17, 18), (17, 19, 20), (18, 22, 23),
                  (19, 24, 25)], "D"),
        # pale belly line
        ("runs", [(11, 7, 8), (12, 8, 9), (13, 9, 10), (14, 10, 11),
                  (15, 12, 13), (16, 14, 15)], "C"),
    ],
}
