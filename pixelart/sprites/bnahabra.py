"""Bnahabra, neopteron. The paralyzing fly: a small round body with big
red-orange compound eyes, two pale wings spread up, and thin legs."""

CONFIG = {
    "name": "bnahabra",
    "size": (24, 24),
    "compare_to": "../icons/mhrise/bnahabra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (120, 140, 100, 255),  # green body
        "D": (90, 106, 74, 255),    # darker shade
        "R": (222, 96, 62, 255),    # red-orange eyes
        "W": (226, 226, 216, 255),  # pale wings
        "w": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        5:  [(4, 6)],                         # antenna
        6:  [(3, 7), (8, 12)],                # head + wing tip
        7:  [(2, 8), (7, 14)],
        8:  [(2, 9), (7, 15)],                # head + wing
        9:  [(2, 9), (6, 15)],
        10: [(2, 9), (6, 15)],                # body
        11: [(2, 9), (6, 14)],
        12: [(3, 9), (7, 13)],
        13: [(3, 8), (8, 12)],
        14: [(4, 8), (9, 11)],
        15: [(4, 7)],
        16: [(4, 6), (8, 10)],                # legs
        17: [(4, 4), (6, 6), (9, 9)],
    },
    "fills": [
        # big red-orange compound eyes
        ("runs", [(7, 2, 4), (8, 2, 4), (9, 2, 4)], "R"),
        ("put", 8, 4, "K"),
        # pale wings spread up-right
        ("runs", [(6, 8, 12), (7, 7, 14), (8, 7, 15), (9, 6, 15)], "W"),
        ("runs", [(8, 10, 11), (9, 10, 12)], "D", "W"),
        # body stripes
        ("runs", [(11, 2, 9), (13, 4, 8)], "D"),
        # legs
        ("put", 17, 4, "D"),
        ("put", 17, 6, "D"),
        ("put", 17, 9, "D"),
    ],
}
