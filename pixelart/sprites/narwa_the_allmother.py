"""Narwa the Allmother, elder dragon. The all-mother serpent: a white-gold
serpentine body with twin arcing horn crests, yellow organ rings along
the coils, floating above the storm."""

CONFIG = {
    "name": "narwa-the-allmother",
    "size": (38, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (226, 222, 214, 255),  # white serpent body
        "D": (188, 184, 176, 255),  # body shade
        "Y": (238, 196, 70, 255),   # gold organ rings / horns
        "N": (76, 68, 56, 255),     # dark horn edges
        "C": (240, 236, 228, 255),  # bright underside
    },
    "base": "W",
    "spans": {
        2:  [(4, 5), (9, 10)],                # horn tips
        3:  [(3, 6), (8, 11)],
        4:  [(2, 7), (7, 13)],                # horns + crest
        5:  [(1, 8), (6, 16)],
        6:  [(1, 9), (5, 19)],
        7:  [(0, 10), (4, 22)],               # head + body
        8:  [(0, 10), (4, 25)],
        9:  [(0, 11), (4, 28)],
        10: [(0, 11), (5, 31)],
        11: [(0, 11), (7, 34)],
        12: [(1, 11), (10, 37)],
        13: [(1, 11), (14, 37)],
        14: [(2, 11), (19, 37)],
        15: [(2, 11), (25, 37)],
        16: [(2, 11), (31, 37)],
        17: [(3, 11), (33, 37)],
    },
    "fills": [
        # gold arcing horns with dark edges
        ("runs", [(2, 4, 5), (2, 9, 10), (3, 3, 6), (3, 8, 11),
                  (4, 2, 7), (4, 7, 13)], "Y"),
        ("runs", [(4, 11, 13), (5, 12, 15)], "N", "Y"),
        # dark eyes
        ("put", 6, 3, "N"),
        ("put", 6, 6, "N"),
        # yellow organ rings along the coils
        ("runs", [(8, 5, 8), (9, 5, 8), (10, 6, 9), (11, 8, 11),
                  (12, 11, 14), (13, 15, 18), (14, 20, 23),
                  (15, 26, 29), (16, 32, 35)], "Y", "W"),
        # body shade
        ("runs", [(13, 1, 10), (14, 2, 10), (15, 2, 10), (16, 2, 10),
                  (17, 3, 10)], "D"),
        # bright underside
        ("runs", [(11, 1, 4), (12, 1, 5), (13, 1, 6)], "C"),
    ],
}
