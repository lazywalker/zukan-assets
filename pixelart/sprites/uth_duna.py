"""Uth Duna, leviathan. The rain-cloaked heavyweight, drawn in the
front-facing bulk of its icon: a massive red-orange dome, pale blue fin
cloaks draped down both arms with staggered hems, a pale face plate on
the chest with a wide snaggletooth grin."""

CONFIG = {
    "name": "uth-duna",
    "size": (34, 24),
    "compare_to": "../icons/mhwilds/uth-duna.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (190, 85, 60, 255),     # red-orange body
        "D": (145, 60, 45, 255),     # darker red shade
        "C": (170, 205, 245, 255),   # pale blue fin cloaks / face
        "E": (60, 26, 24, 255),      # dark mouth
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        2:  [(13, 20)],                          # dome top
        3:  [(11, 22)],
        4:  [(10, 23)],
        5:  [(9, 24)],
        6:  [(8, 25)],
        7:  [(7, 26)],
        8:  [(6, 27)],
        9:  [(6, 27)],
        10: [(5, 28)],
        11: [(5, 28)],
        12: [(5, 28)],
        13: [(5, 28)],
        14: [(5, 28)],
        15: [(6, 27)],
        16: [(7, 26)],
        17: [(8, 25)],
        18: [(10, 23)],
        19: [(12, 21)],                          # belly bottom
    },
    "fills": [
        # darker red along the dome sides
        ("runs", [(4, 10, 12), (5, 9, 11), (6, 8, 10), (7, 7, 9),
                  (8, 6, 8), (9, 6, 8), (10, 5, 7), (11, 5, 7),
                  (12, 5, 7), (13, 5, 7), (14, 5, 7), (15, 6, 8),
                  (16, 7, 9), (17, 8, 10), (18, 10, 13), (4, 21, 23),
                  (5, 22, 24), (6, 23, 25), (7, 24, 26), (8, 25, 27),
                  (9, 25, 27), (10, 26, 28), (11, 26, 28), (12, 26, 28),
                  (13, 26, 28), (14, 26, 28), (15, 25, 27), (16, 24, 26),
                  (17, 23, 25), (18, 20, 23)], "D", "R"),
        # pale face plate on the chest
        ("runs", [(5, 12, 21), (6, 12, 21), (7, 12, 21), (8, 12, 21),
                  (9, 13, 20)], "C"),
        # dark eyes with pale glints
        ("put", 6, 14, "K"),
        ("put", 6, 19, "K"),
        ("runs", [(5, 13, 14), (5, 19, 20)], "D", "R"),
        # wide dark grin with snaggle teeth
        ("runs", [(10, 11, 22), (11, 11, 22), (12, 12, 21)], "E"),
        ("runs", [(10, 12, 13), (10, 16, 17), (10, 20, 21),
                  (12, 13, 14), (12, 18, 19)], "W", "E"),
        # pale fin cloaks draped down both sides, staggered hems
        ("runs", [(9, 2, 4), (10, 2, 4), (11, 1, 4), (12, 1, 4),
                  (13, 2, 4), (14, 2, 5), (15, 2, 5), (16, 3, 5),
                  (9, 29, 31), (10, 29, 31), (11, 29, 32), (12, 29, 32),
                  (13, 29, 31), (14, 28, 31), (15, 28, 31), (16, 28, 30)],
         "C", "R"),
        # belly shading and pale chin
        ("runs", [(16, 11, 22), (17, 12, 21), (18, 14, 19)], "D", "R"),
        ("runs", [(19, 13, 20)], "C"),
    ],
}
