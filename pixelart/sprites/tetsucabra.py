"""Tetsucabra, amphibian. The tusked toad, drawn in the front crouch of
its icon: a wide domed head with dark brow horns and glaring green eyes,
the mouth as a transparent gap crossed by two floating white tusk
islands, a plated pale chest between splayed forelegs with white claws."""

CONFIG = {
    "name": "tetsucabra",
    "size": (32, 24),
    "compare_to": "../icons/mh4u/tetsucabra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (206, 118, 60, 255),
        "D": (148, 78, 46, 255),
        "C": (228, 190, 140, 255),
        "G": (150, 175, 80, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        2:  [(7, 8), (23, 24)],               # horn tips
        3:  [(6, 9), (22, 25)],
        4:  [(5, 10), (13, 18), (21, 26)],    # horns + dome top
        5:  [(5, 26)],
        6:  [(4, 27)],
        7:  [(3, 28)],
        8:  [(3, 28)],                        # head bottom
        9:  [(4, 5), (26, 27)],               # tusk islands cross the mouth gap
        10: [(4, 5), (26, 27)],
        11: [(2, 29)],                        # lower jaw
        12: [(1, 30)],                        # shoulders
        13: [(1, 30)],
        14: [(1, 30)],
        15: [(2, 29)],
        16: [(2, 29)],
        17: [(3, 28)],
        18: [(5, 10), (12, 19), (21, 26)],    # forelegs + crouch
        19: [(4, 9), (12, 19), (22, 27)],
        20: [(3, 8), (12, 19), (23, 28)],
        21: [(3, 3), (5, 5), (7, 7), (24, 24), (26, 26), (28, 28)],
    },
    "fills": [
        # dark brow horns
        ("runs", [(2, 7, 8), (2, 23, 24), (3, 6, 9), (3, 22, 25),
                  (4, 5, 10), (4, 21, 26)], "D"),
        # angry brows slanting over the eyes
        ("runs", [(5, 8, 11), (5, 20, 23), (6, 8, 8), (6, 23, 23)], "D"),
        # glaring green eyes with dark pupils
        ("runs", [(6, 9, 10), (6, 21, 22), (7, 8, 10), (7, 21, 23)], "G"),
        ("put", 7, 9, "K"),
        ("put", 7, 22, "K"),
        # nostrils on the snout
        ("put", 8, 14, "D"),
        ("put", 8, 17, "D"),
        # white tusk islands crossing the mouth gap
        ("runs", [(9, 4, 5), (10, 4, 5), (9, 26, 27), (10, 26, 27)], "W"),
        # plated pale chest
        ("runs", [(11, 2, 29), (12, 5, 26), (13, 6, 25), (14, 7, 24),
                  (15, 8, 23)], "C"),
        ("runs", [(13, 8, 12), (13, 19, 23), (15, 9, 13), (15, 18, 22)],
         "D", "C"),
        # hide texture on the shoulders
        ("runs", [(12, 1, 4), (13, 2, 4), (13, 27, 30), (14, 26, 29),
                  (15, 3, 4), (16, 3, 4)], "D"),
        # foreleg shade and claws
        ("runs", [(18, 5, 10), (19, 4, 9), (20, 3, 8), (18, 21, 26),
                  (19, 22, 27), (20, 23, 28)], "D"),
        ("runs", [(21, 3, 3), (21, 5, 5), (21, 7, 7), (21, 24, 24),
                  (21, 26, 26), (21, 28, 28)], "W"),
    ],
}
