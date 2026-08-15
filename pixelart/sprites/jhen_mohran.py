"""Jhen Mohran, elder dragon. The sand ship: a black-sanded leviathan
cruising through dunes, a broad shovel head with two big tusk rows, gold
trim along the carapace, and stubby flipper legs."""

CONFIG = {
    "name": "jhen-mohran",
    "size": (40, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (66, 60, 54, 255),     # black-sand hide
        "D": (46, 42, 38, 255),     # darker hide
        "Y": (222, 178, 84, 255),   # gold trim
        "C": (206, 188, 156, 255),  # pale tusks
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        3:  [(4, 8)],                         # head top
        4:  [(2, 11), (12, 13)],
        5:  [(1, 13), (11, 16)],
        6:  [(0, 15), (10, 18)],
        7:  [(0, 16), (9, 21)],
        8:  [(0, 17), (8, 24)],               # head + carapace
        9:  [(0, 18), (7, 27)],
        10: [(0, 19), (7, 30)],
        11: [(0, 19), (6, 33)],
        12: [(0, 19), (6, 36)],
        13: [(0, 19), (6, 39)],
        14: [(0, 19), (6, 39)],
        15: [(0, 19), (6, 39)],
        16: [(0, 19), (6, 39)],
        17: [(1, 19), (6, 39)],
        18: [(1, 19), (7, 39)],
        19: [(2, 19), (8, 39)],
        20: [(3, 19), (9, 38)],
        21: [(6, 11), (16, 20), (26, 30), (35, 37)],  # flippers
        22: [(6, 10), (17, 19), (27, 29), (35, 36)],
    },
    "fills": [
        # broad shovel head with a pale brow
        ("runs", [(3, 4, 8), (4, 2, 11), (5, 1, 11)], "D"),
        # two big tusk rows
        ("runs", [(8, 0, 4), (9, 0, 4), (10, 0, 4)], "C"),
        ("runs", [(8, 12, 14), (9, 12, 14), (10, 12, 14)], "C"),
        # dark mouth gap between the tusks
        ("runs", [(8, 5, 11), (9, 5, 11), (10, 5, 11)], "K"),
        # teeth dots
        ("put", 9, 6, "W"),
        ("put", 9, 9, "W"),
        # eye
        ("put", 6, 3, "W"),
        # gold trim along the carapace ridge
        ("runs", [(5, 11, 16), (6, 10, 18), (7, 9, 21), (8, 8, 24),
                  (9, 7, 27), (10, 7, 30), (11, 6, 33), (12, 6, 36)], "Y"),
        # hide shade
        ("runs", [(17, 2, 19), (18, 2, 19), (19, 3, 19), (20, 4, 19)], "D"),
        # flippers darker
        ("runs", [(21, 16, 20), (21, 26, 30), (22, 17, 19),
                  (22, 27, 29)], "D"),
    ],
}
