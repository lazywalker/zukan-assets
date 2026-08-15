"""Epioth, leviathan. The small freshwater pack-swimmer: a low slender
grey-brown body with a blunt snout, one big dark eye, pale spots along
the back, a cream belly, two stubby leg pairs, and a tail that curls
down past the hip."""

CONFIG = {
    "name": "epioth",
    "size": (30, 24),
    "compare_to": "../icons/mh3u/epioth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (134, 120, 106, 255),   # grey-brown scales
        "D": (102, 90, 80, 255),     # darker shade / tail
        "C": (218, 206, 184, 255),   # pale spots / belly
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        5:  [(2, 5)],
        6:  [(1, 7)],
        7:  [(0, 9)],
        8:  [(0, 12)],
        9:  [(0, 18)],
        10: [(1, 22)],
        11: [(2, 24)],
        12: [(3, 26)],
        13: [(4, 28)],
        14: [(5, 27)],
        15: [(6, 25)],
        16: [(7, 23)],
        17: [(8, 11), (14, 17), (19, 22)],     # legs
        18: [(8, 8), (10, 10), (15, 15), (17, 17), (20, 20), (22, 22)],
    },
    "fills": [
        # big dark eye with a white glint
        ("put", 7, 3, "W"),
        ("put", 7, 4, "K"),
        # nostril on the blunt snout
        ("put", 7, 0, "K"),
        # small mouth line
        ("runs", [(8, 0, 2)], "K"),
        # pale spots along the back
        ("runs", [(9, 6, 7), (10, 11, 12), (11, 16, 17), (12, 20, 21),
                  (13, 9, 10), (14, 14, 15)], "C"),
        # cream belly along the bottom edge
        ("runs", [(13, 5, 18), (14, 6, 20), (15, 7, 20),
                  (16, 8, 19)], "C"),
        # tail curls down dark
        ("runs", [(12, 24, 26), (13, 24, 28), (14, 23, 27),
                  (15, 22, 25), (16, 21, 23)], "D"),
        # legs, rear pair darker
        ("runs", [(17, 8, 11)], "G"),
        ("runs", [(17, 14, 17), (17, 19, 22)], "D", "G"),
        ("put", 18, 8, "W"),
        ("put", 18, 10, "W"),
        ("put", 18, 15, "W"),
        ("put", 18, 17, "W"),
        ("put", 18, 20, "W"),
        ("put", 18, 22, "W"),
    ],
}
