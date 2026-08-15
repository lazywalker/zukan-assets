"""Deviljho, the pickle. Brute wyvern: long horizontal green body, massive
head and jaw with a lighter belly, tiny legs, dark back spikes. Reference:
icons/mhgu/deviljho.png colors + series-standard pickle silhouette.
"""

CONFIG = {
    "name": "deviljho",
    "size": (36, 24),
    "compare_to": "../icons/mhgu/deviljho.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "G": (100, 130, 75, 255),   # pickle green body
        "D": (68, 92, 55, 255),     # dark green: spikes, shade
        "L": (150, 165, 90, 255),   # yellow-green belly
        "R": (150, 30, 25, 255),    # red mouth interior
        "W": (245, 242, 230, 255),  # teeth / eye
    },
    "base": "G",
    "spans": {
        # massive head rows 4-13
        4:  [(2, 8), (20, 21)],
        5:  [(1, 9), (19, 22), (28, 30)],
        6:  [(1, 10), (18, 24), (27, 31)],
        7:  [(1, 11), (16, 25), (26, 32)],
        8:  [(1, 12), (14, 26), (25, 33)],
        9:  [(1, 12), (12, 34)],
        10: [(1, 12), (12, 34)],
        11: [(2, 12), (12, 34)],
        12: [(2, 12), (12, 34)],
        13: [(3, 12), (12, 33)],
        14: [(4, 33)],
        15: [(5, 32)],
        16: [(6, 31)],
        17: [(8, 30)],
        18: [(9, 29)],
        19: [(10, 13), (17, 20), (26, 28)],   # tiny legs
        20: [(10, 13), (17, 20), (26, 28)],
        21: [(10, 10), (12, 12), (17, 17), (19, 19), (26, 26), (28, 28)],
    },
    "fills": [
        # dark back spikes
        ("runs", [(4, 20, 21), (5, 19, 19), (5, 21, 22), (6, 18, 18),
                  (6, 22, 23), (7, 16, 16), (7, 23, 24),
                  (8, 15, 16), (8, 19, 20), (8, 23, 24)], "D"),
        # red mouth interior + white teeth
        ("runs", [(8, 2, 5), (9, 1, 4), (10, 1, 3)], "R"),
        ("put", 8, 2, "W"),
        ("put", 8, 5, "W"),
        ("put", 9, 5, "W"),
        ("put", 10, 4, "W"),
        # eye
        ("put", 6, 8, "WK"),
        # yellow-green belly band, ragged top edge
        ("runs", [(11, 13, 30), (12, 13, 29), (13, 14, 28), (14, 15, 26),
                  (15, 16, 25)], "L"),
        # tail underside shade
        ("runs", [(13, 24, 30), (14, 24, 30), (15, 24, 29), (16, 24, 28)], "D"),
    ],
}
