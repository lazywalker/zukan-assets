"""Paolumu, floating wyvern. The fluffy balloon, drawn in the round front
of its icon: a huge white fur ball with orange-brown ears, an orange face
patch with dark eyes and tiny fangs, and a pink tail ball peeking below."""

CONFIG = {
    "name": "paolumu",
    "size": (28, 24),
    "compare_to": "../icons/mhw/paolumu.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (245, 240, 235, 255),   # white fur ball
        "C": (215, 205, 195, 255),   # fur shade
        "O": (170, 110, 60, 255),    # orange-brown ears / face
        "D": (130, 80, 40, 255),     # dark orange shade
        "P": (230, 150, 160, 255),   # pink tail ball
    },
    "base": "W",
    "spans": {
        1:  [(6, 7), (20, 21)],                  # ear tips
        2:  [(5, 8), (19, 22)],
        3:  [(4, 9), (18, 23)],
        4:  [(4, 9), (18, 23), (10, 17)],        # ears + head top
        5:  [(3, 10), (17, 24), (10, 17)],
        6:  [(3, 24)],
        7:  [(2, 25)],
        8:  [(2, 25)],
        9:  [(1, 26)],
        10: [(1, 26)],
        11: [(1, 26)],
        12: [(1, 26)],
        13: [(2, 25)],
        14: [(2, 25)],
        15: [(3, 24)],
        16: [(4, 23), (12, 15)],                 # body + tail ball
        17: [(5, 22), (12, 15)],
        18: [(7, 20), (12, 15)],
        19: [(9, 18), (13, 14)],
    },
    "fills": [
        # orange-brown ears with dark rims
        ("runs", [(1, 6, 7), (2, 5, 8), (3, 4, 9), (4, 4, 9), (5, 3, 6),
                  (1, 20, 21), (2, 19, 22), (3, 18, 23), (4, 18, 23),
                  (5, 21, 24)], "O", "W"),
        ("runs", [(3, 4, 5), (4, 4, 5), (3, 22, 23), (4, 22, 23)],
         "D", "O"),
        # orange face patch with dark eyes and tiny fangs
        ("runs", [(5, 10, 17), (6, 10, 17), (7, 10, 17), (8, 11, 16),
                  (9, 11, 16), (10, 11, 16)], "O"),
        ("runs", [(5, 12, 15)], "D", "O"),
        ("put", 8, 12, "K"),
        ("put", 8, 15, "K"),
        ("put", 9, 12, "W"),
        ("put", 9, 15, "W"),
        # fur ball shading along the lower sides
        ("runs", [(10, 1, 5), (11, 1, 4), (12, 1, 4), (13, 2, 5),
                  (14, 2, 5), (15, 3, 6), (10, 22, 26), (11, 23, 26),
                  (12, 23, 26), (13, 22, 25), (14, 22, 25), (15, 21, 24)],
         "C", "W"),
        # pink tail ball peeking below
        ("runs", [(16, 12, 15), (17, 12, 15), (18, 12, 15), (19, 13, 14)],
         "P"),
        ("put", 17, 13, "W"),
    ],
}
