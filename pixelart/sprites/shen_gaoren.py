"""Shen Gaoren, carapaceon. The skull-carrier giant, drawn in the front
pose of its icon: a colossal bone dragon skull dome with a dark seam,
red ridge strokes and glowing red eye sockets, pillar legs flanking it,
and the small red crab with yellow claws peeking out below."""

CONFIG = {
    "name": "shen-gaoren",
    "size": (34, 24),
    "compare_to": "../icons/mhfu/shen-gaoren.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (196, 192, 164, 255),   # bone
        "D": (150, 144, 120, 255),   # dark bone shade
        "C": (230, 226, 204, 255),   # pale rim
        "R": (200, 60, 44, 255),     # red ridge / crab
        "E": (150, 36, 30, 255),     # dark red
        "Y": (230, 190, 60, 255),    # yellow claws
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(12, 21)],                          # skull top
        2:  [(10, 23)],
        3:  [(9, 24)],
        4:  [(8, 25)],
        5:  [(8, 25)],
        6:  [(7, 26)],
        7:  [(7, 26)],
        8:  [(7, 26)],
        9:  [(7, 26)],
        10: [(7, 26)],
        11: [(7, 26)],
        12: [(3, 6), (7, 26), (27, 30)],         # legs + skull
        13: [(3, 6), (7, 26), (27, 30)],
        14: [(3, 6), (8, 25), (27, 30)],
        15: [(3, 6), (12, 21), (27, 30)],        # crab face under skull
        16: [(3, 6), (12, 21), (27, 30)],
        17: [(3, 6), (13, 20), (27, 30)],        # claws
        18: [(3, 6), (13, 20), (27, 30)],
        19: [(3, 6), (14, 19), (27, 30)],
        20: [(2, 7), (15, 18), (26, 31)],        # foot splay
        21: [(2, 7), (16, 17), (26, 31)],
    },
    "fills": [
        # pale crown rim on the skull top
        ("runs", [(1, 13, 20), (2, 11, 22)], "C"),
        # dark seam down the skull front
        ("runs", [(3, 16, 17), (4, 16, 17), (5, 16, 17), (6, 16, 17),
                  (7, 16, 17)], "D"),
        # dark skull sides and jaw bottom
        ("runs", [(6, 7, 8), (7, 7, 8), (8, 7, 8), (9, 7, 8), (10, 7, 8),
                  (11, 7, 8), (6, 25, 26), (7, 25, 26), (8, 25, 26),
                  (9, 25, 26), (10, 25, 26), (11, 25, 26), (14, 9, 24)],
         "D"),
        # red ridge strokes on the dome
        ("runs", [(4, 10, 11), (5, 9, 10), (6, 9, 10), (4, 22, 23),
                  (5, 23, 24), (6, 23, 24), (3, 14, 15), (3, 18, 19)],
         "R"),
        # dark eye sockets with red glow
        ("runs", [(8, 10, 13), (8, 20, 23), (9, 10, 13), (9, 20, 23),
                  (10, 10, 12), (10, 21, 23)], "D"),
        ("runs", [(9, 11, 12), (9, 21, 22)], "R", "D"),
        # dark nasal notch
        ("runs", [(11, 15, 18), (12, 15, 18), (13, 16, 17)], "D"),
        # red crab face with beady eyes
        ("runs", [(15, 12, 21), (16, 12, 21)], "R"),
        ("runs", [(15, 14, 15), (15, 18, 19)], "W", "R"),
        ("put", 15, 15, "K"),
        ("put", 15, 18, "K"),
        # yellow claws with pale tips
        ("runs", [(17, 13, 20), (18, 13, 20), (19, 14, 19), (20, 15, 18),
                  (21, 16, 17)], "Y"),
        ("runs", [(21, 16, 17)], "W", "Y"),
        # leg joint lines and dark feet
        ("runs", [(15, 3, 6), (15, 27, 30), (18, 3, 6), (18, 27, 30),
                  (21, 2, 7), (21, 26, 31)], "D"),
    ],
}
