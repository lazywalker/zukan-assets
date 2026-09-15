"""Banbaro, brute wyvern. The moose, drawn in the antler-fan front of its
icon: giant two-pronged white antlers sweeping up and out over a small
dark head, a bulky navy-blue body with a cream muzzle and belly band,
and thick legs."""

CONFIG = {
    "name": "banbaro",
    "size": (40, 24),
    "compare_to": "../icons/mhwi/banbaro.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (245, 242, 238, 255),   # antler white
        "D": (205, 198, 186, 255),   # antler shade
        "B": (75, 85, 125, 255),     # navy body
        "N": (95, 60, 38, 255),      # dark brown head
        "E": (66, 42, 28, 255),      # darker head shade
        "C": (230, 220, 195, 255),   # cream muzzle / belly
    },
    "base": "B",
    "spans": {
        1:  [(7, 9), (30, 32)],                  # antler tips
        2:  [(5, 10), (29, 34)],
        3:  [(4, 11), (28, 35)],
        4:  [(3, 12), (27, 36)],
        5:  [(3, 13), (26, 36)],
        6:  [(3, 13), (15, 24), (26, 36)],       # prong gap + head top
        7:  [(3, 13), (15, 24), (26, 36)],
        8:  [(4, 13), (15, 24), (26, 35)],
        9:  [(5, 14), (15, 24), (25, 34)],       # antler base joins head
        10: [(6, 33)],
        11: [(8, 12), (27, 31)],                 # antler bases curl out
        12: [(15, 24)],                          # head
        13: [(15, 24)],
        14: [(15, 24)],
        15: [(15, 24)],                          # muzzle row
        16: [(14, 25)],                          # body
        17: [(14, 25)],
        18: [(15, 24)],
        19: [(10, 13), (16, 23), (26, 29)],      # legs
        20: [(10, 13), (16, 23), (26, 29)],
        21: [(10, 13), (16, 23), (26, 29)],
    },
    "fills": [
        # white antler fans with shaded lower edge
        ("runs", [(1, 7, 9), (2, 5, 10), (3, 4, 11), (4, 3, 12),
                  (5, 3, 13), (6, 3, 13), (7, 3, 13), (8, 4, 13),
                  (9, 5, 14), (1, 30, 32), (2, 29, 34), (3, 28, 35),
                  (4, 27, 36), (5, 26, 36), (6, 26, 36), (7, 26, 36),
                  (8, 26, 35), (9, 25, 34)], "W", "B"),
        ("runs", [(5, 3, 5), (6, 3, 5), (7, 3, 5), (5, 34, 36),
                  (6, 34, 36), (7, 34, 36), (8, 4, 6), (9, 5, 7),
                  (8, 33, 35), (9, 32, 34), (10, 7, 10), (10, 29, 32),
                  (11, 8, 12), (11, 27, 31)], "D", "W"),
        # dark head with pale muzzle
        ("runs", [(12, 15, 24), (13, 15, 24), (14, 15, 24)], "N", "B"),
        ("runs", [(12, 18, 21)], "E", "N"),
        ("put", 13, 17, "K"),
        ("put", 13, 22, "K"),
        ("runs", [(15, 16, 23)], "C", "N"),
        ("runs", [(15, 18, 19), (15, 20, 21)], "E", "C"),
        # navy body with cream belly band
        ("runs", [(16, 14, 25), (17, 14, 25)], "B"),
        ("runs", [(17, 15, 24), (18, 16, 23)], "C", "B"),
        # thick dark legs with pale claws
        ("runs", [(19, 10, 13), (19, 26, 29), (20, 10, 13), (20, 26, 29),
                  (21, 10, 13), (21, 26, 29), (19, 16, 23), (20, 16, 23),
                  (21, 16, 23)], "E", "B"),
        ("put", 21, 11, "C"),
        ("put", 21, 17, "C"),
        ("put", 21, 22, "C"),
        ("put", 21, 28, "C"),
    ],
}
