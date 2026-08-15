"""Gajau, fish. The river catfish: a long olive body with a wide grinning
mouth, pale whiskers trailing forward, golden spots along the flank, and
a low fin ridge."""

CONFIG = {
    "name": "gajau",
    "size": (30, 24),
    "compare_to": "../icons/mhrise/gajau.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (146, 138, 96, 255),   # olive body
        "D": (112, 104, 70, 255),   # darker shade
        "Y": (208, 172, 80, 255),   # golden spots
        "C": (216, 204, 168, 255),  # pale belly / whiskers
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        5:  [(4, 9)],                         # head top
        6:  [(2, 11), (12, 13)],
        7:  [(1, 12), (11, 16)],
        8:  [(0, 13), (10, 18)],              # mouth + body
        9:  [(0, 13), (10, 20)],
        10: [(1, 13), (10, 22)],
        11: [(1, 12), (10, 23)],
        12: [(2, 12), (11, 24)],
        13: [(2, 12), (12, 25)],
        14: [(3, 11), (13, 26)],
        15: [(4, 11), (15, 27)],
        16: [(5, 10), (17, 27)],              # tail fin
        17: [(6, 9), (20, 26)],
        18: [(7, 8), (23, 25)],
    },
    "fills": [
        # wide grinning mouth
        ("runs", [(8, 1, 7)], "K"),
        ("put", 8, 2, "W"),
        ("put", 8, 4, "W"),
        ("put", 8, 6, "W"),
        # pale whiskers trailing forward
        ("runs", [(9, 0, 1), (10, 0, 0)], "C"),
        ("runs", [(9, 1, 2), (10, 1, 2)], "C"),
        # small eye
        ("put", 6, 4, "K"),
        # golden spots along the flank
        ("runs", [(9, 15, 16), (10, 18, 19), (11, 16, 17),
                  (12, 20, 21), (13, 17, 18), (14, 20, 21),
                  (15, 18, 19)], "Y"),
        # low fin ridge along the back
        ("runs", [(6, 12, 13), (7, 11, 14), (8, 12, 15)], "D"),
        # pale belly along the bottom edge
        ("runs", [(13, 3, 10), (14, 4, 10), (15, 5, 10), (16, 6, 9)], "C"),
        # tail fin darker
        ("runs", [(16, 22, 27), (17, 22, 26), (18, 23, 25)], "D"),
    ],
}
