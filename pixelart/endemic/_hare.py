"""Hare archetype: sitting hare facing left, two long upright ears, round
head with a dot eye and a split nose, compact body over big haunches,
front paws together. Fur colors are species identity."""

CONFIG = {
    "name": "_hare",
    "size": (26, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (176, 150, 116, 255),  # fur
        "D": (136, 112, 84, 255),   # ears / shade
        "C": (238, 228, 212, 255),  # belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(6, 7), (10, 11)],
        4:  [(6, 7), (10, 11)],
        5:  [(5, 8), (10, 12)],
        6:  [(5, 12)],
        7:  [(4, 12)],
        8:  [(4, 12)],
        9:  [(4, 11)],
        10: [(5, 19)],
        11: [(5, 20)],
        12: [(6, 20)],
        13: [(6, 20)],
        14: [(7, 19)],
        15: [(8, 18)],
        16: [(9, 17)],
        17: [(9, 10), (13, 16)],
        18: [(9, 9), (11, 11), (13, 13), (15, 15)],
    },
    "fills": [
        # long ears darker inside
        ("runs", [(3, 6, 7), (4, 6, 7), (3, 10, 11), (4, 10, 11)], "D"),
        # face: dot eye + split nose
        ("put", 7, 6, "K"),
        ("put", 9, 4, "D"),
        # haunch shade
        ("runs", [(12, 14, 20), (13, 14, 20), (14, 13, 19), (15, 12, 18)],
         "D"),
        # belly + paws pale
        ("runs", [(9, 4, 5), (10, 5, 7), (11, 6, 8)], "C"),
        ("runs", [(17, 9, 10), (17, 13, 16)], "C"),
    ],
}
