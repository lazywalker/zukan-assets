"""Tzitzi-Ya-Ku, bird wyvern. The flash parrot: blue-purple body with two
huge orange crescent fins flaring from the sides of the head, a bulbous
pale snout, long slim legs, and a fin on the back."""

CONFIG = {
    "name": "tzitzi-ya-ku",
    "size": (32, 24),
    "compare_to": "../icons/mhw/tzitzi-ya-ku.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (102, 112, 162, 255),  # blue-purple body
        "D": (74, 82, 126, 255),    # darker shade
        "O": (228, 142, 62, 255),   # orange crescent fins
        "P": (158, 168, 202, 255),  # pale snout
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(7, 9), (14, 16)],               # crescent fin tips
        4:  [(6, 10), (13, 17)],
        5:  [(5, 11), (12, 18)],
        6:  [(4, 12), (11, 19)],
        7:  [(3, 12), (11, 20)],              # head between fins
        8:  [(2, 12), (10, 21)],
        9:  [(2, 12), (10, 22)],              # snout bulge
        10: [(3, 11), (9, 23)],
        11: [(3, 11), (9, 24)],
        12: [(4, 11), (9, 24)],
        13: [(4, 10), (10, 23)],
        14: [(5, 10), (11, 22)],
        15: [(6, 9), (13, 21)],
        16: [(7, 9), (15, 20)],
        17: [(8, 12), (16, 19)],              # long legs
        18: [(8, 11), (17, 18)],
        19: [(8, 10), (17, 17)],
        20: [(8, 8), (10, 10), (17, 17)],
    },
    "fills": [
        # orange crescent fins with pale rims
        ("runs", [(3, 7, 9), (3, 14, 16), (4, 6, 10), (4, 13, 17),
                  (5, 5, 9), (5, 13, 18)], "O"),
        ("runs", [(5, 10, 11), (5, 17, 18), (6, 11, 12), (6, 18, 19)],
         "W", "O"),
        # pale bulbous snout
        ("runs", [(8, 2, 6), (9, 2, 7), (10, 3, 7)], "P"),
        # dark eye on the head
        ("put", 7, 8, "K"),
        # back fin ridge
        ("runs", [(10, 21, 23), (11, 22, 24), (12, 22, 24)], "D"),
        # belly shade
        ("runs", [(13, 6, 19), (14, 7, 18), (15, 8, 16)], "D"),
        # claws
        ("put", 20, 8, "W"),
        ("put", 20, 10, "W"),
        ("put", 20, 17, "W"),
    ],
}
