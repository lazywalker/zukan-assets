"""Bat archetype: small furry body in the middle, two wings spread wide
with finger bones, tiny ears, feet below. Fur and membrane colors are
species identity."""

CONFIG = {
    "name": "_bat",
    "size": (30, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (110, 90, 130, 255),   # fur
        "D": (80, 62, 98, 255),     # membrane / shade
        "C": (180, 150, 200, 255),  # membrane light
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(3, 4), (24, 25)],
        7:  [(2, 5), (23, 26)],
        8:  [(1, 6), (7, 12), (16, 22), (22, 27)],
        9:  [(1, 6), (7, 21), (22, 27)],
        10: [(1, 5), (7, 21), (23, 28)],
        11: [(2, 5), (7, 21), (24, 27)],
        12: [(2, 4), (8, 20), (25, 26)],
        13: [(2, 3), (10, 18)],
        14: [(11, 12), (16, 17)],
    },
    "fills": [
        # ears
        ("runs", [(6, 3, 4), (6, 24, 25)], "D"),
        # wings: membranes with finger bones
        ("runs", [(8, 1, 6), (9, 1, 6), (10, 1, 5), (11, 2, 5),
                  (12, 2, 4), (13, 2, 3)], "D"),
        ("runs", [(8, 22, 27), (9, 22, 27), (10, 23, 28), (11, 24, 27),
                  (12, 25, 26)], "D"),
        ("runs", [(9, 2, 3), (10, 2, 2), (9, 24, 25), (10, 25, 25)],
         "C", "D"),
        # body fur + face
        ("runs", [(8, 7, 12), (9, 8, 11)], "C"),
        ("put", 9, 9, "K"),
        # scallop wing bottoms
        ("runs", [(13, 10, 18)], "D"),
    ],
}
