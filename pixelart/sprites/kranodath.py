"""Kranodath, bird wyvern. The sail-crested lurker: a dark blue heron-like
body with a big brown-orange sail crest sweeping off the head and
shoulders, pale spots on the flanks, and a long jaw."""

CONFIG = {
    "name": "kranodath",
    "size": (32, 24),
    "compare_to": "../icons/mhwilds/kranodath.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (72, 82, 122, 255),    # dark blue body
        "D": (52, 60, 94, 255),     # darker shade
        "F": (192, 122, 60, 255),   # brown-orange sail
        "P": (150, 158, 192, 255),  # pale spots
        "C": (188, 192, 178, 255),  # pale jaw underside
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        2:  [(6, 10)],                        # sail top
        3:  [(5, 12), (13, 14)],
        4:  [(4, 13), (12, 16)],
        5:  [(3, 14), (11, 18)],              # sail + head
        6:  [(2, 15), (10, 20)],
        7:  [(1, 15), (9, 22)],
        8:  [(1, 15), (9, 24)],               # jaw + body
        9:  [(2, 14), (8, 25)],
        10: [(2, 14), (8, 26)],
        11: [(3, 14), (8, 27)],
        12: [(3, 13), (9, 27)],
        13: [(4, 13), (10, 27)],
        14: [(5, 12), (12, 26)],
        15: [(6, 11), (14, 25)],
        16: [(7, 10), (16, 24)],
        17: [(8, 12), (17, 22)],              # legs
        18: [(8, 11), (18, 21)],
        19: [(8, 8), (10, 10), (18, 18), (20, 20)],
    },
    "fills": [
        # big brown-orange sail
        ("runs", [(2, 6, 10), (3, 5, 12), (4, 4, 13), (5, 3, 14),
                  (6, 2, 15), (7, 1, 15)], "F"),
        ("runs", [(4, 12, 13), (5, 12, 14), (6, 13, 15)], "D", "F"),
        # eye at the sail base
        ("put", 6, 3, "W"),
        # pale jaw underside
        ("runs", [(8, 1, 8), (9, 2, 9)], "C"),
        # pale spots on the flanks
        ("runs", [(10, 17, 18), (11, 20, 21), (12, 16, 17),
                  (13, 19, 20), (14, 21, 22)], "P"),
        # belly shade
        ("runs", [(13, 5, 12), (14, 6, 11), (15, 7, 10), (16, 8, 9)], "D"),
        # claws
        ("put", 19, 8, "W"),
        ("put", 19, 10, "W"),
        ("put", 19, 18, "W"),
        ("put", 19, 20, "W"),
    ],
}
