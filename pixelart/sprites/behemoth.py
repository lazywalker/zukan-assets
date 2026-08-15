"""Behemoth, elder dragon. The other-world chimera: a grey-brown bulk with
a dark mane, a horned face, a spiked tail curling up, and heavy clawed
front limbs."""

CONFIG = {
    "name": "behemoth",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (148, 132, 116, 255),  # grey-brown bulk
        "D": (112, 98, 86, 255),    # darker bulk
        "N": (52, 48, 52, 255),     # dark mane
        "R": (196, 84, 60, 255),    # red tail spine tips
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(4, 5), (9, 10)],                # horn tips
        3:  [(3, 11), (8, 12)],
        4:  [(2, 12), (7, 14)],
        5:  [(1, 13), (6, 17)],
        6:  [(1, 14), (6, 19)],
        7:  [(0, 15), (5, 21)],               # head + back
        8:  [(0, 16), (5, 22)],
        9:  [(0, 17), (5, 23)],
        10: [(0, 17), (5, 24)],
        11: [(0, 17), (5, 24)],
        12: [(0, 17), (5, 24)],
        13: [(0, 17), (5, 24)],
        14: [(0, 17), (5, 24)],
        15: [(0, 17), (5, 24)],
        16: [(1, 17), (5, 24)],
        17: [(1, 17), (5, 24)],
        18: [(1, 17), (5, 24)],
        19: [(2, 17), (5, 24)],
        20: [(3, 17), (5, 24)],
        21: [(4, 10), (14, 18), (20, 23)],    # legs + tail
    },
    "fills": [
        # dark mane over the head
        ("runs", [(2, 4, 5), (2, 9, 10), (3, 3, 11), (4, 3, 12),
                  (5, 2, 12)], "N"),
        # pale eyes
        ("put", 5, 4, "W"),
        ("put", 5, 8, "W"),
        # spiked tail curling up, red tips
        ("runs", [(6, 20, 24), (7, 21, 24), (8, 21, 24), (9, 22, 24),
                  (10, 23, 24)], "N"),
        ("put", 6, 21, "R"),
        ("put", 7, 21, "R"),
        # bulk shade
        ("runs", [(17, 1, 24), (18, 1, 24), (19, 2, 24)], "D"),
        # legs darker
        ("runs", [(21, 14, 18), (22, 15, 17)], "D"),
        # claws
        ("put", 21, 4, "W"),
        ("put", 21, 20, "W"),
        ("put", 21, 22, "W"),
    ],
}
