"""Guardian Seikret, construct. The construct raptor: a pale armored bird
with an amber visor crest, slim legs, a long neck, and a rider's perch
saddle."""

CONFIG = {
    "name": "guardian-seikret",
    "size": (28, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (206, 202, 192, 255),  # pale armor plumage
        "D": (170, 166, 156, 255),  # darker armor
        "A": (236, 178, 88, 255),   # amber visor glow
        "N": (70, 66, 60, 255),     # dark beak / feet
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(3, 5), (8, 9)],                 # head crest + tail tip
        3:  [(2, 6), (7, 10)],
        4:  [(1, 7), (6, 12)],                # head + neck
        5:  [(1, 8), (5, 14)],
        6:  [(0, 8), (4, 16)],                # neck + body
        7:  [(0, 9), (4, 18)],
        8:  [(0, 9), (4, 19)],                # body
        9:  [(0, 9), (4, 20)],
        10: [(1, 9), (4, 20)],                # saddle zone
        11: [(1, 9), (4, 20)],
        12: [(1, 9), (4, 20)],
        13: [(2, 9), (5, 19)],
        14: [(2, 9), (6, 17)],
        15: [(3, 9), (8, 15)],
        16: [(4, 9), (10, 13)],               # legs
        17: [(4, 8), (11, 12)],
        18: [(4, 4), (6, 6), (11, 11)],
    },
    "fills": [
        # amber visor crest on the head
        ("runs", [(2, 3, 5), (3, 2, 6), (4, 1, 4)], "A"),
        # dark beak
        ("runs", [(5, 0, 2), (6, 0, 2)], "N"),
        # dark eye
        ("put", 4, 4, "K"),
        # saddle band on the back
        ("runs", [(10, 5, 19), (11, 5, 19)], "D", "G"),
        # body shade
        ("runs", [(13, 2, 9), (14, 2, 9), (15, 3, 9)], "D"),
        # legs dark
        ("runs", [(16, 10, 13), (17, 11, 12)], "N"),
        # feet
        ("put", 18, 4, "N"),
        ("put", 18, 6, "N"),
        ("put", 18, 11, "N"),
    ],
}
