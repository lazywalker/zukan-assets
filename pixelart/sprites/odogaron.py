"""Odogaron, fanged wyvern. Crimson hound: low-slung hunched body, open
jaw with white fangs, dark stripe bands on the back, long straight tail,
four long thin legs with white claws. Colors: crimson (178,52,46), dark
stripe/underside (122,34,30), white fangs and claws."""

CONFIG = {
    "name": "odogaron",
    "size": (34, 24),
    "compare_to": "../icons/mhw/odogaron.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (178, 52, 46, 255),    # crimson body
        "D": (122, 34, 30, 255),    # dark red: stripes, underside
        "W": (245, 242, 230, 255),  # fangs / claws / eye
    },
    "base": "R",
    "spans": {
        4:  [(2, 3), (6, 7)],                 # ears
        5:  [(1, 5), (6, 8)],
        6:  [(1, 7), (7, 10)],
        7:  [(1, 8), (8, 12)],
        8:  [(1, 9), (9, 14)],
        9:  [(1, 8), (10, 16)],
        10: [(1, 8), (10, 22)],               # body + tail root
        11: [(2, 8), (10, 23)],
        12: [(3, 8), (10, 24)],
        13: [(4, 8), (10, 25)],
        14: [(5, 8), (10, 26)],
        15: [(6, 8), (11, 27)],               # tail underside tapers
        16: [(7, 8), (13, 26)],
        17: [(8, 8), (10, 21), (25, 26)],     # tail tip droops
        18: [(10, 21), (25, 25)],
        19: [(10, 12), (14, 16), (19, 21)],
        20: [(10, 12), (14, 16), (19, 21)],
        21: [(10, 10), (12, 12), (15, 15), (17, 17), (20, 20)],
    },
    "fills": [
        # ears + eye
        ("runs", [(4, 2, 2), (4, 6, 6)], "D"),
        ("put", 6, 3, "W"),
        # open jaw: dark gape + fangs
        ("runs", [(8, 1, 4), (9, 1, 3)], "D"),
        ("put", 8, 2, "W"),
        ("put", 9, 2, "W"),
        # dark stripe bands on the back and tail
        ("runs", [(r, a, b) for r, a, b in ((10, 12, 13), (11, 12, 13),
                  (11, 15, 16), (12, 15, 16), (12, 18, 19), (13, 18, 19),
                  (13, 21, 22), (14, 21, 22), (12, 21, 22), (13, 22, 23),
                  (14, 23, 24))], "D"),
        # underside shade + tail underside
        ("runs", [(16, 10, 11), (17, 10, 11), (18, 10, 12)], "D"),
        ("runs", [(14, 24, 26), (15, 25, 27), (16, 26, 28), (17, 26, 27)],
         "D"),
        # claws
        ("put", 21, 10, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 14, "W"),
        ("put", 21, 16, "W"),
        ("put", 21, 19, "W"),
        ("put", 21, 21, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 17, "W"),
    ],
}
