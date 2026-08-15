"""Moly archetype: the fluffy sheep; a round wool ball on four stub legs,
a dark bare face, folded ears, and a little tail. Wool color and fluff
dots are species identity."""

CONFIG = {
    "name": "_moly",
    "size": (30, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (232, 226, 210, 255),  # wool
        "D": (190, 182, 164, 255),  # wool shade
        "F": (70, 62, 58, 255),     # face / legs
        "V": (246, 242, 230, 255),
    },
    "base": "W",
    "spans": {
        6:  [(12, 15)],
        7:  [(10, 18)],
        8:  [(8, 20)],
        9:  [(6, 21)],
        10: [(5, 22)],
        11: [(4, 22)],
        12: [(4, 22)],
        13: [(4, 22)],
        14: [(4, 22)],
        15: [(5, 21)],
        16: [(6, 20)],
        17: [(7, 19)],
        18: [(9, 10), (16, 18)],
        19: [(9, 9), (16, 16), (18, 18)],
    },
    "fills": [
        # dark bare face at the front with an ear
        ("runs", [(8, 8, 11), (9, 6, 9), (10, 5, 8), (11, 5, 8)], "F"),
        ("put", 7, 11, "F"),
        # eye
        ("put", 9, 8, "V"),
        ("put", 9, 9, "K"),
        # wool fluff dots
        ("put", 9, 15, "D"),
        ("put", 10, 18, "D"),
        ("put", 11, 7, "D"),
        ("put", 12, 13, "D"),
        ("put", 13, 17, "D"),
        ("put", 14, 9, "D"),
        # belly shade
        ("runs", [(15, 8, 18), (16, 9, 16), (17, 11, 15)], "D"),
        # stub legs dark
        ("runs", [(18, 9, 10), (18, 16, 17)], "F"),
    ],
}
