"""Espinas, flying wyvern. The thorn wyvern: a green hide bristling with
rose thorns, a deep rose horn on the snout, thorn-wing spurs, and a
scaled chest. The espinas archetype its fiery variant derives from."""

CONFIG = {
    "name": "espinas",
    "size": (30, 24),
    "compare_to": "../icons/mhrs/espinas.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (122, 142, 86, 255),   # green hide
        "D": (92, 110, 64, 255),    # darker green
        "R": (206, 92, 92, 255),    # rose thorns
        "C": (222, 204, 172, 255),  # pale chest
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(4, 5), (9, 10)],                # thorn tips
        3:  [(3, 11), (8, 12)],
        4:  [(2, 12), (7, 14)],               # head + thorns
        5:  [(1, 13), (6, 16)],
        6:  [(1, 14), (5, 18)],               # horn + wing thorns
        7:  [(0, 15), (5, 19)],
        8:  [(0, 15), (5, 20)],               # body
        9:  [(0, 15), (5, 21)],
        10: [(0, 15), (5, 21)],
        11: [(0, 15), (5, 21)],
        12: [(0, 15), (5, 21)],
        13: [(0, 15), (5, 21)],
        14: [(0, 15), (6, 21)],
        15: [(1, 15), (7, 21)],
        16: [(1, 15), (9, 21)],
        17: [(2, 15), (11, 21)],
        18: [(3, 14), (13, 21)],
        19: [(4, 13), (16, 21)],
        20: [(5, 12), (19, 21)],
    },
    "fills": [
        # rose thorns bristling over the head and back
        ("runs", [(2, 4, 5), (2, 9, 10), (3, 3, 5), (3, 8, 12),
                  (4, 7, 9), (4, 11, 12), (5, 6, 8), (5, 13, 16),
                  (6, 5, 7), (6, 15, 18)], "R"),
        # deep rose horn on the snout
        ("runs", [(4, 2, 3), (5, 1, 2), (6, 1, 1)], "R"),
        # dark eye
        ("put", 6, 4, "K"),
        # jaw line
        ("runs", [(8, 0, 4)], "K"),
        # scaled pale chest
        ("runs", [(13, 1, 12), (14, 1, 12), (15, 1, 12), (16, 2, 11)], "C"),
        # chest scale dots
        ("runs", [(14, 4, 4), (14, 8, 8), (15, 3, 3), (15, 7, 7),
                  (15, 11, 11)], "D", "C"),
        # back shade
        ("runs", [(17, 3, 14), (18, 4, 13), (19, 5, 12)], "D"),
    ],
}
