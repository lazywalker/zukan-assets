"""Yama Tsukami, elder dragon. The floating forest: a moss-green balloon
body with a ring of hanging whisker-vines below, a dark gaping mouth
hanging at the bottom-left, and wood horns on top."""

CONFIG = {
    "name": "yama-tsukami",
    "size": (30, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (118, 138, 88, 255),   # moss-green body
        "D": (90, 108, 66, 255),    # darker green
        "T": (146, 112, 74, 255),   # wood horns
        "N": (52, 48, 40, 255),     # dark mouth
        "C": (176, 186, 130, 255),  # pale vines
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(8, 9), (14, 15)],               # wood horns
        3:  [(7, 10), (13, 16)],
        4:  [(6, 17)],
        5:  [(5, 18)],
        6:  [(4, 19)],                        # balloon body
        7:  [(3, 20)],
        8:  [(3, 21)],
        9:  [(2, 21)],
        10: [(2, 22)],
        11: [(2, 22)],
        12: [(2, 22)],
        13: [(2, 22)],
        14: [(2, 21)],
        15: [(3, 21)],
        16: [(3, 20)],
        17: [(4, 19)],
        18: [(5, 17)],
        19: [(6, 15)],
        20: [(6, 7), (9, 10), (12, 13)],      # hanging whisker-vines
        21: [(6, 6), (9, 9), (12, 12)],
    },
    "fills": [
        # wood horns on top
        ("runs", [(2, 8, 9), (2, 14, 15), (3, 7, 10), (3, 13, 16)], "T"),
        # dark gaping mouth hanging at the bottom-left
        ("runs", [(17, 5, 11), (18, 6, 10), (19, 7, 9)], "N"),
        ("put", 18, 7, "W"),
        ("put", 18, 9, "W"),
        # pale eye dots on the body
        ("put", 8, 6, "W"),
        ("put", 8, 15, "W"),
        # body spots
        ("runs", [(6, 8, 9), (8, 12, 13), (10, 6, 7), (10, 16, 17),
                  (12, 10, 11), (13, 15, 16), (15, 8, 9)], "D", "G"),
        # body shade
        ("runs", [(16, 4, 19), (17, 5, 18), (18, 6, 16)], "D"),
        # hanging vines
        ("runs", [(20, 6, 7), (20, 9, 10), (20, 12, 13)], "C"),
        ("put", 21, 6, "C"),
        ("put", 21, 9, "C"),
        ("put", 21, 12, "C"),
    ],
}
