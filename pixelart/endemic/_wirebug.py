"""Wirebug archetype: a rounded bug with an arched back, two glowing
sacs on its sides, antennae forward, and small legs. Sac and shell
colors are species identity."""

CONFIG = {
    "name": "_wirebug",
    "size": (26, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (90, 100, 150, 255),   # shell
        "D": (64, 72, 116, 255),    # darker shell
        "G": (140, 230, 200, 255),  # glow sacs
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(11, 12), (15, 16)],
        7:  [(10, 17)],
        8:  [(8, 18)],
        9:  [(6, 20)],
        10: [(5, 21)],
        11: [(5, 21)],
        12: [(6, 20)],
        13: [(8, 18)],
        14: [(10, 16)],
        15: [(12, 14)],
        16: [(8, 8), (11, 11), (14, 14), (17, 17)],
        17: [(8, 8), (11, 11), (14, 14), (17, 17)],
    },
    "fills": [
        # antennae
        ("put", 6, 11, "D"),
        ("put", 6, 15, "D"),
        # glowing sacs on both flanks
        ("runs", [(9, 6, 8), (10, 5, 8)], "G"),
        ("runs", [(9, 18, 20), (10, 18, 21)], "G"),
        ("put", 10, 6, "W"),
        ("put", 10, 19, "W"),
        # shell arch banding
        ("runs", [(8, 9, 17), (9, 10, 16)], "D"),
        # face
        ("put", 12, 6, "W"),
        ("put", 12, 7, "K"),
    ],
}
