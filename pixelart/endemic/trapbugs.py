"""Trapbugs: pill bugs that clamp shut; a segmented shell split open at
the front like a trap."""
CONFIG = {
    "name": "trapbugs",
    "size": (28, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (120, 110, 130, 255),  # shell
        "D": (88, 80, 98, 255),     # darker bands
        "C": (210, 190, 150, 255),  # inner mouth
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        7:  [(8, 12), (18, 21)],
        8:  [(6, 23)],
        9:  [(4, 24)],
        10: [(3, 25)],
        11: [(3, 25)],
        12: [(3, 25)],
        13: [(4, 24)],
        14: [(5, 23)],
        15: [(6, 21)],
        16: [(7, 19)],
        17: [(9, 10), (14, 15), (18, 18)],
        18: [(9, 9), (14, 14), (18, 18)],
    },
    "fills": [
        # the open trap mouth at the front, pale with teeth
        ("runs", [(8, 8, 12), (9, 4, 7)], "C"),
        ("runs", [(10, 3, 5)], "K"),
        ("put", 10, 6, "W"),
        ("put", 11, 4, "W"),
        # shell segment bands
        ("runs", [(9, 18, 24), (11, 16, 25), (13, 17, 24), (15, 15, 21)],
         "D"),
        # eyes on stalks at the top
        ("put", 7, 10, "W"),
        ("put", 7, 11, "K"),
    ],
}
