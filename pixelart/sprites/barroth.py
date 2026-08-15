"""Barroth, brute wyvern. Mud-clay hammerhead: a huge rectangular head
almost as tall as the body, topped by a flat clay crown ridge, tiny eye
sunk under the crown, a wide flat mouth gap with blunt teeth, a stocky
horizontal body, thick columnar legs and a blunt heavy tail."""

CONFIG = {
    "name": "barroth",
    "size": (36, 24),
    "compare_to": "../icons/mhrise/barroth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (140, 118, 96, 255),   # gray-brown body
        "D": (105, 88, 70, 255),    # darker shade: rear leg, tail underside
        "O": (200, 122, 58, 255),   # clay crown
        "S": (150, 90, 44, 255),    # crown notch lines
        "L": (172, 148, 116, 255),  # muddy belly band
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(3, 9)],                         # crown top
        3:  [(2, 11)],                        # crown widening
        4:  [(1, 12), (16, 20)],              # head + back hump start
        5:  [(0, 12), (13, 22)],
        6:  [(0, 13), (13, 24)],
        7:  [(0, 13), (12, 26)],
        8:  [(1, 13), (11, 27)],              # mouth gap drawn r8 c2-5
        9:  [(2, 12), (9, 28)],
        10: [(3, 11), (8, 29)],
        11: [(8, 31)],
        12: [(8, 32)],
        13: [(8, 33)],
        14: [(8, 33)],
        15: [(9, 33)],
        16: [(9, 32)],
        17: [(10, 14), (16, 19), (20, 24)],   # legs + belly dip
        18: [(10, 14), (20, 24)],
        19: [(10, 14), (20, 24)],
        20: [(10, 14), (20, 24)],
        21: [(10, 14), (20, 24)],
        22: [(10, 10), (12, 12), (20, 20), (22, 22)],
    },
    "fills": [
        # clay crown ridge with notch lines
        ("runs", [(2, 3, 9), (3, 2, 11), (4, 1, 12)], "O"),
        ("runs", [(2, 5, 6), (3, 7, 8)], "S"),
        # wide flat mouth gap with blunt teeth
        ("runs", [(8, 2, 5)], "K"),
        ("put", 8, 2, "W"),
        ("put", 8, 4, "W"),
        # tiny eye sunk under the crown
        ("put", 6, 3, "W"),
        ("put", 6, 4, "K"),
        # mud patches on the body
        ("runs", [(11, 15, 17), (12, 20, 22), (13, 24, 26)], "D"),
        # belly band along the bottom edge
        ("runs", [(14, 9, 20), (15, 9, 22), (16, 9, 24)], "L"),
        ("runs", [(17, 16, 19)], "L"),
        # tail underside shade
        ("runs", [(15, 26, 33), (16, 25, 32)], "D"),
        # rear leg darker
        ("runs", [(17, 20, 24), (18, 20, 24), (19, 20, 24), (20, 20, 24),
                  (21, 20, 24)], "D"),
        # claws
        ("put", 22, 10, "W"),
        ("put", 22, 12, "W"),
        ("put", 22, 20, "W"),
        ("put", 22, 22, "W"),
    ],
}
