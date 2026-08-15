"""Kulu-Ya-Ku, bird wyvern. Bipedal archetype: big head with a long dark
beak, red-and-yellow crest feathers, white face, cyan eye, tan spotted body,
small wing, long legs. Reference: icons/mhrise/kulu-ya-ku.png.
"""

CONFIG = {
    "name": "kulu-ya-ku",
    "size": (28, 24),
    "compare_to": "../icons/mhrise/kulu-ya-ku.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "T": (228, 170, 121, 255),  # tan body
        "t": (170, 115, 70, 255),   # dark tan: spots, wing, leg shade
        "N": (48, 50, 84, 255),     # navy: beak, legs, tail edge
        "R": (222, 84, 62, 255),    # red crest feathers
        "Y": (240, 200, 60, 255),   # yellow crest feathers
        "W": (245, 242, 235, 255),  # white face
        "C": (60, 185, 185, 255),   # cyan eye
    },
    "base": "T",
    "spans": {
        # crest feathers rows 1-4
        1:  [(5, 6)],
        2:  [(4, 7), (22, 23)],
        3:  [(3, 8), (21, 24)],
        # head rows 4-9 + beak; tail fan upper right
        4:  [(3, 9), (20, 24)],
        5:  [(2, 10), (19, 25)],
        6:  [(1, 11), (18, 25)],
        7:  [(1, 6), (8, 11), (18, 24)],      # beak gap c7? no: beak c1-6
        8:  [(2, 5), (8, 12), (17, 22)],      # beak tip + head bottom + tail
        # body rows 9-16
        9:  [(8, 20)],
        10: [(8, 21)],
        11: [(8, 19)],
        12: [(8, 19)],
        13: [(9, 18)],
        14: [(9, 17)],
        15: [(10, 16)],
        16: [(11, 15)],
        # long legs
        17: [(11, 12), (15, 16)],
        18: [(11, 12), (15, 16)],
        19: [(11, 12), (15, 16)],
        20: [(11, 12), (15, 16)],
        21: [(10, 13), (14, 17)],             # feet
        22: [(10, 10), (13, 13)],             # toe claws
    },
    "fills": [
        # crest: red + yellow feathers
        ("runs", [(1, 5, 6), (2, 4, 5), (3, 3, 5)], "R"),
        ("runs", [(2, 6, 7), (3, 6, 8)], "Y"),
        # beak navy
        ("runs", [(6, 1, 3), (7, 1, 6), (8, 2, 5)], "N"),
        # white face patch
        ("runs", [(5, 6, 10), (6, 5, 11), (7, 8, 11)], "W"),
        # eye
        ("put", 6, 7, "C"),
        ("put", 6, 8, "K"),
        # tail fan: navy edge band + spots
        ("runs", [(4, 22, 24), (5, 22, 25), (6, 22, 25), (7, 21, 24)], "N"),
        # body spots
        ("runs", [(10, 12, 13), (11, 15, 16), (12, 10, 11), (12, 17, 18),
                  (13, 13, 14), (14, 15, 16)], "t"),
        # wing: darker tan with navy feather tips
        ("runs", [(11, 9, 14), (12, 9, 14), (13, 10, 14), (14, 10, 14)], "t"),
        ("runs", [(12, 10, 11), (12, 13, 13), (13, 11, 12)], "T"),
        ("runs", [(14, 10, 11), (14, 13, 14)], "N"),
        # legs navy + feet
        ("runs", [(r, 11, 12) for r in range(17, 21)]
               + [(r, 15, 16) for r in range(17, 21)]
               + [(21, 10, 13), (21, 14, 17)], "N"),
    ],
}
