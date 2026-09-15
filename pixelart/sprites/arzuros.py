"""Arzuros, fanged beast. The honey bear: blue-purple pelt with a cream
face and chest, a gold honey pot hugged between the forepaws, orange
claws on every toe, round ears, dark eye over a white muzzle."""

CONFIG = {
    "name": "arzuros",
    "size": (32, 24),
    "compare_to": "../icons/mhrise/arzuros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (88, 72, 118, 255),
        "D": (64, 54, 92, 255),
        "F": (232, 222, 200, 255),
        "O": (222, 124, 52, 255),
        "G": (226, 156, 44, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(4, 6)],
        3:  [(3, 8)],
        4:  [(2, 10), (17, 27)],
        5:  [(1, 11), (15, 28)],
        6:  [(1, 12), (14, 28)],
        7:  [(0, 13), (13, 29)],
        8:  [(0, 13), (12, 29)],
        9:  [(0, 14), (12, 29)],
        10: [(0, 14), (12, 29)],
        11: [(1, 15), (11, 29)],
        12: [(0, 28)],
        13: [(0, 28)],
        14: [(1, 28)],
        15: [(2, 28)],
        16: [(3, 27)],
        17: [(4, 11), (12, 18), (20, 26)],
        18: [(5, 9), (12, 16), (20, 25)],
        19: [(5, 9), (12, 16), (20, 25)],
        20: [(5, 9), (12, 16), (20, 25)],
        21: [(5, 5), (8, 8), (12, 12), (15, 15), (20, 20), (22, 22), (25, 25)],
    },
    "fills": [
        # face: dark cap on the head top, cream face below with white
        # muzzle, dark nose, eye + brow
        ("runs", [(6, 1, 12), (7, 0, 13), (8, 0, 13), (9, 0, 14),
                  (10, 0, 14), (11, 1, 15)], "F"),
        ("runs", [(4, 2, 10), (5, 1, 11)], "D"),
        ("runs", [(7, 0, 3), (8, 0, 4)], "W", "F"),
        ("runs", [(9, 0, 4)], "D", "F"),
        ("put", 7, 0, "K"),
        ("put", 8, 0, "K"),
        ("put", 8, 1, "D"),
        ("put", 7, 4, "D"),
        ("put", 6, 4, "K"),
        ("put", 6, 5, "K"),
        ("put", 3, 5, "O"),
        # chest and belly band along the bottom edge
        ("runs", [(12, 0, 11), (13, 0, 12), (14, 1, 13), (15, 2, 14),
                  (16, 3, 15), (17, 4, 11)], "F"),
        # belly texture on the cream band
        ("runs", [(14, 2, 2), (15, 3, 3), (16, 4, 4), (16, 14, 14),
                  (17, 6, 7), (17, 16, 18)], "D", "F"),
        # honey pot hugged between the forepaws, high enough to break
        # the chin so face and chest do not merge into one cream mass
        ("runs", [(11, 4, 9), (12, 3, 10), (13, 3, 10), (14, 3, 10),
                  (15, 4, 9), (16, 5, 8)], "G", "F"),
        ("runs", [(12, 9, 10), (13, 8, 10), (14, 8, 10), (15, 8, 9),
                  (16, 7, 8)], "D", "G"),
        ("runs", [(11, 4, 9)], "W", "F"),
        ("put", 12, 4, "W"),
        # forepaw wrapping the pot's left side
        ("runs", [(12, 3, 3), (13, 3, 3), (14, 3, 3)], "B", "G"),
        ("put", 15, 3, "O"),
        # grizzled texture on the back and rump
        ("runs", [(5, 20, 22), (6, 17, 18), (6, 25, 27), (7, 14, 16),
                  (7, 26, 28), (8, 24, 25), (9, 26, 28), (10, 13, 15),
                  (10, 25, 26), (11, 24, 28), (13, 20, 26), (14, 20, 27),
                  (15, 22, 27), (16, 22, 26)], "D"),
        # hind quarters shade
        ("runs", [(17, 22, 26), (18, 22, 25), (19, 23, 25)], "D"),
        # orange claws on every toe
        ("runs", [(21, 5, 5), (21, 8, 8), (21, 12, 12), (21, 15, 15),
                  (21, 20, 20), (21, 22, 22), (21, 25, 25)], "O"),
    ],
}
