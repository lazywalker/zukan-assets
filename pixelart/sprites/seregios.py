"""Seregios, flying wyvern. The thousand blades: tigrex's proven
big-headed runner skeleton dressed in seregios identity; tall V brow
crest with red spur tips, cream beaked jaw with fangs, blade spikes
rising from the shoulder with red tips, gold body with blade-scale
dashes, banded tail, feet with toe claws."""

CONFIG = {
    "name": "seregios",
    "size": (32, 24),
    "compare_to": "../icons/mhgu/seregios.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (206, 168, 74, 255),   # gold scales
        "D": (160, 128, 54, 255),   # darker gold
        "R": (202, 82, 52, 255),    # red blade tips
        "C": (232, 206, 158, 255),  # pale chest / jaw
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(5, 5), (9, 9), (29, 30)],       # V crest tips + tail tip
        3:  [(4, 10), (14, 15), (19, 20), (28, 31)],
        4:  [(3, 11), (14, 16), (19, 21), (27, 31)],
        5:  [(2, 12), (14, 16), (19, 21), (26, 31)],
        6:  [(1, 13), (14, 16), (19, 21), (25, 31)],
        7:  [(1, 13), (13, 24), (25, 30)],
        8:  [(5, 13), (13, 25), (25, 28)],    # mouth gap c1-4
        9:  [(2, 12), (12, 25)],
        10: [(2, 11), (12, 25)],
        11: [(3, 11), (12, 25)],
        12: [(12, 25)],
        13: [(12, 24)],
        14: [(13, 23)],
        15: [(13, 22)],
        16: [(14, 18), (22, 26)],
        17: [(14, 18), (22, 26)],
        18: [(14, 17), (22, 25)],
        19: [(14, 17), (22, 25)],
        20: [(13, 17), (22, 25)],
        21: [(13, 13), (15, 15), (22, 22), (24, 24)],
    },
    "fills": [
        # V brow crest dark with red spur tips
        ("runs", [(2, 5, 5), (2, 9, 9), (3, 4, 10), (4, 3, 10)], "D"),
        ("put", 2, 5, "R"),
        ("put", 2, 9, "R"),
        # blade spikes rising from the shoulder
        ("runs", [(3, 14, 15), (3, 19, 20), (4, 14, 16), (4, 19, 21)],
         "D"),
        ("put", 3, 14, "R"),
        ("put", 3, 19, "R"),
        # eye + fangs in the dark mouth gap
        ("put", 6, 4, "K"),
        ("put", 7, 2, "W"),
        ("put", 7, 4, "W"),
        ("put", 8, 3, "W"),
        # cream lower jaw
        ("runs", [(9, 2, 12), (10, 2, 11), (11, 3, 11)], "C"),
        # cream belly
        ("runs", [(12, 12, 19), (13, 12, 19), (14, 13, 18),
                  (15, 13, 18)], "C"),
        # blade-scale dashes down the flank
        ("runs", [(9, 15, 16), (10, 18, 19), (11, 20, 21)], "D"),
        # tail bands
        ("runs", [(2, 29, 30), (3, 28, 30), (4, 27, 30), (5, 26, 30),
                  (6, 25, 28)], "D"),
        # leg scale dashes
        ("runs", [(17, 15, 17), (17, 23, 25)], "D"),
        # claws
        ("put", 21, 13, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 22, "W"),
        ("put", 21, 24, "W"),
    ],
}
