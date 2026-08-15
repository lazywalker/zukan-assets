"""Kulve Taroth, elder dragon. The gilded behemoth: twin huge horns
arcing up-back clear of the head, a deep bronze face with pale eyes
under them, a massive gold-mantled body with molten fur trim, heavy
clawed limbs."""

CONFIG = {
    "name": "kulve-taroth",
    "size": (36, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (222, 178, 82, 255),   # gold mantle
        "D": (178, 138, 58, 255),   # darker gold
        "B": (110, 84, 66, 255),    # bronze face
        "M": (240, 210, 130, 255),  # molten gold fur
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        1:  [(4, 4), (10, 10)],               # horn tips
        2:  [(3, 5), (9, 11)],                # horn arcs
        3:  [(2, 6), (8, 12)],
        4:  [(2, 7), (8, 13)],                # horn roots
        5:  [(1, 9), (7, 14)],                # head top between horns
        6:  [(0, 11), (6, 17)],               # face + head
        7:  [(0, 13), (5, 19)],
        8:  [(0, 21)],                        # mantle merged
        9:  [(0, 23)],
        10: [(0, 25)],
        11: [(0, 26)],
        12: [(0, 27)],
        13: [(0, 27)],
        14: [(0, 27)],
        15: [(0, 27)],
        16: [(1, 27)],
        17: [(1, 26)],
        18: [(2, 25)],
        19: [(4, 9), (13, 17), (20, 24)],     # limbs
        20: [(4, 8), (14, 16), (21, 23)],
        21: [(4, 4), (6, 6), (14, 14), (21, 21), (23, 23)],
    },
    "fills": [
        # twin horns: near one bright, far one shaded
        ("runs", [(1, 4, 4), (2, 3, 5), (3, 2, 6), (4, 2, 7)], "M"),
        ("runs", [(1, 10, 10), (2, 9, 11), (3, 8, 12), (4, 8, 13)],
         "D"),
        ("put", 3, 8, "M"),
        # bronze face under the horns with pale eyes
        ("runs", [(5, 1, 6), (6, 0, 7), (7, 0, 7)], "B"),
        ("put", 5, 2, "W"),
        ("put", 5, 5, "W"),
        # molten fur trim along the mantle bottom edge
        ("runs", [(16, 1, 27), (17, 1, 26), (18, 2, 25)], "M"),
        ("runs", [(16, 8, 8), (16, 14, 14), (16, 20, 20),
                  (17, 11, 11), (17, 18, 18), (18, 8, 8), (18, 16, 16)],
         "D", "M"),
        # mantle plate seams
        ("runs", [(10, 14, 15), (12, 18, 19), (14, 22, 23)], "D", "G"),
        # limbs darker
        ("runs", [(19, 13, 17), (19, 20, 24), (20, 14, 16),
                  (20, 21, 23)], "D"),
        # claws
        ("put", 21, 4, "W"),
        ("put", 21, 6, "W"),
        ("put", 21, 14, "W"),
        ("put", 21, 21, "W"),
        ("put", 21, 23, "W"),
    ],
}
