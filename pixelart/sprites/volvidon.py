"""Volvidon, fanged beast. The rolling armadillo: a red carapace ball with
dark segment cracks, a green face set low on the front with a big yellow
eye, an orange tongue hanging out, and a pale under-carriage on stubby
legs."""

CONFIG = {
    "name": "volvidon",
    "size": (28, 24),
    "compare_to": "../icons/mhrise/volvidon.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (204, 86, 54, 255),
        "D": (150, 58, 40, 255),
        "C": (226, 204, 164, 255),
        "G": (150, 175, 80, 255),
        "O": (232, 140, 90, 255),
        "Y": (232, 190, 70, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "R",
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
        # green face filling the front-lower quadrant of the ball
        ("runs", [(5, 8, 12), (6, 5, 11), (7, 3, 11), (8, 2, 10),
                  (9, 2, 8)], "G"),
        # big yellow eye with the pupil toward the front
        ("runs", [(6, 6, 8), (7, 6, 8)], "Y", "G"),
        ("put", 6, 5, "K"),
        ("put", 7, 5, "K"),
        # open mouth, tongue hanging over the front edge
        ("runs", [(9, 2, 7)], "K", "G"),
        ("runs", [(10, 2, 4), (11, 2, 3), (12, 2, 3)], "O"),
        # shell segment cracks over the ball
        ("runs", [(7, 13, 16), (8, 12, 17), (9, 12, 18), (10, 12, 19),
                  (11, 13, 19), (12, 13, 20), (13, 14, 20)], "D"),
        ("runs", [(9, 6, 8), (10, 8, 10), (12, 4, 6), (13, 8, 10),
                  (14, 10, 12)], "D"),
        # pale under-carriage along the bottom edge
        ("runs", [(14, 2, 9), (15, 2, 18), (16, 3, 17), (17, 4, 15)], "C"),
        # legs and claws
        ("runs", [(19, 7, 9), (19, 12, 14)], "D"),
        ("put", 20, 7, "W"),
        ("put", 20, 9, "W"),
        ("put", 20, 12, "W"),
        ("put", 20, 14, "W"),
    ],
}
