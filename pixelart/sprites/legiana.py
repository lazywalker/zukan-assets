"""Legiana, flying wyvern. The breeze-lance, drawn in the symmetric front
spread of its icon: light-blue wings like a butterfly with dark chevron
bands, a pale white body and head between them with fin horns, and a thin
white tail hanging below."""

CONFIG = {
    "name": "legiana",
    "size": (34, 24),
    "compare_to": "../icons/mhw/legiana.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (152, 190, 224, 255),
        "D": (86, 120, 168, 255),
        "C": (236, 239, 246, 255),
    },
    "base": "B",
    "spans": {
        2:  [(5, 8), (12, 13), (20, 21), (25, 28)],   # wing tips + fin horns
        3:  [(3, 10), (12, 21), (23, 30)],
        4:  [(1, 32)],
        5:  [(0, 33)],
        6:  [(0, 33)],
        7:  [(0, 33)],
        8:  [(0, 33)],
        9:  [(1, 32)],
        10: [(2, 31)],
        11: [(4, 29)],
        12: [(6, 27)],
        13: [(8, 25)],
        14: [(10, 23)],
        15: [(12, 21)],
        16: [(15, 18)],
        17: [(16, 17)],
        18: [(16, 17)],
        19: [(16, 17)],
        20: [(16, 17)],
    },
    "fills": [
        # pale head between the fin horns
        ("runs", [(3, 14, 19), (4, 13, 20), (5, 13, 20), (6, 14, 19),
                  (7, 15, 18)], "C"),
        # dark eyes
        ("put", 5, 15, "K"),
        ("put", 5, 18, "K"),
        # fin horns shade
        ("runs", [(2, 12, 13), (2, 20, 21), (3, 12, 13), (3, 20, 21)], "D"),
        # dark chevron bands fanning across the wings
        ("runs", [(4, 2, 5), (5, 1, 4), (7, 1, 4), (9, 2, 5), (10, 4, 7),
                  (12, 7, 10), (13, 9, 12), (14, 11, 13)], "D"),
        ("runs", [(4, 28, 31), (5, 29, 32), (7, 29, 32), (9, 28, 31),
                  (10, 26, 29), (12, 23, 26), (13, 21, 24), (14, 20, 22)],
         "D"),
        # pale leading edge on the wing tips
        ("runs", [(2, 5, 8), (2, 25, 28), (3, 3, 5), (3, 28, 30)], "C"),
        # tail bands and tip
        ("runs", [(16, 15, 18), (18, 16, 17), (20, 16, 17)], "D"),
        ("put", 17, 16, "C"),
        ("put", 17, 17, "C"),
        ("put", 19, 16, "C"),
        ("put", 19, 17, "C"),
    ],
}
