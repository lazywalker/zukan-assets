"""Glavenus, brute wyvern. Crimson t-rex with a sword tail: massive jawed
head with a bone-white lower jaw, navy crown and back plates, tiny arms,
one solid torso over two thick legs, the huge orange blade tail rising
diagonally from the hip with a dark red cutting edge."""

CONFIG = {
    "name": "glavenus",
    "size": (36, 24),
    "compare_to": "../icons/mhgu/glavenus.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (170, 45, 38, 255),    # crimson body
        "D": (120, 32, 28, 255),    # dark crimson shade
        "N": (48, 50, 84, 255),     # navy: crown, back plates
        "B": (228, 125, 45, 255),   # orange blade
        "E": (130, 45, 30, 255),    # blade edge dark red
        "W": (246, 242, 230, 255),  # bone jaw / teeth / eye / claws
    },
    "base": "R",
    "spans": {
        4:  [(2, 7), (25, 26)],
        5:  [(1, 9), (23, 28)],
        6:  [(1, 10), (21, 29)],
        7:  [(1, 11), (16, 30)],
        8:  [(1, 30)],
        9:  [(1, 30)],
        10: [(1, 29)],
        11: [(2, 29)],
        12: [(2, 28)],
        13: [(3, 26)],
        14: [(4, 25)],
        15: [(6, 24)],
        16: [(8, 12), (16, 20)],
        17: [(8, 12), (16, 20)],
        18: [(8, 11), (16, 19)],
        19: [(7, 12), (16, 21)],
        20: [(7, 7), (9, 9), (11, 11), (16, 16), (18, 18), (20, 20)],
    },
    "fills": [
        # navy crown over the skull
        ("runs", [(4, 2, 6), (5, 1, 8), (6, 1, 9)], "N"),
        # brow + eye
        ("put", 6, 3, "WK"),
        # fangs over the dark mouth gap
        ("put", 11, 2, "W"),
        ("put", 11, 3, "KK"),
        ("put", 11, 5, "W"),
        # bone-white lower jaw
        ("runs", [(12, 3, 8), (13, 3, 8)], "W"),
        # navy back plates behind the head
        ("runs", [(7, 16, 18), (8, 16, 18)], "N"),
        # orange blade tail with dark red cutting edge on the outer rim
        ("runs", [(4, 25, 26), (5, 23, 28), (6, 21, 29), (7, 19, 30)],
         "B"),
        ("runs", [(4, 26, 26), (5, 27, 28), (6, 28, 29), (7, 29, 30)],
         "E"),
        ("runs", [(8, 26, 29), (9, 27, 29)], "B"),
        # tiny arms
        ("runs", [(11, 8, 9), (12, 8, 9)], "D"),
        # belly shade along the bottom edge
        ("runs", [(13, 10, 24), (14, 11, 23), (15, 12, 22)], "D"),
        # far leg darker
        ("runs", [(16, 16, 20), (17, 16, 20), (18, 16, 19), (19, 16, 21)],
         "D"),
        # claws
        ("runs", [(20, 7, 7), (20, 9, 9), (20, 11, 11), (20, 16, 16),
                  (20, 18, 18), (20, 20, 20)], "W"),
    ],
}
