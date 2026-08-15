"""Malfestio, bird wyvern. The night owl: a round blue-grey head with dark
ear tufts, wide folded wings with barred feather bands, an orange chest
collar over a scaled cream belly, and orange eyes."""

CONFIG = {
    "name": "malfestio",
    "size": (32, 24),
    "compare_to": "../icons/mhgu/malfestio.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (112, 126, 152, 255),  # blue-grey plumage
        "D": (82, 94, 120, 255),    # darker bars / tufts
        "C": (204, 200, 178, 255),  # cream belly
        "O": (232, 152, 62, 255),   # orange chest collar / eyes
        "N": (50, 56, 82, 255),     # dark ear tufts
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(5, 6), (12, 13)],               # ear tufts
        3:  [(4, 8), (11, 14)],
        4:  [(3, 9), (10, 16)],               # round head
        5:  [(2, 10), (9, 18)],
        6:  [(1, 11), (8, 19)],
        7:  [(1, 12), (8, 21)],
        8:  [(1, 13), (7, 22)],
        9:  [(1, 13), (7, 23)],
        10: [(2, 13), (6, 23)],
        11: [(2, 14), (6, 22)],
        12: [(3, 14), (6, 21)],
        13: [(4, 13), (7, 20)],
        14: [(5, 12), (8, 19)],
        15: [(6, 11), (9, 18)],
        16: [(7, 10), (11, 16)],
        17: [(8, 9), (12, 15)],               # feet
        18: [(8, 8), (13, 14)],
    },
    "fills": [
        # dark ear tufts
        ("runs", [(2, 5, 6), (2, 12, 13), (3, 4, 5), (3, 12, 13)], "N"),
        # face disc lighter
        ("runs", [(5, 4, 9), (6, 3, 10), (7, 3, 10)], "C", "B"),
        # orange eyes
        ("put", 6, 5, "O"),
        ("put", 6, 8, "O"),
        # small dark beak
        ("put", 8, 6, "N"),
        ("put", 8, 7, "N"),
        # orange chest collar
        ("runs", [(9, 2, 12), (10, 2, 13)], "O"),
        # cream scaled belly
        ("runs", [(11, 3, 12), (12, 4, 12), (13, 5, 11), (14, 6, 10)],
         "C"),
        ("runs", [(11, 5, 6), (11, 9, 10), (12, 7, 8), (13, 7, 8)],
         "D", "C"),
        # barred wing feathers
        ("runs", [(10, 16, 22), (12, 15, 20), (14, 10, 18),
                  (16, 12, 15)], "D"),
        # claws
        ("put", 18, 8, "N"),
        ("put", 18, 13, "N"),
    ],
}
