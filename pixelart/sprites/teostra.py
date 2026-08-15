"""Teostra, elder dragon. Flaming lion: huge cream mane ringing a red face,
twin swept-back horns, red-orange body, folded dark-red wings, cream tail
tuft, ember dots on the mane.

Palette: red body (195,65,45), dark red wings (150,45,38), cream mane and
tail tuft (232,206,150), dark horns (110,60,50), ember dots (240,140,60).
Recognition: cream lion mane + red face = teostra instantly.
"""

CONFIG = {
    "name": "teostra",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/teostra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (195, 65, 45, 255),    # red body
        "D": (150, 45, 38, 255),    # dark red: wings, shade
        "M": (232, 206, 150, 255),  # cream: mane, tail tuft, chest
        "H": (110, 60, 50, 255),    # dark horns
        "E": (240, 140, 60, 255),   # ember dots
        "W": (246, 242, 230, 255),  # eye
    },
    "base": "R",
    "spans": {
        3:  [(8, 10), (14, 16)],
        4:  [(6, 12), (13, 17)],
        5:  [(4, 13), (12, 18)],
        6:  [(3, 14), (12, 20)],
        7:  [(2, 14), (13, 22)],
        8:  [(2, 15), (14, 24)],
        9:  [(2, 15), (15, 26)],
        10: [(2, 15), (16, 27)],
        11: [(2, 15), (16, 27)],
        12: [(3, 14), (16, 26)],
        13: [(4, 14), (16, 25)],
        14: [(5, 14), (17, 25)],
        15: [(6, 14), (18, 24)],
        16: [(7, 14), (19, 23)],
        17: [(8, 14), (20, 22)],
        18: [(8, 13), (21, 22)],
        19: [(9, 12), (22, 22)],
    },
    "fills": [
        # cream mane ring around the face
        ("runs", [(4, 6, 12), (5, 4, 12), (6, 3, 4), (6, 9, 14),
                  (7, 2, 3), (7, 9, 14), (8, 2, 3), (8, 9, 15),
                  (9, 2, 3), (9, 9, 15)], "M"),
        # red face inside the ring
        ("runs", [(6, 5, 8), (7, 4, 8), (8, 4, 8), (9, 4, 8)], "R"),
        # dark horns, swept back
        ("runs", [(3, 8, 10), (4, 10, 12), (5, 12, 13)], "H"),
        ("runs", [(3, 14, 16), (4, 15, 17), (5, 16, 17)], "H"),
        # white eyes
        ("put", 7, 5, "W"),
        ("put", 7, 7, "W"),
        # cream chest under the face
        ("runs", [(10, 3, 9), (11, 4, 10), (12, 5, 10)], "M"),
        # folded dark-red wings on the back
        ("runs", [(10, 17, 26), (11, 17, 27), (12, 17, 26), (13, 17, 25),
                  (14, 18, 25), (15, 19, 24)], "D"),
        # ember dots on the mane and wings
        ("put", 5, 6, "E"),
        ("put", 8, 4, "E"),
        ("put", 9, 14, "E"),
        ("put", 11, 18, "E"),
        ("put", 13, 18, "E"),
        # tail with cream tuft
        ("runs", [(16, 20, 23), (17, 21, 22), (18, 21, 22), (19, 22, 22)],
         "R"),
        ("runs", [(18, 20, 21), (19, 21, 22)], "M"),
    ],
}
