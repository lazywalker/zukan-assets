"""Qurupeco, bird wyvern. The songbird: a red-crested head with a pale
beak and an orange throat pouch it puffs when it sings, olive wings with
a big cream eyespot, a yellow chest, and a purple tail curling up."""

CONFIG = {
    "name": "qurupeco",
    "size": (34, 24),
    "compare_to": "../icons/mh3u/qurupeco.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (202, 72, 60, 255),    # red head
        "G": (142, 152, 82, 255),   # olive wings
        "D": (110, 118, 62, 255),   # darker olive
        "F": (222, 112, 72, 255),   # orange throat pouch
        "Y": (232, 202, 120, 255),  # yellow chest
        "P": (122, 92, 142, 255),   # purple tail
        "B": (226, 202, 162, 255),  # pale beak
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(4, 6)],                         # crest feather
        4:  [(3, 7), (13, 14)],
        5:  [(2, 8), (12, 16)],
        6:  [(1, 9), (11, 18)],
        7:  [(0, 10), (10, 20)],              # beak + wing
        8:  [(1, 9), (9, 21)],
        9:  [(1, 9), (8, 22)],
        10: [(2, 8), (8, 23)],
        11: [(2, 8), (8, 24)],
        12: [(3, 8), (9, 24)],
        13: [(4, 8), (10, 23)],
        14: [(5, 8), (12, 22)],
        15: [(6, 8), (14, 21)],
        16: [(7, 8), (16, 20)],
        17: [(8, 8), (18, 19)],
        18: [(9, 12), (16, 18)],              # legs
        19: [(9, 11), (17, 17)],
        20: [(9, 9), (11, 11), (16, 16), (18, 18)],
    },
    "fills": [
        # red head with a crest feather
        ("runs", [(3, 4, 6), (4, 3, 7), (5, 2, 8), (6, 2, 8),
                  (7, 2, 9)], "R"),
        # pale beak
        ("runs", [(7, 0, 2), (8, 1, 3)], "B"),
        # orange throat pouch
        ("runs", [(8, 2, 8), (9, 1, 8), (10, 2, 7)], "F"),
        # dark eye on the red head
        ("put", 6, 5, "K"),
        # yellow chest
        ("runs", [(11, 3, 8), (12, 4, 8), (13, 5, 8), (14, 6, 8)], "Y"),
        # cream eyespot ring on the wing
        ("runs", [(10, 16, 21), (11, 16, 22), (12, 17, 22)], "W", "G"),
        ("runs", [(11, 18, 20)], "P", "W"),
        # purple tail curling up
        ("runs", [(4, 13, 14), (5, 12, 16), (6, 11, 18), (7, 10, 20),
                  (8, 9, 21)], "P"),
        # wing shade
        ("runs", [(13, 12, 22), (14, 13, 21), (15, 14, 20)], "D"),
        # claws
        ("put", 20, 9, "W"),
        ("put", 20, 11, "W"),
        ("put", 20, 16, "W"),
        ("put", 20, 18, "W"),
    ],
}
