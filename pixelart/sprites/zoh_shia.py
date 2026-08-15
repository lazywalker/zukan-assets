"""Zoh Shia, construct. The white prophecy: a pale construct dragon grown
from the guardians' root; twin thin gold crown horns over a small skull
with a dark eye, a neck step into a slim body, wide wing-arms whose
bottom edge is scalloped with gold seams, column legs, and a burning
core low in the chest."""

CONFIG = {
    "name": "zoh-shia",
    "size": (36, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (224, 222, 216, 255),  # pale construct plating
        "D": (186, 184, 178, 255),  # darker plating
        "Y": (236, 182, 84, 255),   # gold energy lines
        "R": (198, 92, 74, 255),    # burning core
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(6, 6), (11, 11)],               # crown horn tips
        3:  [(5, 7), (10, 12)],               # crown horns
        4:  [(4, 8), (9, 13), (18, 18)],      # skull + wing blade + spike
        5:  [(3, 9), (8, 15), (17, 18)],
        6:  [(3, 10), (7, 17), (16, 19)],
        7:  [(3, 10), (7, 19)],
        8:  [(4, 11), (6, 21)],
        9:  [(2, 22)],                        # body top merged
        10: [(2, 23)],
        11: [(2, 23)],
        12: [(3, 22)],
        13: [(4, 21)],
        14: [(6, 20)],
        15: [(8, 12), (17, 21)],              # legs
        16: [(8, 12), (17, 21)],
        17: [(8, 8), (10, 10), (17, 17), (19, 19)],
    },
    "fills": [
        # thin gold crown horns
        ("runs", [(2, 6, 6), (2, 11, 11), (3, 5, 7), (3, 10, 12)], "Y"),
        # skull shading + dark eye
        ("runs", [(4, 7, 8), (5, 7, 9)], "D"),
        ("put", 5, 5, "K"),
        # mouth notch shadow
        ("runs", [(6, 3, 4)], "D"),
        # wing-arm plating with scalloped gold seams
        ("runs", [(5, 10, 15), (6, 11, 17), (7, 11, 19), (8, 7, 21)],
         "D"),
        ("runs", [(7, 13, 13), (7, 17, 17), (8, 12, 12), (8, 16, 16),
                  (8, 20, 21)], "Y", "D"),
        # wing spike gold
        ("put", 4, 18, "Y"),
        ("put", 5, 17, "Y"),
        ("put", 6, 16, "Y"),
        # burning core low in the chest
        ("runs", [(11, 3, 5), (12, 3, 5)], "R"),
        # body shade along the bottom
        ("runs", [(12, 6, 21), (13, 6, 20), (14, 7, 19)], "D"),
        # far leg darker + claws
        ("runs", [(15, 17, 21), (16, 17, 21)], "D"),
        ("put", 17, 8, "W"),
        ("put", 17, 10, "W"),
        ("put", 17, 17, "W"),
        ("put", 17, 19, "W"),
    ],
}
