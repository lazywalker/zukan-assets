"""Valstrax, elder dragon. The silver jet: a sleek silver dragon with
crimson wings swept back like rocket exhaust, a pointed crest horn, blue
eyes, and bladed wing tips."""

CONFIG = {
    "name": "valstrax",
    "size": (34, 24),
    "compare_to": "../icons/mhgu/valstrax.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "S": (188, 190, 198, 255),  # silver body
        "D": (146, 148, 158, 255),  # darker silver
        "R": (196, 62, 66, 255),    # crimson jet wings
        "r": (150, 44, 52, 255),    # darker crimson
        "B": (86, 120, 176, 255),   # blue eyes
        "C": (226, 228, 234, 255),  # pale silver chest
        "W": (246, 242, 230, 255),
    },
    "base": "S",
    "spans": {
        2:  [(5, 7)],                         # crest tip
        3:  [(4, 8), (9, 10)],
        4:  [(3, 9), (8, 13)],                # crest + wing top
        5:  [(2, 10), (7, 15)],
        6:  [(1, 11), (6, 17)],               # head + jet wing
        7:  [(1, 12), (5, 19)],
        8:  [(0, 13), (4, 21)],               # body + jet wing
        9:  [(0, 14), (4, 22)],
        10: [(0, 15), (4, 23)],
        11: [(0, 15), (4, 23)],
        12: [(0, 15), (4, 23)],
        13: [(0, 15), (4, 23)],
        14: [(0, 15), (4, 23)],
        15: [(0, 15), (4, 22)],
        16: [(0, 15), (4, 21)],
        17: [(1, 15), (4, 20)],
        18: [(1, 15), (4, 18)],
        19: [(2, 14), (5, 15)],               # legs
        20: [(2, 13), (6, 14)],
        21: [(2, 2), (4, 4), (7, 7), (13, 13)],
    },
    "fills": [
        # crimson jet wings with darker exhaust edges
        ("runs", [(4, 8, 13), (5, 7, 15), (6, 6, 17), (7, 5, 19),
                  (8, 4, 21), (9, 4, 22), (10, 4, 23), (11, 4, 23)], "R"),
        ("runs", [(10, 18, 23), (11, 19, 23), (12, 19, 23),
                  (13, 19, 23), (14, 19, 23)], "r", "R"),
        # pointed crest horn
        ("runs", [(2, 5, 7), (3, 4, 8), (4, 3, 7)], "D"),
        # blue eyes
        ("put", 6, 4, "B"),
        ("put", 6, 7, "B"),
        # silver chest
        ("runs", [(10, 1, 8), (11, 1, 8), (12, 1, 8), (13, 1, 8)], "C"),
        # body shade
        ("runs", [(16, 1, 15), (17, 2, 15), (18, 2, 15)], "D"),
        # claws
        ("put", 21, 2, "W"),
        ("put", 21, 4, "W"),
        ("put", 21, 7, "W"),
        ("put", 21, 13, "W"),
    ],
}
