"""Somnacanth, leviathan. The sleeping siren shark, side view: a big
blunt cream-faced head under a sweeping dark navy mane, a sleek lavender
body with a cream belly, a small arm fin with orange shell spikes tucked
under the chin, and a broad navy tail fan sweeping down past the hip."""

CONFIG = {
    "name": "somnacanth",
    "size": (52, 24),
    "compare_to": "../icons/mhrise/somnacanth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "L": (172, 148, 190, 255),   # lavender body
        "D": (132, 108, 152, 255),   # darker lavender shade
        "C": (238, 230, 214, 255),   # cream face / belly
        "M": (58, 56, 84, 255),      # navy mane / tail
        "O": (214, 110, 80, 255),    # orange shells
        "W": (246, 242, 230, 255),
    },
    "base": "L",
    "spans": {
        3:  [(3, 6)],                          # mane bump
        4:  [(2, 9)],
        5:  [(1, 12)],
        6:  [(0, 15)],
        7:  [(0, 20)],
        8:  [(0, 26)],                         # back only
        9:  [(0, 29)],
        10: [(1, 33), (34, 45)],               # tail fan roots at the hip
        11: [(2, 33), (34, 47)],
        12: [(3, 32), (33, 48)],
        13: [(4, 33), (33, 49)],
        14: [(5, 34), (33, 49)],
        15: [(6, 34), (34, 48)],
        16: [(8, 34), (36, 46)],
        17: [(10, 33), (39, 43)],
        18: [(13, 31)],
        19: [(16, 28)],
    },
    "fills": [
        # navy mane sweeping over the crown and down the back
        ("runs", [(3, 3, 6), (4, 2, 9), (5, 1, 12), (6, 0, 13),
                  (7, 0, 9)], "M"),
        ("runs", [(7, 13, 20), (8, 18, 24), (9, 22, 27),
                  (10, 25, 29)], "M"),
        # big cream face under the mane
        ("runs", [(7, 1, 5), (8, 1, 6), (9, 1, 7), (10, 2, 8),
                  (11, 3, 9), (12, 4, 10), (13, 5, 10)], "C"),
        # droopy sleeping eye under the mane fringe
        ("put", 8, 5, "K"),
        ("put", 9, 5, "W"),
        ("put", 9, 6, "K"),
        # tiny low mouth
        ("put", 13, 3, "K"),
        # cream belly along the bottom edge
        ("runs", [(13, 11, 26), (14, 12, 28), (15, 13, 29),
                  (16, 14, 28)], "C"),
        # navy tail fan with lavender rays
        ("runs", [(10, 34, 45), (11, 34, 47),
                  (12, 33, 48), (13, 33, 49), (14, 33, 49),
                  (15, 34, 48), (16, 36, 46), (17, 39, 43)], "M"),
        ("runs", [(11, 40, 40),
                  (12, 40, 40), (13, 41, 41), (14, 42, 42),
                  (15, 42, 42), (16, 41, 41)], "L", "M"),
        ("runs", [(12, 45, 45), (13, 46, 46), (14, 46, 46),
                  (15, 45, 45)], "L", "M"),
        # darker top shade along the back
        ("runs", [(8, 25, 24), (9, 27, 26), (10, 30, 30)], "D"),
        # arm fin with orange shell spikes under the chin
        ("runs", [(16, 10, 12), (17, 11, 13)], "D"),
        ("put", 17, 12, "O"),
        ("put", 17, 13, "O"),
        ("put", 16, 11, "O"),
    ],
}
