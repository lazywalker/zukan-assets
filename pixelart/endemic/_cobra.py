"""Cobra archetype: a flared hood over a raised head with round eyes and a
forked tongue, body coiling down to the right. Hood color and banding are
species identity. Tsuchinoko patches a fat hoodless body."""

CONFIG = {
    "name": "_cobra",
    "size": (30, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (96, 130, 96, 255),    # body
        "D": (70, 98, 70, 255),     # darker bands
        "H": (180, 200, 160, 255),  # hood front
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(5, 9)],
        7:  [(4, 10)],
        8:  [(3, 11)],
        9:  [(3, 11)],
        10: [(4, 10)],
        11: [(5, 9)],
        12: [(4, 22)],
        13: [(4, 25)],
        14: [(5, 26)],
        15: [(6, 25)],
        16: [(7, 24)],
        17: [(8, 22)],
        18: [(9, 20)],
    },
    "fills": [
        # hood front lighter with a dark rim
        ("runs", [(6, 5, 9), (7, 4, 10), (8, 3, 7), (8, 10, 11)], "H"),
        ("runs", [(8, 8, 9), (9, 3, 4), (9, 10, 11)], "D"),
        # head: eyes + forked tongue
        ("put", 9, 6, "W"),
        ("put", 9, 7, "K"),
        ("put", 10, 4, "W"),
        ("runs", [(10, 4, 5)], "K"),
        # bands down the coil
        ("runs", [(12, 8, 11), (13, 9, 13), (14, 12, 16), (15, 13, 17),
                  (16, 15, 19), (17, 16, 18)], "D"),
        # coil underside shade
        ("runs", [(14, 20, 26), (15, 19, 25), (16, 18, 24)], "D"),
    ],
}
