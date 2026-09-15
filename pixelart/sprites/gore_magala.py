"""Gore Magala, elder dragon. The gothic cloak: the body hidden under a
near-black symmetric wing cloak with purple streaks, orange feelers
curling from the hood, no visible eyes, and a tailed tip below."""

CONFIG = {
    "name": "gore-magala",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/gore-magala.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "E": (32, 26, 42, 255),
        "D": (56, 44, 74, 255),
        "P": (96, 72, 110, 255),
        "O": (222, 132, 60, 255),
    },
    "base": "E",
    "spans": {
        2:  [(13, 14), (19, 20)],             # feeler tips
        3:  [(1, 10), (12, 14), (19, 21), (23, 32)],
        4:  [(0, 11), (13, 20), (22, 33)],
        5:  [(0, 33)],
        6:  [(0, 33)],
        7:  [(0, 33)],
        8:  [(1, 32)],
        9:  [(1, 32)],
        10: [(2, 31)],
        11: [(2, 31)],
        12: [(3, 30)],
        13: [(4, 29)],
        14: [(5, 28)],
        15: [(7, 26)],
        16: [(9, 24)],
        17: [(12, 21)],
        18: [(13, 20)],
        19: [(14, 19)],
        20: [(15, 18)],
        21: [(16, 17)],                       # tail tip
    },
    "fills": [
        # orange feelers curling from the hood
        ("runs", [(2, 13, 14), (2, 19, 20), (3, 12, 13), (3, 20, 21)], "O"),
        # hood crest band
        ("runs", [(4, 14, 19), (5, 15, 18)], "D"),
        # purple streaks down the cloak
        ("runs", [(6, 5, 9), (6, 24, 28), (9, 8, 12), (9, 21, 25),
                  (12, 6, 10), (12, 23, 27), (15, 10, 12), (15, 21, 23)],
         "D"),
        # wing-arm claws at the cloak edge
        ("put", 4, 0, "O"),
        ("put", 4, 33, "O"),
        ("put", 5, 1, "O"),
        ("put", 5, 32, "O"),
        # hood glints where eyes would be, if it had them
        ("runs", [(6, 14, 15), (6, 18, 19)], "P"),
        # tail tip highlight
        ("put", 21, 16, "P"),
        ("put", 21, 17, "P"),
    ],
}
