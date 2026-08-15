"""Rathalos side view. Flying wyvern: frontal-ish horned head at the left,
the signature fan wing spreading up-right (red finger bones radiating
through the cream membrane, deep scallops between fingers), compact body,
spiked tail curling below the wing, splayed toes."""

CONFIG = {
    "name": "rathalos",
    "size": (36, 24),
    "compare_to": "../icons/mh4u/rathalos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (166, 53, 38, 255),
        "D": (112, 32, 25, 255),
        "C": (214, 176, 116, 255),
        "S": (152, 112, 70, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        # wing: leading edge up to the tip, trailing edge scalloped by
        # three fingers (tips at r2 c23, r5 c26, r7-8 c27)
        1:  [(3, 3), (19, 21)],
        2:  [(2, 3), (17, 23)],
        3:  [(2, 4), (15, 21)],
        4:  [(2, 5), (14, 25)],
        5:  [(2, 6), (13, 26)],
        6:  [(1, 6), (7, 8), (12, 23)],
        7:  [(1, 7), (7, 8), (11, 27)],
        8:  [(1, 6), (7, 9), (10, 27)],
        9:  [(1, 5), (7, 9), (10, 23)],
        10: [(3, 6), (7, 9), (11, 22)],
        11: [(1, 4), (5, 10)],
        12: [(5, 17), (19, 19), (21, 21), (23, 23)],
        13: [(6, 17), (18, 24)],
        14: [(7, 17), (18, 25)],
        15: [(7, 17), (18, 25)],
        16: [(8, 16), (22, 27)],
        17: [(9, 11), (13, 15), (24, 27)],
        18: [(9, 11), (13, 15), (25, 26)],
        19: [(9, 11), (13, 14)],
        20: [(9, 11), (12, 15)],
        21: [(8, 9), (11, 12)],
        22: [(8, 8), (11, 11)],
    },
    "fills": [
        # wing membrane: cream right of the leading-edge arm
        ("runs", [(2, 19, 23), (3, 17, 21), (4, 16, 25), (5, 15, 26),
                  (6, 14, 23), (7, 13, 27), (8, 12, 27), (9, 12, 23),
                  (10, 13, 22)], "C"),
        # three red finger bones radiating from the wrist to the tips
        ("runs", [(2, 21, 23), (3, 20, 21), (4, 19, 21), (5, 17, 18),
                  (6, 15, 16)], "R"),
        ("runs", [(4, 24, 25), (5, 22, 26), (6, 19, 23), (7, 17, 20),
                  (8, 15, 17)], "R"),
        ("runs", [(7, 24, 27), (8, 23, 27), (9, 19, 23), (10, 18, 22)],
         "R"),
        # scale dashes in the membrane panels
        ("runs", [(3, 17, 18), (4, 16, 17), (5, 19, 20), (7, 14, 15),
                  (8, 13, 13), (8, 20, 21), (9, 16, 18), (10, 15, 16)],
         "S", "C"),
        # horn + lower jaw
        ("runs", [(1, 3, 3), (2, 2, 3), (3, 2, 4), (4, 2, 4), (10, 3, 5)],
         "C"),
        # far leg + belly + tail underside
        ("runs", [(17, 15, 18), (18, 15, 18), (19, 15, 18), (20, 15, 18)],
         "D"),
        ("put", 14, 10, "DDDD"),
        ("put", 15, 10, "DDDD"),
        ("put", 16, 11, "DDD"),
        ("put", 15, 19, "DD"),
        ("put", 16, 18, "DDD"),
        # brow, eye, fang
        ("put", 4, 2, "KK"),
        ("put", 5, 2, "WK"),
        ("put", 10, 1, "W"),
    ],
}
