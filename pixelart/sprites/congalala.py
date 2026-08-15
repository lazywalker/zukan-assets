"""Congalala, fanged beast. The pink baboon king: a big pink body sitting
hunched on its rear, a huge dark face plate with a pale muzzle and yellow
tusks, a scruffy mane crest, and clawed arms held forward. The conga
archetype the variants derive from."""

CONFIG = {
    "name": "congalala",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/congalala.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (222, 130, 140, 255),  # pink fur
        "D": (178, 92, 104, 255),   # darker pink
        "V": (82, 64, 70, 255),     # dark face plate
        "Y": (234, 198, 88, 255),   # yellow tusks
        "C": (228, 200, 168, 255),  # pale muzzle
        "W": (246, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        2:  [(8, 9), (13, 14)],               # mane tufts
        3:  [(6, 15)],
        4:  [(4, 17)],
        5:  [(3, 18)],
        6:  [(2, 19)],
        7:  [(2, 20)],
        8:  [(1, 21)],
        9:  [(1, 21)],
        10: [(1, 22)],                        # round body
        11: [(0, 22)],
        12: [(0, 22)],
        13: [(0, 22)],
        14: [(1, 22)],
        15: [(1, 21)],
        16: [(2, 20)],
        17: [(3, 19)],
        18: [(4, 17)],
        19: [(6, 15), (18, 20)],              # arms + feet
        20: [(6, 14), (17, 20)],
        21: [(6, 6), (8, 8), (10, 10), (12, 12), (17, 17), (19, 19)],
    },
    "fills": [
        # huge dark face plate with a pale muzzle
        ("runs", [(4, 6, 15), (5, 4, 17), (6, 3, 17), (7, 2, 18),
                  (8, 2, 18), (9, 2, 18), (10, 3, 18)], "V"),
        ("runs", [(9, 5, 15), (10, 6, 16), (11, 6, 16), (12, 7, 16)],
         "C"),
        # nostrils
        ("put", 10, 9, "K"),
        ("put", 10, 13, "K"),
        # yellow tusks
        ("runs", [(12, 8, 9), (12, 13, 14)], "Y"),
        # pale eyes
        ("put", 7, 6, "W"),
        ("put", 7, 13, "W"),
        # scruffy mane crest
        ("runs", [(2, 8, 9), (2, 13, 14), (3, 6, 8), (3, 13, 15)], "D"),
        # belly shade
        ("runs", [(15, 2, 19), (16, 3, 18), (17, 4, 17), (18, 5, 15)], "D"),
        # arms with claws
        ("runs", [(19, 6, 15), (20, 6, 14)], "D"),
        ("put", 21, 6, "W"),
        ("put", 21, 8, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 17, "W"),
        ("put", 21, 19, "W"),
    ],
}
