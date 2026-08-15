"""Paolumu, fluffy floating wyvern. Round white body ball, symmetric front
pose. Reference: icons/mhw/paolumu.png; cream fluffy sphere with gray
triangle flecks, orange face and ears in the center, gray wing arms spread
up-out with orange pads, plum spiral tail, tiny feet.
"""

CONFIG = {
    "name": "paolumu",
    "size": (28, 24),
    "compare_to": "../icons/mhw/paolumu.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "W": (215, 206, 196, 255),  # cream fluff
        "g": (175, 166, 158, 255),  # gray: wing arms, flecks
        "O": (215, 105, 68, 255),   # orange: face, ear, wing pads
        "P": (120, 68, 80, 255),    # plum: spiral tail
        "D": (51, 39, 36, 255),     # dark: eyes, nose
    },
    "base": "W",
    "spans": {
        # wing arms rows 1-5, rising out from behind the ball
        1:  [(2, 3), (24, 25)],
        2:  [(1, 4), (23, 26)],
        3:  [(1, 6), (8, 18), (22, 26)],
        4:  [(1, 7), (7, 19), (20, 26)],
        5:  [(1, 7), (6, 20), (20, 25)],
        6:  [(1, 21), (22, 24)],
        7:  [(1, 24)],
        8:  [(1, 24)],
        9:  [(2, 24)],
        10: [(2, 24)],
        11: [(3, 24)],
        12: [(3, 23)],
        13: [(4, 23)],
        14: [(4, 22)],
        15: [(5, 21)],
        16: [(6, 21), (21, 25)],              # tail start
        17: [(7, 15), (17, 25)],
        18: [(8, 14), (18, 26)],
        19: [(9, 13), (19, 26)],
        20: [(10, 12), (20, 25)],
        21: [(10, 11), (21, 23)],             # tail tip + feet
        22: [(8, 8), (11, 11)],
    },
    "fills": [
        # wing arms gray with orange pads at the tips
        ("runs", [(1, 2, 3), (2, 1, 4), (3, 1, 6), (4, 1, 7), (5, 1, 7),
                  (1, 24, 25), (2, 23, 26), (3, 22, 26), (4, 20, 26),
                  (5, 20, 25)], "g"),
        ("runs", [(1, 2, 3), (2, 1, 3), (1, 24, 25), (2, 23, 25)],
         "O", "g"),
        # gray flecks on the ball
        ("runs", [(5, 10, 12), (6, 15, 17), (7, 12, 13), (8, 16, 18),
                  (9, 8, 9), (9, 19, 20), (10, 12, 13), (11, 18, 19),
                  (12, 7, 8), (13, 16, 18)], "g"),
        # orange face + ears
        ("runs", [(11, 12, 15), (12, 11, 16), (13, 11, 16), (14, 12, 15),
                  (15, 12, 14)], "O"),
        ("runs", [(10, 12, 13), (10, 15, 16)], "O"),
        # face details: eyes + nose
        ("put", 12, 12, "D"),
        ("put", 12, 15, "D"),
        ("put", 13, 13, "D"),
        ("put", 13, 14, "D"),
        ("put", 14, 13, "D"),
        ("put", 14, 14, "D"),
        # plum spiral tail
        ("runs", [(17, 19, 25), (18, 21, 26), (19, 22, 26), (20, 22, 25),
                  (21, 21, 23)], "P"),
        ("runs", [(18, 22, 24), (19, 23, 25)], "W"),
    ],
}
