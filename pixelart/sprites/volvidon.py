"""Volvidon, fanged beast. The rolling armadillo: an orange ball body with
a pale under-carriage, a face set on top with a big yellow eye, and four
stubby legs."""

CONFIG = {
    "name": "volvidon",
    "size": (28, 24),
    "compare_to": "../icons/mhrise/volvidon.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (206, 122, 58, 255),   # orange shell
        "D": (158, 90, 42, 255),    # darker shell
        "C": (226, 204, 164, 255),  # pale under-carriage
        "Y": (232, 190, 70, 255),   # big eye
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        4:  [(8, 10)],                        # face top
        5:  [(6, 13)],
        6:  [(5, 15)],
        7:  [(3, 16)],
        8:  [(2, 17)],                        # ball
        9:  [(2, 18)],
        10: [(1, 19)],
        11: [(1, 19)],
        12: [(1, 20)],
        13: [(1, 20)],
        14: [(2, 20)],
        15: [(2, 19)],
        16: [(3, 18)],
        17: [(4, 16)],
        18: [(6, 14)],
        19: [(7, 9), (12, 14)],               # legs
        20: [(7, 8), (13, 13)],
    },
    "fills": [
        # face set on top with a big yellow eye
        ("runs", [(5, 6, 12), (6, 5, 14)], "C"),
        ("put", 6, 7, "K"),
        ("put", 6, 8, "Y"),
        # small mouth
        ("put", 7, 9, "K"),
        # shell segment bands
        ("runs", [(7, 15, 16), (8, 14, 17), (9, 14, 18), (10, 14, 18),
                  (11, 15, 19), (12, 15, 19)], "D", "O"),
        # pale under-carriage along the bottom edge
        ("runs", [(14, 3, 19), (15, 3, 18), (16, 4, 17), (17, 5, 15)],
         "C"),
        # legs
        ("runs", [(19, 7, 9), (19, 12, 14)], "D"),
        # claws
        ("put", 20, 7, "W"),
        ("put", 20, 13, "W"),
    ],
}
