"""Gammoth, fanged beast. The snow mammoth: a massive white-furred dome
body over stubby legs, a purple face plate with a curved trunk, two big
ivory tusks, and gold trim along the fur edge."""

CONFIG = {
    "name": "gammoth",
    "size": (36, 24),
    "compare_to": "../icons/mhgu/gammoth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (226, 222, 212, 255),  # white fur
        "D": (186, 180, 170, 255),  # fur shade
        "V": (104, 84, 128, 255),   # purple face
        "I": (236, 228, 208, 255),  # ivory tusks
        "Y": (222, 178, 82, 255),   # gold trim
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        3:  [(10, 22)],                       # dome top
        4:  [(8, 25)],
        5:  [(6, 27)],
        6:  [(4, 28)],
        7:  [(3, 30)],
        8:  [(2, 31)],                        # dome body
        9:  [(1, 32), (31, 32)],
        10: [(1, 33)],
        11: [(0, 33)],
        12: [(0, 34)],                        # head zone left
        13: [(0, 34)],
        14: [(0, 34)],
        15: [(0, 33)],
        16: [(1, 33)],
        17: [(1, 32)],
        18: [(2, 31)],
        19: [(3, 30)],
        20: [(4, 29)],
        21: [(6, 12), (15, 20), (24, 28)],    # legs
        22: [(6, 11), (16, 19), (25, 27)],
        23: [(6, 6), (8, 8), (16, 16), (18, 18), (25, 25), (27, 27)],
    },
    "fills": [
        # purple face plate with pale eyes
        ("runs", [(11, 0, 7), (12, 0, 8), (13, 0, 8), (14, 0, 8),
                  (15, 0, 7), (16, 1, 6)], "V"),
        ("put", 12, 3, "W"),
        ("put", 13, 5, "W"),
        # curved trunk
        ("runs", [(15, 0, 1), (16, 0, 2), (17, 0, 3), (18, 1, 4),
                  (19, 2, 5), (20, 3, 6)], "V"),
        # big ivory tusks sweeping up
        ("runs", [(14, 8, 12), (13, 10, 14), (12, 12, 15)], "I"),
        ("runs", [(18, 6, 10), (17, 8, 12), (16, 10, 14)], "I"),
        # gold trim along the fur edge
        ("runs", [(3, 10, 22), (4, 8, 12), (4, 22, 25), (5, 6, 10),
                  (5, 24, 27), (6, 4, 8), (6, 26, 28), (7, 3, 6),
                  (7, 28, 30)], "Y"),
        # fur shade under the dome
        ("runs", [(17, 20, 32), (18, 19, 31), (19, 18, 30),
                  (20, 17, 29)], "D"),
        # claws
        ("put", 23, 6, "W"),
        ("put", 23, 8, "W"),
        ("put", 23, 16, "W"),
        ("put", 23, 18, "W"),
        ("put", 23, 25, "W"),
        ("put", 23, 27, "W"),
    ],
}
