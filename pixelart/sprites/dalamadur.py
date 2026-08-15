"""Dalamadur, elder dragon. The world serpent: a colossal grey-mountain
serpent winding right, a blunt hammer head with red eyes, mountain spines
standing along the coils, and the tail tapering off-frame."""

CONFIG = {
    "name": "dalamadur",
    "size": (40, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (140, 138, 130, 255),  # mountain-grey scales
        "D": (108, 106, 100, 255),  # darker scales
        "R": (198, 68, 56, 255),    # red eyes
        "C": (180, 178, 168, 255),  # pale underside
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(3, 8)],                         # head top
        4:  [(2, 10)],
        5:  [(1, 11), (12, 13)],
        6:  [(1, 12), (11, 16)],              # head + spine
        7:  [(0, 13), (10, 19)],
        8:  [(0, 14), (9, 22)],
        9:  [(0, 15), (8, 26)],
        10: [(0, 15), (8, 30)],
        11: [(1, 15), (7, 34)],
        12: [(1, 15), (7, 37)],
        13: [(2, 15), (6, 39)],
        14: [(2, 15), (6, 39)],
        15: [(2, 15), (6, 39)],
        16: [(3, 15), (6, 39)],
        17: [(3, 15), (7, 39)],
        18: [(4, 15), (8, 39)],
        19: [(5, 15), (10, 39)],
        20: [(6, 15), (13, 39)],
        21: [(7, 15), (17, 39)],
    },
    "fills": [
        # blunt hammer head
        ("runs", [(3, 3, 8), (4, 2, 10), (5, 1, 9)], "D"),
        # red eyes
        ("put", 5, 4, "R"),
        ("put", 5, 8, "R"),
        # jagged mountain spines along the coils
        ("runs", [(5, 12, 13), (6, 11, 16), (7, 10, 19), (8, 9, 22),
                  (9, 8, 26), (10, 8, 30), (11, 7, 34), (12, 7, 37)],
         "D", "G"),
        # pale underside along the bottom edge
        ("runs", [(17, 4, 15), (18, 5, 15), (19, 6, 15), (20, 7, 15),
                  (21, 8, 15)], "C"),
        # coil seams
        ("runs", [(11, 30, 31), (13, 33, 34), (15, 36, 37),
                  (17, 38, 39)], "D"),
    ],
}
