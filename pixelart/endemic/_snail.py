"""Snail archetype: a spiral shell over a soft foot, two eye stalks with
beady eyes reaching forward, a mouth. Shell shape and colors are species
identity."""

CONFIG = {
    "name": "_snail",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (150, 120, 150, 255),  # shell
        "D": (112, 88, 112, 255),   # shell shade
        "C": (200, 214, 160, 255),  # foot
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(11, 12), (16, 17)],
        7:  [(11, 12), (16, 17)],
        8:  [(7, 21)],
        9:  [(6, 22)],
        10: [(5, 22)],
        11: [(5, 22)],
        12: [(6, 21)],
        13: [(7, 20)],
        14: [(3, 22)],
        15: [(2, 23)],
        16: [(2, 23)],
        17: [(3, 22)],
        18: [(4, 21)],
    },
    "fills": [
        # eye stalks with beady eyes
        ("put", 6, 11, "C"),
        ("put", 6, 16, "C"),
        ("put", 6, 12, "K"),
        ("put", 6, 17, "K"),
        # spiral shell with a darker whorl
        ("runs", [(8, 7, 12), (8, 19, 21), (9, 6, 8), (9, 20, 22)], "D"),
        ("runs", [(10, 11, 15), (11, 11, 16), (12, 11, 15)], "D"),
        ("put", 10, 13, "W"),
        # foot with a head end
        ("runs", [(14, 3, 9), (15, 2, 5)], "C"),
        ("put", 14, 4, "K"),
        # foot bottom shade
        ("runs", [(17, 4, 21), (18, 5, 20)], "D"),
    ],
}
