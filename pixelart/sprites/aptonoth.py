"""Aptonoth, herbivore. The gentle grazer: grey-blue body with a long
neck raised at the upper left, small blunt head, cream throat and belly
band, dark green back stripe, four plodding legs, drooping tail. The
long-neck herbivore archetype larinoth derives from."""

CONFIG = {
    "name": "aptonoth",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/aptonoth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (142, 152, 162, 255),  # grey-blue hide
        "D": (108, 118, 130, 255),  # darker shade
        "C": (216, 206, 180, 255),  # cream throat / belly
        "V": (96, 124, 86, 255),    # green back stripe
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(2, 5)],                         # head top
        3:  [(1, 6)],
        4:  [(1, 7), (7, 8)],                 # head + neck back
        5:  [(0, 7), (8, 9)],                 # snout tip col 0
        6:  [(0, 7), (8, 10)],
        7:  [(1, 8), (9, 12)],
        8:  [(2, 9), (10, 16)],               # neck joins back
        9:  [(3, 18)],
        10: [(4, 20)],
        11: [(4, 22)],
        12: [(5, 23)],
        13: [(5, 24)],
        14: [(5, 25)],
        15: [(6, 26)],
        16: [(7, 26)],                        # tail tip
        17: [(8, 11), (14, 17), (22, 25)],    # legs + tail tip
        18: [(8, 10), (15, 16), (23, 24)],
        19: [(8, 8), (10, 10), (15, 15), (24, 24)],
    },
    "fills": [
        # gentle eye + nostril
        ("put", 4, 2, "W"),
        ("put", 4, 3, "K"),
        ("put", 5, 0, "K"),
        # green back stripe down the neck and back
        ("runs", [(4, 6, 7), (5, 7, 8), (6, 8, 9), (7, 10, 11),
                  (8, 12, 15), (9, 13, 17), (10, 15, 19), (11, 17, 21),
                  (12, 18, 22), (13, 19, 23), (14, 20, 24)], "V"),
        # cream throat and belly band along the bottom edge
        ("runs", [(9, 4, 12), (10, 5, 14), (11, 5, 16), (12, 6, 18),
                  (13, 6, 19), (14, 6, 20), (15, 7, 21), (16, 8, 21)],
         "C"),
        # darker tail underside
        ("runs", [(14, 21, 25), (15, 22, 26), (16, 22, 26)], "D"),
        # claws
        ("put", 19, 8, "W"),
        ("put", 19, 10, "W"),
        ("put", 19, 15, "W"),
        ("put", 19, 24, "W"),
    ],
}
