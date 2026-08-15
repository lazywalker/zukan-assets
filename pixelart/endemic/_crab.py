"""Crab archetype: shell dome with a cream rim, eye stalks with beady
eyes, one big front claw with an open slot (the gap opens through the
silhouette edge so the stroke draws a wedge), pointed legs below."""

CONFIG = {
    "name": "_crab",
    "size": (30, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (170, 96, 60, 255),    # shell
        "D": (130, 70, 44, 255),    # darker shell
        "C": (226, 208, 172, 255),  # cream rim / claw
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        7:  [(10, 19)],
        8:  [(8, 21)],
        9:  [(6, 22)],
        10: [(5, 23)],
        11: [(4, 24)],
        12: [(4, 24)],
        13: [(5, 23)],
        14: [(6, 22)],
        15: [(0, 8), (19, 25)],               # big claw + small claw
        16: [(0, 9), (19, 26)],
        17: [(0, 7), (20, 25)],
        18: [(1, 6), (21, 24)],
        19: [(1, 4), (6, 6), (22, 22), (24, 24)],
        20: [(9, 11), (14, 16), (18, 20)],    # legs
        21: [(9, 9), (11, 11), (14, 14), (16, 16), (18, 18), (20, 20)],
    },
    "fills": [
        # shell dome with a cream rim along the top edge
        ("runs", [(7, 10, 19), (8, 8, 11), (8, 18, 21), (9, 6, 9),
                  (9, 19, 22)], "D"),
        # big claw with an open slot through the silhouette edge
        ("runs", [(15, 0, 8), (16, 0, 9), (17, 0, 7), (18, 1, 6)], "C"),
        ("runs", [(16, 3, 4), (16, 7, 8)], "K"),
        # small claw darker
        ("runs", [(15, 19, 25), (16, 19, 26), (17, 20, 25), (18, 21, 24)],
         "D"),
        # eye on the shell front
        ("put", 11, 7, "W"),
        ("put", 11, 8, "K"),
    ],
}
