"""Seltas Queen, neopteron. The armored tank: a massive green beetle with
a heavy horn crown, yellow eyes under the brow, spiked shoulder plates,
and thick legs. Big and wide."""

CONFIG = {
    "name": "seltas-queen",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/seltas-queen.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (104, 144, 88, 255),   # green armor
        "D": (74, 108, 62, 255),    # darker green
        "Y": (232, 190, 74, 255),   # yellow eyes / horn tips
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(3, 5), (9, 10)],                # horn crown tips
        3:  [(2, 6), (8, 11), (16, 17)],
        4:  [(1, 7), (7, 12), (15, 19)],
        5:  [(1, 8), (6, 14), (14, 21)],
        6:  [(1, 9), (5, 15), (13, 23)],
        7:  [(0, 10), (5, 16), (12, 25)],     # head + shoulders + back
        8:  [(0, 11), (5, 17), (11, 26)],
        9:  [(0, 12), (5, 18), (11, 27)],
        10: [(0, 13), (6, 18), (11, 27)],
        11: [(1, 13), (7, 18), (12, 26)],
        12: [(1, 13), (8, 18), (13, 25)],
        13: [(2, 12), (9, 17), (14, 24)],
        14: [(3, 11), (10, 16), (16, 23)],
        15: [(4, 10), (18, 22)],
        16: [(4, 9), (19, 21)],
        17: [(5, 12), (15, 19)],              # legs
        18: [(5, 11), (16, 18)],
        19: [(5, 9), (16, 17)],
    },
    "fills": [
        # yellow horn crown tips
        ("runs", [(2, 3, 5), (2, 9, 10), (3, 2, 4)], "Y"),
        # angry yellow eyes under the brow
        ("runs", [(6, 2, 5), (7, 1, 6)], "D"),
        ("put", 7, 2, "Y"),
        ("put", 7, 5, "Y"),
        # spiked shoulder plates
        ("runs", [(8, 5, 17), (9, 5, 18), (10, 6, 18)], "D"),
        ("runs", [(8, 8, 9), (8, 13, 14), (9, 11, 12), (9, 15, 16)],
         "Y", "D"),
        # back shell shade
        ("runs", [(12, 14, 25), (13, 15, 24), (14, 17, 23)], "D"),
        # legs darker
        ("runs", [(17, 15, 19), (18, 16, 18)], "D"),
        # claws
        ("put", 19, 5, "W"),
        ("put", 19, 9, "W"),
        ("put", 19, 16, "W"),
    ],
}
