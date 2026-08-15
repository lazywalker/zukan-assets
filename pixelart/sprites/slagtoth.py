"""Slagtoth, herbivore. The droopy wallow: a wide low green lump with
drooping jowls, mossy diamonds along the back, a pale throat, stubby
legs nearly hidden under the body."""

CONFIG = {
    "name": "slagtoth",
    "size": (32, 24),
    "compare_to": "../icons/mh4u/slagtoth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (122, 146, 92, 255),   # green hide
        "D": (92, 112, 68, 255),    # darker shade
        "M": (172, 186, 122, 255),  # moss diamonds
        "C": (196, 202, 160, 255),  # pale throat
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        5:  [(6, 14)],                        # head top
        6:  [(4, 16)],
        7:  [(3, 18), (18, 20)],
        8:  [(2, 20), (17, 23)],
        9:  [(1, 22), (16, 25)],
        10: [(1, 24), (15, 27)],
        11: [(0, 26), (14, 28)],              # jowls droop left
        12: [(0, 27), (13, 29)],
        13: [(1, 28), (12, 29)],
        14: [(2, 28)],
        15: [(3, 27)],
        16: [(4, 26)],
        17: [(5, 10), (13, 16), (19, 24)],    # legs
        18: [(5, 9), (14, 15), (20, 23)],
        19: [(5, 5), (7, 7), (14, 14), (21, 21), (23, 23)],
    },
    "fills": [
        # droopy eye on the jowl
        ("put", 7, 4, "K"),
        ("put", 8, 4, "W"),
        # pale throat under the chin
        ("runs", [(9, 2, 6), (10, 2, 6), (11, 1, 5)], "C"),
        # moss diamonds along the back
        ("runs", [(7, 19, 20), (8, 18, 21), (9, 18, 21), (10, 17, 20)],
         "M"),
        ("runs", [(10, 22, 26), (11, 21, 27), (12, 20, 26)], "M"),
        ("runs", [(13, 13, 16), (14, 13, 16)], "M"),
        # belly shade
        ("runs", [(13, 17, 27), (14, 17, 27), (15, 17, 26),
                  (16, 18, 25)], "D"),
        # claws
        ("put", 19, 5, "W"),
        ("put", 19, 7, "W"),
        ("put", 19, 14, "W"),
        ("put", 19, 21, "W"),
        ("put", 19, 23, "W"),
    ],
}
