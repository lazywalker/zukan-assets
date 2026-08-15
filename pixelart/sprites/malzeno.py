"""Malzeno, elder dragon. The crimson knight: a silver-white dragon with
crimson wing membranes and chest, elegant curved horns, and a long
blade-tipped tail."""

CONFIG = {
    "name": "malzeno",
    "size": (34, 24),
    "compare_to": "../icons/mhrs/malzeno.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "S": (212, 210, 206, 255),  # silver-white scales
        "D": (172, 168, 164, 255),  # darker silver
        "R": (178, 56, 62, 255),    # crimson wings / chest
        "r": (134, 38, 46, 255),    # darker crimson
        "W": (246, 242, 230, 255),
    },
    "base": "S",
    "spans": {
        2:  [(4, 5), (8, 9)],                 # horn tips
        3:  [(3, 6), (7, 10)],
        4:  [(2, 7), (6, 12)],                # horns + wing top
        5:  [(1, 8), (5, 15)],
        6:  [(1, 9), (4, 17)],                # head + wing
        7:  [(0, 10), (4, 19)],
        8:  [(0, 11), (4, 21)],               # body + wing
        9:  [(0, 12), (4, 22)],
        10: [(0, 12), (4, 23)],
        11: [(0, 12), (4, 23)],
        12: [(0, 12), (4, 23)],
        13: [(0, 12), (4, 23)],
        14: [(0, 12), (4, 23)],
        15: [(0, 12), (4, 23)],
        16: [(1, 12), (4, 22)],
        17: [(1, 12), (4, 21)],
        18: [(2, 12), (5, 20)],
        19: [(2, 12), (6, 19)],               # legs + tail blade
        20: [(3, 12), (8, 18)],
        21: [(4, 6), (9, 12), (11, 14)],      # legs + tail tip
    },
    "fills": [
        # curved horns silver-dark
        ("runs", [(2, 4, 5), (2, 8, 9), (3, 3, 6), (3, 7, 10)], "D"),
        # crimson wing membranes with darker edges
        ("runs", [(4, 6, 12), (5, 5, 15), (6, 4, 17), (7, 4, 19),
                  (8, 4, 21), (9, 4, 22), (10, 4, 23), (11, 4, 23)], "R"),
        ("runs", [(10, 18, 23), (11, 19, 23), (12, 19, 23),
                  (13, 19, 23), (14, 19, 23), (15, 19, 23)], "r", "R"),
        # dark eye
        ("put", 6, 3, "K"),
        # crimson chest
        ("runs", [(10, 1, 8), (11, 1, 8), (12, 1, 8), (13, 1, 8)], "R"),
        # body shade
        ("runs", [(16, 1, 12), (17, 2, 12), (18, 3, 12)], "D"),
        # tail blade dark
        ("runs", [(19, 12, 19), (20, 12, 18)], "r"),
    ],
}
