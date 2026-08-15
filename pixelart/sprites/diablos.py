"""Diablos, horned desert wyvern. Crouched quadruped. Reference:
icons/mhrise/diablos.png; orange body, twin cream horns curving up and
forward from the skull like a bull, cream beak jaw with fangs, red eye,
cream spikes along the back, tail sweeping up into a cream-studded club.
"""

CONFIG = {
    "name": "diablos",
    "size": (36, 24),
    "compare_to": "../icons/mhrise/diablos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "O": (222, 147, 47, 255),   # orange body
        "o": (176, 112, 34, 255),   # dark orange: belly shade, far legs
        "M": (231, 223, 189, 255),  # cream: horns, jaw, spikes, club
        "m": (196, 182, 140, 255),  # dark cream: far horn, club studs
        "R": (210, 40, 45, 255),    # red eye
        "W": (246, 242, 230, 255),  # white fang
        "V": (60, 50, 40, 255),     # dark claws
    },
    "base": "O",
    "spans": {
        # near horn rows 1-5 hooking forward over the snout; far horn a
        # shorter spike behind it; tail root merges with the hip, rises
        # into the club diamond top right
        1:  [(3, 3), (32, 32)],
        2:  [(2, 3), (8, 8), (31, 33)],
        3:  [(2, 4), (7, 8), (31, 33)],
        4:  [(2, 5), (7, 8), (30, 34)],
        5:  [(2, 5), (7, 8), (30, 34)],
        6:  [(1, 9), (12, 13), (16, 17), (20, 21), (30, 33)],
        7:  [(1, 26), (29, 31)],
        8:  [(1, 27), (27, 31)],
        9:  [(1, 30)],
        10: [(1, 30)],
        11: [(1, 30)],
        12: [(2, 30)],
        13: [(3, 29)],
        14: [(4, 28)],
        15: [(5, 27)],
        16: [(6, 26)],
        17: [(9, 13), (18, 22)],
        18: [(9, 13), (18, 22)],
        19: [(9, 12), (18, 21)],
        20: [(8, 12), (18, 22)],
        21: [(8, 8), (10, 10), (12, 12), (18, 18), (20, 20), (22, 22)],
    },
    "fills": [
        # near horn cream, rooted into the skull top
        ("runs", [(1, 3, 3), (2, 2, 3), (3, 2, 4), (4, 2, 5), (5, 2, 5)],
         "M"),
        ("put", 6, 2, "MMM"),
        # far horn darker (distance shade)
        ("runs", [(2, 8, 8), (3, 7, 8), (4, 7, 8), (5, 7, 8)], "m"),
        # brow + red eye
        ("put", 7, 1, "K"),
        ("put", 8, 2, "RW"),
        # cream jaw with a dark mouth notch and white fang
        ("runs", [(11, 2, 8), (12, 3, 8)], "M"),
        ("put", 11, 2, "K"),
        ("put", 12, 2, "W"),
        # back spikes cream
        ("runs", [(6, 12, 13), (6, 16, 17), (6, 20, 21)], "M"),
        # tail club cream with dark studs
        ("runs", [(1, 32, 32), (2, 31, 33), (3, 31, 33), (4, 30, 34),
                  (5, 30, 34), (6, 30, 33)], "M"),
        ("put", 3, 32, "m"),
        ("put", 4, 31, "m"),
        ("put", 4, 33, "m"),
        # rising tail keeps one dark cream ridge
        ("put", 8, 28, "m"),
        # belly shade + far legs darker
        ("runs", [(13, 4, 28), (14, 5, 27), (15, 6, 26), (16, 7, 25)], "o"),
        ("runs", [(17, 18, 22), (18, 18, 22), (19, 18, 21), (20, 18, 22)],
         "o"),
        # claws
        ("put", 21, 8, "V"),
        ("put", 21, 10, "V"),
        ("put", 21, 12, "V"),
        ("put", 21, 18, "V"),
        ("put", 21, 20, "V"),
        ("put", 21, 22, "V"),
    ],
}
