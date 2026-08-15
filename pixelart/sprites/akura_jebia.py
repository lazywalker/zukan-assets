"""Akura Jebia, temnoceran. The scorpion empress: a crowned head with
pincers at the left, a round armored body, and a segmented tail arching
over the back to a red stinger at the top right."""

CONFIG = {
    "name": "akura-jebia",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (72, 58, 96, 255),     # dark blue-purple shell
        "D": (52, 40, 70, 255),     # darker shell
        "Y": (232, 190, 70, 255),   # crown gold
        "R": (206, 72, 56, 255),    # stinger red
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        1:  [(24, 26)],                       # stinger tip over the back
        2:  [(4, 5), (8, 9), (22, 27)],       # crown tips + tail segment
        3:  [(3, 10), (21, 28)],              # crown band + tail
        4:  [(2, 9), (20, 28)],               # head + tail
        5:  [(1, 10), (19, 28)],              # head + tail base
        6:  [(0, 11), (18, 27)],              # head + body top
        7:  [(0, 12), (12, 26)],              # body + tail root merged
        8:  [(0, 26)],
        9:  [(0, 26)],
        10: [(0, 25)],
        11: [(0, 24)],
        12: [(1, 23)],
        13: [(2, 21)],
        14: [(3, 19)],
        15: [(4, 17)],
        16: [(6, 8), (11, 14), (17, 20)],     # legs
        17: [(6, 8), (11, 14), (17, 20)],
        18: [(6, 6), (8, 8), (11, 11), (13, 13), (17, 17), (19, 19)],
    },
    "fills": [
        # gold crown over the head
        ("runs", [(2, 4, 5), (2, 8, 9), (3, 3, 10)], "Y"),
        # pale eyes under the crown
        ("put", 5, 3, "W"),
        ("put", 5, 6, "W"),
        # tail segments: darker bands
        ("runs", [(2, 22, 27), (3, 21, 28), (4, 20, 28), (5, 19, 28)],
         "D"),
        ("runs", [(3, 24, 25), (4, 23, 24)], "N", "D"),
        # red stinger tip
        ("runs", [(1, 24, 26), (2, 22, 24)], "R", "D"),
        # head shell darker behind the crown
        ("runs", [(4, 6, 9), (5, 7, 10), (6, 8, 11)], "D"),
        # body shade along the bottom
        ("runs", [(13, 3, 20), (14, 4, 18), (15, 5, 16)], "D"),
        # legs darker
        ("runs", [(16, 11, 14), (16, 17, 20), (17, 11, 14),
                  (17, 17, 20)], "D"),
        # claws
        ("put", 18, 6, "W"),
        ("put", 18, 11, "W"),
        ("put", 18, 17, "W"),
    ],
}
