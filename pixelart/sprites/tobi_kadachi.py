"""Tobi-Kadachi, slender fanged wyvern. Low-slung serpentine quadruped.
Reference: icons/mhrise/tobi-kadachi.png; white fur, navy markings, red
eye, gliding membrane along the flanks, long tapering tail.
"""

CONFIG = {
    "name": "tobi-kadachi",
    "size": (36, 24),
    "compare_to": "../icons/mhrise/tobi-kadachi.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "W": (226, 231, 223, 255),  # white fur
        "G": (170, 181, 189, 255),  # gray-blue shade
        "N": (48, 50, 84, 255),     # navy markings, paws, tail tip
        "R": (205, 45, 55, 255),    # red eye
    },
    "base": "W",
    "spans": {
        # head rows 6-11, wedge snout
        5:  [(16, 19)],
        6:  [(2, 8), (15, 20)],
        7:  [(1, 9), (12, 22), (28, 30)],
        8:  [(1, 9), (12, 22), (27, 31)],
        9:  [(1, 9), (11, 24), (26, 32)],
        10: [(2, 9), (10, 26), (25, 33)],
        11: [(3, 9), (10, 34)],
        12: [(10, 34)],
        13: [(10, 33)],
        14: [(11, 32)],
        15: [(11, 30)],
        16: [(12, 29)],
        17: [(12, 16), (20, 24)],             # legs
        18: [(12, 16), (20, 24)],
        19: [(12, 15), (20, 23)],
        20: [(12, 15), (20, 23)],             # paws
        21: [(12, 12), (14, 14), (20, 20), (22, 22)],  # claws
    },
    "fills": [
        # navy head stripe over the crown + down the neck
        ("runs", [(5, 16, 19), (6, 4, 8), (7, 4, 9), (8, 5, 9)], "N"),
        # red eye
        ("put", 8, 2, "R"),
        # snout shade
        ("runs", [(9, 1, 4), (10, 2, 5)], "G"),
        # navy back stripe along the spine
        ("runs", [(8, 13, 17), (9, 12, 15), (10, 14, 16)], "N"),
        # flank spots
        ("runs", [(11, 13, 14), (11, 18, 19), (12, 16, 17), (12, 21, 22),
                  (13, 14, 15), (13, 19, 20), (14, 17, 18), (15, 19, 20),
                  (16, 18, 19)], "N"),
        # tail bands + navy tip
        ("runs", [(8, 27, 30), (9, 26, 28), (10, 25, 27), (11, 29, 30),
                  (12, 31, 33), (13, 29, 33), (14, 28, 32), (15, 27, 30),
                  (16, 26, 29)], "N"),
        # gliding membrane: gray band along the lower flank
        ("runs", [(13, 11, 13), (14, 11, 12), (15, 11, 12), (16, 12, 15),
                  (16, 24, 27)], "G"),
        # navy paws
        ("runs", [(19, 12, 15), (19, 20, 23), (20, 12, 15), (20, 20, 23)], "N"),
        # claws
        ("put", 21, 12, "N"),
        ("put", 21, 14, "N"),
        ("put", 21, 20, "N"),
        ("put", 21, 22, "N"),
    ],
}
