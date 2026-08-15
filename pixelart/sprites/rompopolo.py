"""Rompopolo, brute wyvern. The gas bag: a bloated purple body sagging
with round cyan venom sacs, a small skull with red eyes and a thin
beak-needle pointing down, stubby legs."""

CONFIG = {
    "name": "rompopolo",
    "size": (34, 24),
    "compare_to": "../icons/mhwilds/rompopolo.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (122, 106, 132, 255),  # purple gas-hide
        "D": (90, 76, 98, 255),     # darker shade
        "C": (142, 205, 210, 255),  # cyan venom sacs
        "T": (202, 192, 170, 255),  # beak-needle
        "R": (216, 60, 60, 255),    # red eyes
        "W": (246, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        4:  [(11, 14), (20, 22)],             # sac bumps
        5:  [(9, 24)],
        6:  [(7, 26)],
        7:  [(5, 27)],
        8:  [(3, 28)],
        9:  [(2, 28)],
        10: [(1, 28)],                        # head front
        11: [(1, 27)],
        12: [(1, 1), (3, 26)],                # beak needle + body
        13: [(1, 1), (4, 25)],
        14: [(4, 24)],
        15: [(6, 23)],
        16: [(8, 22)],
        17: [(10, 12), (16, 20)],             # legs
        18: [(10, 11), (17, 19)],
        19: [(10, 10), (18, 18)],
    },
    "fills": [
        # round cyan sacs with dark rims, sagging along the body
        ("runs", [(5, 12, 15), (6, 10, 18), (7, 9, 13)], "C"),
        ("runs", [(6, 21, 25), (7, 20, 26), (8, 18, 24)], "C"),
        ("runs", [(9, 22, 27), (10, 23, 27), (11, 22, 26)], "C"),
        ("runs", [(10, 4, 9), (11, 4, 9), (12, 4, 8)], "C"),
        # sac rims
        ("runs", [(7, 9, 9), (8, 18, 18), (9, 22, 22), (12, 4, 4)],
         "D", "C"),
        # beak needle, pale
        ("runs", [(12, 1, 1), (13, 1, 1)], "T"),
        ("runs", [(10, 1, 4), (11, 1, 5)], "T"),
        # red eyes on the small skull
        ("put", 8, 3, "R"),
        ("put", 9, 3, "R"),
        # belly shade
        ("runs", [(13, 5, 20), (14, 6, 20), (15, 7, 19), (16, 9, 18)], "D"),
        # claws
        ("put", 19, 10, "W"),
        ("put", 19, 18, "W"),
    ],
}
