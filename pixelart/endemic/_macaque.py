"""Macaque archetype: a small monkey sitting upright facing left, round
head with a pale face patch, rounded body, long arm, folded legs, and a
curling tail. Fur and face colors are species identity."""

CONFIG = {
    "name": "_macaque",
    "size": (26, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (170, 130, 90, 255),   # fur
        "D": (130, 96, 64, 255),    # darker fur
        "C": (232, 210, 180, 255),  # face
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(8, 13)],
        6:  [(7, 14)],
        7:  [(7, 14)],
        8:  [(7, 14)],
        9:  [(8, 13)],
        10: [(6, 18)],
        11: [(6, 18)],
        12: [(6, 17)],
        13: [(7, 16)],
        14: [(8, 15)],
        15: [(9, 14)],
        16: [(10, 13)],
        17: [(10, 11), (14, 14)],
        18: [(14, 14)],
    },
    "fills": [
        # pale face patch with eyes
        ("runs", [(6, 8, 12), (7, 7, 13), (8, 7, 13)], "C"),
        ("put", 7, 9, "K"),
        ("put", 7, 12, "K"),
        # head fur cap
        ("runs", [(5, 8, 13), (6, 7, 9), (6, 12, 14)], "D"),
        # arm reaching down
        ("runs", [(10, 6, 8), (11, 6, 8), (12, 6, 8), (13, 7, 8)], "D"),
        # body shade
        ("runs", [(13, 10, 16), (14, 10, 15), (15, 11, 14)], "D"),
        # tail curl
        ("put", 17, 14, "D"),
        ("put", 18, 14, "D"),
    ],
}
