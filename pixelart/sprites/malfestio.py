"""Malfestio, bird wyvern. The night owl, drawn in the round front of its
icon: a plump blue body with cream ear tufts, a wide dark face with big
yellow eyes and a small beak, a gold collar band across the chest, folded
wing bars at the sides and gold talons below."""

CONFIG = {
    "name": "malfestio",
    "size": (32, 24),
    "compare_to": "../icons/mhgu/malfestio.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (70, 90, 140, 255),     # blue body
        "D": (52, 68, 108, 255),     # dark blue shade
        "Y": (230, 190, 70, 255),    # gold collar / eyes / talons
        "C": (225, 215, 185, 255),   # cream tufts / belly
        "E": (40, 35, 50, 255),      # dark face
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(10, 11), (20, 21)],                # ear tuft tips
        2:  [(9, 12), (19, 22)],
        3:  [(8, 13), (18, 23), (14, 17)],       # tufts + head top
        4:  [(8, 23)],
        5:  [(7, 24)],
        6:  [(6, 25)],
        7:  [(6, 25)],
        8:  [(5, 26)],
        9:  [(5, 26)],
        10: [(5, 26)],                           # collar row
        11: [(5, 26)],
        12: [(4, 27)],                           # body widest
        13: [(4, 27)],
        14: [(4, 27)],
        15: [(5, 26)],
        16: [(5, 26)],
        17: [(6, 25)],
        18: [(7, 24)],
        19: [(8, 11), (13, 18), (20, 23)],       # talons
        20: [(9, 10), (14, 17), (21, 22)],
    },
    "fills": [
        # cream ear tufts
        ("runs", [(1, 10, 11), (1, 20, 21), (2, 9, 12), (2, 19, 22),
                  (3, 8, 10), (3, 21, 23)], "C"),
        # wide dark face with big yellow eyes
        ("runs", [(4, 8, 23), (5, 8, 23), (6, 8, 23), (7, 7, 24),
                  (8, 7, 24), (9, 8, 23)], "E", "B"),
        ("runs", [(6, 10, 13), (6, 18, 21), (7, 10, 13), (7, 18, 21),
                  (8, 11, 12), (8, 19, 20)], "Y", "E"),
        ("put", 7, 11, "K"),
        ("put", 7, 20, "K"),
        # small pale beak
        ("runs", [(8, 15, 16)], "C", "E"),
        ("put", 9, 15, "C"),
        ("put", 9, 16, "C"),
        # gold collar band across the chest
        ("runs", [(10, 6, 25), (11, 5, 26)], "Y", "B"),
        ("runs", [(10, 9, 10), (10, 14, 15), (10, 19, 20), (11, 7, 8),
                  (11, 12, 13), (11, 17, 18), (11, 22, 23)], "D", "Y"),
        # folded wing bars at the sides
        ("runs", [(12, 4, 7), (13, 4, 7), (14, 4, 7), (15, 5, 8),
                  (16, 5, 8), (17, 6, 9), (12, 24, 27), (13, 24, 27),
                  (14, 24, 27), (15, 23, 26), (16, 23, 26), (17, 22, 25)],
         "D", "B"),
        ("runs", [(13, 4, 7), (15, 5, 8), (13, 24, 27), (15, 23, 26)],
         "E", "D"),
        # pale belly patch
        ("runs", [(13, 11, 20), (14, 11, 20), (15, 11, 20), (16, 12, 19),
                  (17, 13, 18)], "C", "B"),
        # gold talons
        ("runs", [(19, 8, 11), (19, 20, 23), (20, 9, 10), (20, 21, 22),
                  (19, 13, 18), (20, 14, 17)], "Y", "B"),
        ("put", 20, 9, "D"),
        ("put", 20, 22, "D"),
    ],
}
