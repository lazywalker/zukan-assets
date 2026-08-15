"""Velkhana, elder dragon. The ice dragon: small crowned head at the left,
slender neck, horizontal silver body, a fan of ice shards spread ABOVE the
back with deep-blue bones, long tail ending in an ice blade, thin legs."""

CONFIG = {
    "name": "velkhana",
    "size": (36, 24),
    "compare_to": "../icons/mhrs/velkhana.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "S": (210, 215, 225, 255),  # silver-white body
        "I": (140, 190, 230, 255),  # ice blue shards
        "B": (80, 130, 190, 255),   # deep blue: bones, shade
        "W": (240, 244, 250, 255),  # eye
    },
    "base": "S",
    "spans": {
        2:  [(2, 3), (6, 7)],                 # crown horns
        3:  [(1, 4), (5, 8)],
        4:  [(1, 8), (14, 25)],
        5:  [(1, 9), (12, 27)],
        6:  [(1, 10), (12, 28)],
        7:  [(1, 11), (13, 28)],
        8:  [(1, 12), (14, 27)],
        9:  [(2, 25), (15, 26)],
        10: [(3, 25)],
        11: [(4, 26)],
        12: [(5, 26)],
        13: [(5, 26)],
        14: [(6, 25), (27, 28)],
        15: [(7, 24), (28, 30)],
        16: [(8, 24), (29, 31)],
        17: [(9, 23), (30, 32)],
        18: [(10, 23), (30, 32)],
        19: [(11, 22), (29, 31)],
        20: [(12, 21), (28, 29)],
        21: [(13, 13), (16, 16), (19, 19), (27, 27), (29, 29)],
    },
    "fills": [
        # crown horns, ice blue
        ("runs", [(2, 2, 3), (3, 1, 3), (4, 1, 2)], "I"),
        ("runs", [(2, 6, 7), (3, 5, 8), (4, 5, 7)], "I"),
        # white eye
        ("put", 5, 3, "W"),
        # neck ice stripe
        ("runs", [(5, 7, 8), (6, 8, 9), (7, 9, 10), (8, 10, 11)], "I"),
        # wing: fan of ice shards with deep blue bones
        ("runs", [(4, 14, 25), (5, 12, 27), (6, 12, 28), (7, 13, 28),
                  (8, 14, 27), (9, 15, 26)], "I"),
        ("runs", [(5, 13, 13), (6, 13, 13), (7, 14, 14), (8, 15, 16),
                  (9, 16, 17)], "B"),
        # deep blue shading on the rear body
        ("runs", [(13, 20, 26), (14, 20, 26), (15, 20, 24)], "B"),
        # tail ice blade
        ("runs", [(15, 28, 30), (16, 29, 31), (17, 30, 32)], "B"),
        # claws
        ("runs", [(21, 13, 13), (21, 16, 16), (21, 19, 19), (21, 27, 27),
                  (21, 29, 29)], "B"),
    ],
}
