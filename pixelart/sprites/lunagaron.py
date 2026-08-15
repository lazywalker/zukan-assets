"""Lunagaron, fanged wyvern. The wolf: head raised in a howl at the upper
left, pointed muzzle, dark mane sweeping down the neck, sleek pale body,
bushy plume tail sweeping down behind, slim legs with red claws."""

CONFIG = {
    "name": "lunagaron",
    "size": (30, 24),
    "compare_to": "../icons/mhrs/lunagaron.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (198, 204, 216, 255),  # pale silver fur
        "D": (148, 156, 172, 255),  # fur shade
        "M": (72, 74, 92, 255),     # dark mane / muzzle top
        "V": (196, 74, 74, 255),    # red claws
        "W": (245, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        2:  [(2, 4)],                          # ear
        3:  [(1, 5)],
        4:  [(0, 6), (6, 7)],                  # muzzle + neck
        5:  [(0, 6), (7, 8)],                  # snout tip col 0
        6:  [(1, 7), (8, 9)],
        7:  [(1, 8), (8, 10)],
        8:  [(2, 10)],                         # mane base
        9:  [(3, 17)],
        10: [(4, 20)],
        11: [(4, 22)],
        12: [(4, 23)],                         # body
        13: [(5, 23)],
        14: [(6, 22)],
        15: [(7, 21)],
        16: [(8, 20)],                         # hip
        17: [(9, 15), (18, 20)],               # legs + plume start
        18: [(9, 14), (18, 21)],
        19: [(9, 12), (19, 22)],
        20: [(10, 11), (20, 22)],
        21: [(10, 10), (21, 21)],
    },
    "fills": [
        # dark muzzle top + howling mouth line
        ("runs", [(3, 1, 5), (4, 0, 5), (5, 0, 3)], "M"),
        ("runs", [(5, 4, 6)], "K"),
        # ear inner
        ("runs", [(2, 3, 3)], "D"),
        # dark mane sweeping down the neck
        ("runs", [(6, 6, 9), (7, 7, 10), (8, 8, 10), (9, 10, 13),
                  (10, 11, 15), (11, 12, 16)], "M"),
        # fur shade along the belly
        ("runs", [(13, 6, 18), (14, 7, 17), (15, 8, 16), (16, 9, 15)],
         "D"),
        # bushy plume tail, dark edge
        ("runs", [(17, 18, 20), (18, 18, 21), (19, 19, 22), (20, 20, 22),
                  (21, 21, 21)], "M"),
        # eye
        ("put", 4, 4, "K"),
        # red claws
        ("put", 21, 10, "V"),
        ("put", 21, 21, "V"),
    ],
}
