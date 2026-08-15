"""Slug archetype: a shell-less soft slug with two upper antennae and a
rounded tail, crawling. Skin color and spots are species identity."""

CONFIG = {
    "name": "_slug",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (170, 140, 180, 255),  # skin
        "D": (130, 102, 140, 255),  # shade
        "C": (220, 200, 220, 255),  # light underside
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        7:  [(8, 9), (13, 14)],
        8:  [(8, 9), (13, 14)],
        9:  [(5, 21)],
        10: [(4, 22)],
        11: [(3, 22)],
        12: [(3, 22)],
        13: [(4, 21)],
        14: [(5, 20)],
        15: [(6, 19)],
        16: [(8, 17)],
    },
    "fills": [
        # antennae with dark tips
        ("runs", [(7, 8, 9), (7, 13, 14), (8, 8, 9), (8, 13, 14)], "C"),
        ("put", 7, 9, "D"),
        ("put", 7, 14, "D"),
        # back spots
        ("put", 10, 8, "D"),
        ("put", 11, 12, "D"),
        ("put", 11, 17, "D"),
        ("put", 12, 10, "D"),
        # underside light band
        ("runs", [(13, 6, 18), (14, 7, 17), (15, 8, 16)], "C"),
        # eye
        ("put", 10, 6, "K"),
    ],
}
