"""Ceadeus, elder dragon. The sea wolf: a colossal pale sea dragon with a
huge scarred head, a gold horn on the brow, a wide mouth, gill slits, and
a long tapering body trailing right."""

CONFIG = {
    "name": "ceadeus",
    "size": (40, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (168, 172, 168, 255),  # pale sea-grey hide
        "D": (132, 136, 134, 255),  # darker hide
        "Y": (222, 184, 78, 255),   # gold horn
        "R": (168, 84, 70, 255),    # scar red
        "C": (200, 202, 196, 255),  # pale belly
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(4, 7)],                         # head top
        4:  [(2, 9), (10, 11)],
        5:  [(1, 11), (9, 14)],               # horn base
        6:  [(0, 13), (8, 16)],
        7:  [(0, 15), (7, 18)],
        8:  [(0, 16), (7, 21)],               # huge head
        9:  [(0, 17), (6, 23)],
        10: [(0, 18), (6, 25)],
        11: [(0, 18), (6, 27)],
        12: [(1, 18), (6, 29)],
        13: [(1, 18), (6, 31)],
        14: [(1, 18), (6, 33)],
        15: [(2, 18), (6, 35)],
        16: [(2, 18), (6, 37)],
        17: [(3, 18), (6, 39)],
        18: [(4, 18), (8, 39)],
        19: [(5, 12), (14, 17), (20, 25), (30, 35)],  # fins
        20: [(5, 11), (15, 16), (21, 24), (31, 34)],
    },
    "fills": [
        # gold horn on the brow
        ("runs", [(5, 9, 14), (6, 8, 15), (7, 8, 14)], "Y"),
        # pale eye
        ("put", 7, 3, "W"),
        # red scar across the head
        ("runs", [(6, 5, 6), (7, 6, 7), (8, 7, 8)], "R"),
        # wide mouth line with teeth
        ("runs", [(9, 0, 12)], "K"),
        ("put", 9, 2, "W"),
        ("put", 9, 5, "W"),
        ("put", 9, 8, "W"),
        ("put", 9, 11, "W"),
        # gill slits behind the head
        ("runs", [(12, 19, 19), (13, 20, 20), (14, 21, 21)], "D", "G"),
        # body shade along the bottom
        ("runs", [(16, 3, 16), (17, 4, 16), (18, 5, 16)], "D"),
        # fin shade
        ("runs", [(19, 21, 24), (19, 31, 34)], "D"),
        # pale belly
        ("runs", [(15, 3, 16), (16, 4, 17)], "C"),
    ],
}
