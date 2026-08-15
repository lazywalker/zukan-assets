"""Basarios, flying wyvern. The sleeping rock: a lumpy grey-green boulder
pile with a small tucked-in face, stubby legs, and moss tufts. The
basarios archetype its variants derive from."""

CONFIG = {
    "name": "basarios",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/basarios.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (138, 148, 124, 255),  # grey-green rock
        "D": (104, 114, 92, 255),   # darker rock
        "C": (188, 192, 168, 255),  # pale rock face
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        4:  [(7, 12)],                        # boulder top
        5:  [(5, 15)],
        6:  [(4, 17)],
        7:  [(3, 18)],
        8:  [(2, 19)],                        # face zone
        9:  [(1, 20)],
        10: [(1, 21)],
        11: [(1, 21)],
        12: [(1, 21)],
        13: [(2, 21)],
        14: [(2, 21)],
        15: [(3, 20)],
        16: [(4, 19)],
        17: [(5, 17)],
        18: [(7, 15)],
        19: [(7, 9), (11, 13)],               # legs
        20: [(7, 8), (12, 12)],
    },
    "fills": [
        # tucked-in face: pale panel with closed eyes
        ("runs", [(7, 4, 9), (8, 3, 10), (9, 3, 10), (10, 3, 9)], "C"),
        ("runs", [(8, 5, 5), (8, 8, 8)], "D", "C"),
        # small dark mouth
        ("runs", [(10, 5, 7)], "K"),
        # rock seams
        ("runs", [(5, 9, 10), (6, 12, 13), (7, 14, 15), (11, 4, 5),
                  (12, 16, 17), (14, 6, 7), (15, 15, 16)], "D", "G"),
        # moss tufts
        ("runs", [(4, 8, 10), (5, 6, 7)], "C", "G"),
        # boulder shade
        ("runs", [(15, 4, 19), (16, 5, 18), (17, 6, 16), (18, 8, 14)], "D"),
        # claws
        ("put", 20, 7, "W"),
        ("put", 20, 12, "W"),
    ],
}
