"""Arzuros, fanged beast. The honey bear: plump cream-furred body with a
blue-purple carapace saddle on the shoulders and rump, round ears, small
bowl-shaped eye patches, brown clawed paws."""

CONFIG = {
    "name": "arzuros",
    "size": (32, 24),
    "compare_to": "../icons/mhrise/arzuros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (228, 218, 196, 255),   # cream fur
        "D": (188, 175, 152, 255),   # fur shade
        "B": (88, 72, 118, 255),     # blue-purple carapace
        "N": (110, 78, 58, 255),     # brown claws / paws
        "R": (200, 60, 50, 255),     # eye rim
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        2:  [(3, 5), (8, 10)],                 # ears
        3:  [(2, 11)],
        4:  [(1, 12), (18, 25)],               # head + back hump
        5:  [(1, 13), (16, 27)],
        6:  [(1, 14), (14, 28)],
        7:  [(0, 15), (13, 28)],
        8:  [(0, 15), (12, 28)],
        9:  [(0, 15), (12, 28)],
        10: [(0, 15), (12, 28)],
        11: [(1, 15), (12, 28)],
        12: [(2, 26)],
        13: [(2, 26)],
        14: [(3, 25)],
        15: [(4, 24)],
        16: [(5, 24)],
        17: [(6, 23)],
        18: [(6, 10), (13, 17), (20, 24)],     # legs
        19: [(6, 10), (13, 17), (20, 24)],
        20: [(6, 10), (13, 17), (20, 24)],
        21: [(6, 6), (8, 8), (13, 13), (15, 15), (20, 20), (22, 22)],
    },
    "fills": [
        # carapace saddle on the shoulders and rump
        ("runs", [(4, 18, 25), (5, 16, 21), (5, 23, 27), (6, 14, 18),
                  (6, 24, 28), (7, 13, 16), (7, 25, 28), (8, 25, 28),
                  (9, 25, 28), (10, 25, 28)], "B"),
        # eye with red rim
        ("put", 6, 4, "K"),
        ("put", 5, 4, "R"),
        # muzzle shade and nose
        ("runs", [(7, 0, 2), (8, 0, 3)], "D"),
        ("put", 7, 0, "K"),
        # belly shade
        ("runs", [(13, 4, 12), (14, 5, 13), (15, 6, 14), (16, 7, 15)],
         "D"),
        # brown paws
        ("runs", [(18, 6, 10), (19, 6, 10), (20, 6, 10), (18, 20, 24),
                  (19, 20, 24), (20, 20, 24)], "N"),
        # claws
        ("put", 21, 6, "W"),
        ("put", 21, 8, "W"),
        ("put", 21, 13, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 20, "W"),
        ("put", 21, 22, "W"),
    ],
}
