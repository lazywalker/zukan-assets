"""Kelbi, herbivore. The little deer: orange-tan body, a big green horn
sweeping back over the shoulders, white belly, slim legs, gentle face."""

CONFIG = {
    "name": "kelbi",
    "size": (26, 24),
    "compare_to": "../icons/mh4u/kelbi.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (212, 150, 92, 255),   # tan coat
        "D": (172, 116, 66, 255),   # darker shade
        "G": (140, 180, 92, 255),   # green horn
        "C": (234, 222, 196, 255),  # cream belly / muzzle
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        3:  [(8, 10)],                        # horn tip
        4:  [(7, 11), (11, 12)],
        5:  [(6, 11), (11, 13)],              # horn sweeping back
        6:  [(4, 10), (11, 14)],
        7:  [(3, 9), (11, 15)],               # head + horn base
        8:  [(2, 9), (10, 16)],               # muzzle + back
        9:  [(2, 9), (10, 17)],
        10: [(2, 10), (10, 18)],
        11: [(3, 10), (10, 18)],
        12: [(3, 17)],
        13: [(4, 16)],
        14: [(5, 15)],
        15: [(6, 14)],
        16: [(7, 10), (13, 14)],              # legs
        17: [(7, 9), (13, 13)],
        18: [(7, 7), (9, 9), (13, 13)],
    },
    "fills": [
        # green horn sweeping back, pale tip
        ("runs", [(3, 8, 10), (4, 7, 12), (5, 6, 13), (6, 10, 14),
                  (7, 11, 15)], "G"),
        ("put", 3, 10, "W"),
        # gentle face: cream muzzle, dark eye
        ("runs", [(7, 3, 4), (8, 2, 4)], "C"),
        ("put", 6, 5, "K"),
        # cream belly along the bottom edge
        ("runs", [(11, 4, 10), (12, 4, 12), (13, 5, 12), (14, 6, 11),
                  (15, 7, 10)], "C"),
        # back shade
        ("runs", [(9, 12, 16), (10, 13, 17), (11, 13, 17)], "D"),
        # hooves
        ("put", 18, 7, "D"),
        ("put", 18, 9, "D"),
        ("put", 18, 13, "D"),
    ],
}
