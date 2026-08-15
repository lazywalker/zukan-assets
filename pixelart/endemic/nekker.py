"""Nekker: a small gray-green ogre from the Witcher hunt; big head, wide
grinning mouth with teeth, hunched body, clawed hands."""
CONFIG = {
    "name": "nekker",
    "size": (26, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (110, 122, 96, 255),   # gray-green skin
        "D": (80, 90, 68, 255),     # darker
        "C": (208, 196, 160, 255),  # belly
        "R": (200, 70, 50, 255),    # red eyes
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(7, 16)],
        6:  [(6, 17)],
        7:  [(6, 17)],
        8:  [(6, 17)],
        9:  [(7, 16)],
        10: [(5, 18)],
        11: [(5, 18)],
        12: [(5, 17)],
        13: [(6, 16)],
        14: [(7, 15)],
        15: [(8, 14)],
        16: [(7, 8), (11, 12), (15, 16)],
        17: [(7, 7), (9, 9), (11, 11), (13, 13), (15, 15), (16, 16)],
    },
    "fills": [
        # wide grinning mouth with teeth
        ("runs", [(9, 7, 16)], "K"),
        ("put", 9, 8, "W"),
        ("put", 9, 10, "W"),
        ("put", 9, 12, "W"),
        ("put", 9, 14, "W"),
        # red eyes
        ("put", 7, 9, "R"),
        ("put", 7, 14, "R"),
        # belly + claws
        ("runs", [(11, 7, 10), (12, 7, 10)], "C"),
        ("put", 16, 7, "W"),
        ("put", 16, 16, "W"),
    ],
}
