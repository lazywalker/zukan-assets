"""Barioth, flying wyvern. White sabertooth: tusked upper jaw with two
long fangs pointing up from the lower jaw, gray-blue stripes on the flanks
and tail, small wing fins on the forelimbs, powerful hind legs, dark claws.

Palette: white coat (228,230,236), gray-blue stripes (150,158,175), dark
claws (60,60,70), amber eyes (220,150,60). Recognition: white bulk + twin
saberteeth + stripe bands = barioth at terminal size.
"""

CONFIG = {
    "name": "barioth",
    "size": (36, 24),
    "compare_to": "../icons/mh3u/barioth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (228, 230, 236, 255),  # white coat
        "S": (150, 158, 175, 255),  # gray-blue stripes
        "D": (110, 118, 138, 255),  # darker: far legs, shade
        "A": (220, 150, 60, 255),   # amber eyes
        "L": (205, 205, 215, 255),  # pale warm belly band
        "V": (60, 60, 70, 255),     # dark claws
    },
    "base": "W",
    "spans": {
        3:  [(3, 4), (8, 9)],                 # small ears
        4:  [(2, 6), (7, 10)],
        5:  [(1, 8), (9, 14), (16, 18)],
        6:  [(1, 9), (10, 16), (16, 19)],
        7:  [(1, 10), (11, 18), (17, 20)],
        8:  [(1, 11), (12, 20), (18, 21)],
        9:  [(1, 11), (13, 21), (19, 22)],
        10: [(2, 12), (14, 23), (21, 23)],
        11: [(3, 13), (15, 24), (24, 25)],
        12: [(4, 13), (16, 24), (25, 26)],
        13: [(5, 13), (18, 25), (26, 27)],
        14: [(6, 13), (19, 25), (27, 28)],
        15: [(7, 13), (21, 26), (28, 28)],
        16: [(8, 13), (22, 26), (28, 29)],
        17: [(9, 13), (23, 26), (29, 29)],
        18: [(9, 13), (24, 26)],
        19: [(9, 12), (24, 25)],
        20: [(8, 12), (24, 24)],
        21: [(8, 8), (10, 10), (24, 24)],
    },
    "fills": [
        # amber eyes + dark nose
        ("put", 6, 3, "A"),
        ("put", 6, 6, "D"),
        # dark mouth gap so the twin saberteeth pop
        ("runs", [(7, 2, 2), (8, 2, 2)], "K"),
        ("runs", [(7, 4, 4), (8, 4, 4)], "K"),
        # twin saberteeth: up from the lower jaw
        ("runs", [(7, 3, 3), (8, 3, 3)], "W"),
        ("runs", [(7, 5, 5), (8, 5, 5)], "W"),
        # gray-blue stripes: flank bands + tail bands
        ("runs", [(9, 15, 16), (10, 17, 18), (11, 19, 20), (12, 21, 22),
                  (13, 22, 23), (14, 23, 24)], "S"),
        ("runs", [(8, 19, 20), (9, 21, 22), (10, 22, 23)], "S"),
        # pale belly band along the bottom edge
        ("runs", [(13, 6, 12), (14, 7, 12), (15, 8, 12), (16, 9, 13)], "L"),
        # foreleg wing fins (small membrane), striped
        ("runs", [(8, 12, 14), (9, 12, 14), (10, 13, 14)], "S"),
        # far legs darker
        ("runs", [(17, 23, 26), (18, 24, 26), (19, 24, 25)], "D"),
        ("runs", [(15, 21, 22), (16, 22, 23)], "D"),
        # dark claws
        ("put", 21, 8, "V"),
        ("put", 21, 10, "V"),
        ("put", 21, 24, "V"),
    ],
}
