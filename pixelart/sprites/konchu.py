"""Konchu, neopteron. The pill bug: a smooth round shell dome over a tiny
body, small legs peeking below, a blunt face at the left."""

CONFIG = {
    "name": "konchu",
    "size": (24, 24),
    "compare_to": "../icons/mh4u/konchu.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (148, 142, 118, 255),  # khaki shell
        "D": (114, 108, 88, 255),   # darker shell
        "C": (208, 200, 176, 255),  # pale face / underside
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        6:  [(7, 13)],                        # shell top
        7:  [(5, 15)],
        8:  [(4, 16)],
        9:  [(3, 17)],
        10: [(2, 18)],                        # dome
        11: [(2, 18)],
        12: [(2, 18)],
        13: [(2, 17)],
        14: [(3, 16)],
        15: [(4, 15)],
        16: [(5, 13)],
        17: [(6, 8), (11, 13)],               # legs
        18: [(6, 6), (8, 8), (11, 11), (13, 13)],
    },
    "fills": [
        # blunt pale face at the left
        ("runs", [(10, 2, 4), (11, 2, 4), (12, 2, 4), (13, 2, 4)], "C"),
        # tiny dark eye
        ("put", 11, 3, "K"),
        # shell ridge lines
        ("runs", [(8, 8, 8), (9, 7, 7), (10, 6, 6), (11, 6, 6),
                  (12, 7, 7), (13, 8, 8)], "D", "G"),
        # shell shade right
        ("runs", [(9, 13, 17), (10, 14, 18), (11, 14, 18)], "D"),
        # legs
        ("put", 18, 6, "D"),
        ("put", 18, 8, "D"),
        ("put", 18, 11, "D"),
        ("put", 18, 13, "D"),
    ],
}
