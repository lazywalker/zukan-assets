"""Duramboros, brute wyvern. The hunchback ram: a huge moss-capped hump
dominating the back, a small sunk head, two club tails (one raised, one
low), and thick legs."""

CONFIG = {
    "name": "duramboros",
    "size": (38, 24),
    "compare_to": "../icons/mhgu/duramboros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (140, 100, 70, 255),   # brown hide
        "D": (104, 72, 50, 255),    # darker shade
        "C": (222, 204, 172, 255),  # cream hump cap
        "M": (112, 140, 82, 255),   # moss patches
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(14, 18)],                       # hump top
        3:  [(12, 21)],
        4:  [(10, 24)],
        5:  [(8, 26), (28, 29)],              # hump + raised club tip
        6:  [(6, 28), (27, 31)],
        7:  [(4, 30), (26, 33)],
        8:  [(2, 31), (24, 34)],              # head + body + club
        9:  [(1, 32)],
        10: [(1, 33)],
        11: [(2, 34)],
        12: [(2, 35)],
        13: [(3, 35)],
        14: [(4, 35)],
        15: [(5, 34)],
        16: [(6, 33)],
        17: [(8, 12), (18, 22), (26, 31)],    # legs + low club
        18: [(8, 12), (18, 22), (26, 31)],
        19: [(8, 11), (19, 21), (27, 30)],
        20: [(8, 11), (19, 21), (27, 30)],
        21: [(8, 8), (10, 10), (19, 19), (21, 21), (27, 27), (29, 29)],
    },
    "fills": [
        # cream hump cap with moss patches
        ("runs", [(2, 14, 18), (3, 12, 21), (4, 10, 24), (5, 8, 22),
                  (6, 6, 20)], "C"),
        ("runs", [(3, 15, 16), (4, 13, 14), (4, 18, 19), (5, 11, 12),
                  (5, 16, 17)], "M", "C"),
        # small sunk head with an eye
        ("runs", [(8, 2, 5), (9, 1, 4), (10, 1, 4)], "D"),
        ("put", 9, 3, "W"),
        # raised club: dark with cream rim
        ("runs", [(5, 28, 29), (6, 27, 31), (7, 26, 33), (8, 24, 28)],
         "D"),
        ("runs", [(6, 30, 31), (7, 31, 33)], "C", "D"),
        # belly band along the bottom edge
        ("runs", [(13, 4, 22), (14, 5, 24), (15, 6, 25), (16, 7, 24)],
         "C"),
        # low club
        ("runs", [(17, 26, 31), (18, 26, 31), (19, 27, 30),
                  (20, 27, 30)], "D"),
        # legs darker
        ("runs", [(17, 18, 22), (18, 18, 22), (19, 19, 21),
                  (20, 19, 21)], "D"),
        # claws
        ("put", 21, 8, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 19, "W"),
        ("put", 21, 21, "W"),
        ("put", 21, 27, "W"),
        ("put", 21, 29, "W"),
    ],
}
