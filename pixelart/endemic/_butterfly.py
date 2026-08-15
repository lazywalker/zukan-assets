"""Butterfly archetype: two big wings raised over a slim body, the wings
separated from it by 1px channels, antennae up, legs below. Wing spots
are the species identity."""

CONFIG = {
    "name": "_butterfly",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (150, 110, 170, 255),  # wings
        "D": (110, 78, 130, 255),   # wing border
        "C": (240, 230, 200, 255),  # body
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(7, 7), (18, 18)],
        4:  [(6, 8), (17, 19)],
        5:  [(5, 12), (15, 22)],
        6:  [(4, 12), (15, 23)],
        7:  [(4, 12), (15, 23)],
        8:  [(4, 12), (15, 23)],
        9:  [(5, 12), (15, 22)],
        10: [(6, 12), (15, 21)],
        11: [(7, 12), (15, 20)],
        12: [(8, 11), (16, 19)],
        13: [(12, 15)],
        14: [(12, 15)],
        15: [(13, 14)],
        16: [(13, 14)],
    },
    "fills": [
        # wing borders darker with spot rows
        ("runs", [(5, 5, 6), (5, 11, 12), (6, 4, 5), (7, 4, 4),
                  (9, 4, 5), (10, 5, 6)], "D"),
        ("runs", [(5, 21, 22), (6, 22, 23), (7, 22, 23), (9, 22, 22),
                  (10, 21, 21)], "D"),
        # wing spots
        ("put", 7, 8, "W"),
        ("put", 8, 7, "W"),
        ("put", 7, 18, "W"),
        ("put", 8, 19, "W"),
        # body segments
        ("runs", [(13, 12, 15), (14, 12, 15)], "C"),
        ("put", 15, 13, "D"),
        ("put", 16, 13, "D"),
        # antennae
        ("put", 3, 7, "D"),
        ("put", 3, 18, "D"),
    ],
}
