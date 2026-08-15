"""Doshaguma, fanged beast. The shaggy guardian bear: a big golden-brown
bulk with a bald red face, small dark eyes, massive forelimbs, and a
grizzled mane crest. The guardian-bear archetype ajarakan derives from."""

CONFIG = {
    "name": "doshaguma",
    "size": (32, 24),
    "compare_to": "../icons/mhwilds/doshaguma.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (186, 142, 88, 255),   # golden-brown fur
        "D": (148, 110, 66, 255),   # darker fur
        "R": (188, 92, 72, 255),    # bald red face
        "N": (70, 46, 40, 255),    # dark eyes / nose
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        2:  [(4, 7), (11, 13)],               # mane crest tufts
        3:  [(3, 14)],
        4:  [(2, 15)],
        5:  [(1, 16)],
        6:  [(1, 17)],                        # head + shoulders
        7:  [(0, 18)],
        8:  [(0, 19)],
        9:  [(0, 19), (20, 22)],              # body + forelimb
        10: [(0, 19), (19, 23)],
        11: [(0, 19), (19, 24)],
        12: [(0, 19), (19, 24)],
        13: [(0, 19), (19, 24)],
        14: [(0, 19), (19, 24)],
        15: [(0, 19), (19, 24)],
        16: [(1, 19), (19, 23)],
        17: [(2, 19), (19, 23)],
        18: [(3, 19), (19, 23)],
        19: [(4, 12), (15, 19), (19, 22)],    # legs + forelimb
        20: [(4, 11), (16, 18), (19, 21)],
        21: [(4, 4), (6, 6), (10, 10), (16, 16), (18, 18), (20, 20)],
    },
    "fills": [
        # grizzled mane crest
        ("runs", [(2, 4, 7), (2, 11, 13), (3, 3, 13), (4, 3, 14)], "D"),
        # bald red face
        ("runs", [(6, 2, 10), (7, 1, 11), (8, 1, 11), (9, 1, 10)], "R"),
        # small dark eyes + nose
        ("put", 7, 3, "N"),
        ("put", 7, 9, "N"),
        ("put", 9, 5, "N"),
        ("put", 9, 6, "N"),
        # forelimb fur shade
        ("runs", [(10, 20, 23), (11, 19, 24), (12, 19, 24)], "D"),
        # belly shade
        ("runs", [(16, 1, 18), (17, 2, 18), (18, 3, 18)], "D"),
        # claws
        ("put", 21, 4, "W"),
        ("put", 21, 6, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 16, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 20, "W"),
    ],
}
