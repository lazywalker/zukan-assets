"""Uragaan, brute wyvern. The rolling boulder, drawn in the armored front
of its icon: a studded plate dome with ore glints, a dark jaw gap with
white teeth sunk low, and the huge pale bone chin axe curving up across
the whole front, on stubby legs."""

CONFIG = {
    "name": "uragaan",
    "size": (34, 24),
    "compare_to": "../icons/mhw/uragaan.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (165, 115, 55, 255),    # rocky plate
        "D": (120, 80, 38, 255),     # dark plate shade
        "O": (190, 90, 40, 255),     # rust accents
        "C": (225, 210, 180, 255),   # bone chin axe
        "E": (60, 30, 20, 255),      # dark jaw
        "Y": (240, 210, 60, 255),    # ore glints
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(14, 19)],                          # dome top
        3:  [(12, 21)],
        4:  [(10, 23)],
        5:  [(9, 24)],
        6:  [(8, 25)],
        7:  [(7, 26)],
        8:  [(6, 27)],
        9:  [(5, 28)],
        10: [(5, 28)],                           # face row
        11: [(4, 29)],
        12: [(4, 29)],                           # jaw row
        13: [(4, 29)],
        14: [(3, 30)],                           # chin axe
        15: [(3, 30)],
        16: [(4, 29)],
        17: [(5, 28)],
        18: [(6, 27)],
        19: [(8, 12), (16, 17), (21, 25)],       # legs
        20: [(8, 12), (16, 17), (21, 25)],
        21: [(8, 11), (16, 17), (22, 25)],
    },
    "fills": [
        # plate dome with dark seams and studs
        ("runs", [(2, 14, 19), (3, 12, 21), (4, 10, 23), (5, 9, 24),
                  (6, 8, 25), (7, 7, 26), (8, 6, 27), (9, 5, 28)], "B"),
        ("runs", [(3, 15, 16), (3, 18, 19),
                  (4, 13, 14), (4, 20, 21), (5, 12, 13), (5, 21, 22),
                  (6, 11, 12), (6, 22, 23), (7, 10, 11), (7, 23, 24),
                  (8, 9, 10), (8, 24, 25)], "D", "B"),
        # ore glints studding the dome
        ("runs", [(4, 16, 17), (6, 14, 15), (6, 19, 20), (8, 12, 13),
                  (8, 21, 22), (10, 10, 11), (10, 23, 24)], "Y", "B"),
        # tiny eyes sunk low
        ("put", 10, 13, "K"),
        ("put", 10, 20, "K"),
        # dark jaw gap with white teeth
        ("runs", [(12, 10, 23), (13, 10, 23)], "E"),
        ("runs", [(12, 11, 12), (12, 16, 17), (12, 21, 22), (13, 13, 14),
                  (13, 18, 19)], "W", "E"),
        # the pale bone chin axe curving up
        ("runs", [(14, 3, 30), (15, 3, 30), (16, 4, 29), (17, 5, 28),
                  (18, 6, 27)], "C", "B"),
        ("runs", [(14, 3, 5), (15, 3, 4), (14, 28, 30), (15, 29, 30),
                  (16, 4, 5), (16, 28, 29), (17, 5, 6), (17, 27, 28),
                  (18, 6, 7), (18, 26, 27)], "E", "C"),
        ("runs", [(15, 12, 21)], "W", "C"),
        # stubby dark legs
        ("runs", [(19, 8, 12), (19, 21, 25), (20, 8, 12), (20, 21, 25),
                  (21, 8, 11), (21, 22, 25), (19, 16, 17), (20, 16, 17)],
         "D", "B"),
    ],
}
