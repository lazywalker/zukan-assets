"""Shen Gaoren, carapaceon. The skull-tower giant: a colossal orange crab
carrying a tower of giant skulls on its back, long stilt legs below, and
small claws peeking from under the tower."""

CONFIG = {
    "name": "shen-gaoren",
    "size": (34, 24),
    "compare_to": "../icons/mhfu/shen-gaoren.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (198, 122, 62, 255),   # orange carapace
        "D": (152, 90, 44, 255),    # darker orange
        "C": (226, 210, 184, 255),  # skull bone
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        2:  [(10, 23)],                       # skull tower top
        3:  [(8, 25)],
        4:  [(7, 26)],
        5:  [(6, 27)],
        6:  [(5, 28)],                        # tower widens
        7:  [(4, 29)],
        8:  [(4, 29)],
        9:  [(3, 30)],
        10: [(2, 31)],                        # tower base
        11: [(2, 31)],
        12: [(2, 31)],                        # legs start
        13: [(1, 31), (0, 0)],
        14: [(1, 31), (0, 0)],
        15: [(1, 31)],
        16: [(1, 31)],
        17: [(1, 31)],
        18: [(2, 31)],
        19: [(3, 8), (11, 13), (17, 20), (24, 30)],   # stilt legs
        20: [(3, 7), (12, 12), (18, 19), (25, 29)],
        21: [(3, 3), (5, 5), (12, 12), (18, 18), (25, 25), (27, 27)],
    },
    "fills": [
        # skull faces on the tower: pale rounds with dark sockets
        ("runs", [(2, 10, 23), (3, 8, 25), (4, 7, 26), (5, 6, 27)], "C"),
        ("runs", [(4, 11, 12), (4, 16, 17), (4, 21, 22)], "D", "C"),
        ("runs", [(5, 9, 10), (5, 14, 15), (5, 19, 20), (5, 24, 25)],
         "D", "C"),
        # jaw row on the tower base
        ("runs", [(7, 8, 9), (7, 12, 13), (7, 16, 17), (7, 20, 21),
                  (7, 24, 25)], "D", "C"),
        # tower base shell band
        ("runs", [(9, 3, 30), (10, 2, 31), (11, 2, 31)], "O"),
        ("runs", [(9, 8, 9), (9, 14, 15), (9, 20, 21), (9, 26, 27)],
         "D", "O"),
        # legs striped
        ("runs", [(13, 0, 0), (14, 0, 0)], "D"),
        ("runs", [(19, 4, 6), (19, 12, 12), (19, 18, 19),
                  (19, 25, 27)], "D"),
        # claws peeking at the tower base corners
        ("runs", [(12, 2, 3), (12, 29, 31)], "D"),
        # claws
        ("put", 21, 3, "W"),
        ("put", 21, 5, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 25, "W"),
        ("put", 21, 27, "W"),
    ],
}
