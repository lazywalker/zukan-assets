"""Pukei-Pukei, bird wyvern. The poison chameleon: plump round green body
under a big round head, red-rimmed face with big rolling eyes, pink tongue,
light green belly, big tail fins with red accents, four short lizard legs."""

CONFIG = {
    "name": "pukei-pukei",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/pukei-pukei.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (120, 170, 90, 255),   # green body
        "R": (200, 80, 70, 255),    # red face rim / tail fins
        "L": (170, 205, 130, 255),  # light green belly
        "T": (220, 120, 140, 255),  # pink tongue
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        4:  [(2, 8)],                         # round head top
        5:  [(1, 9)],
        6:  [(1, 10)],                        # eyes
        7:  [(1, 10)],
        8:  [(1, 10)],                        # tongue
        9:  [(2, 9), (11, 14)],               # chin + tail top
        10: [(3, 10), (11, 16)],              # body + tail
        11: [(4, 11), (12, 18)],
        12: [(4, 12), (13, 19)],
        13: [(4, 13), (14, 20)],
        14: [(5, 13), (15, 21)],
        15: [(5, 13), (17, 22)],
        16: [(5, 13), (19, 23)],
        17: [(6, 12), (21, 23)],
        18: [(6, 11), (23, 23)],
        19: [(6, 8), (11, 13)],
        20: [(6, 8), (11, 13)],
        21: [(6, 6), (8, 8), (11, 11), (13, 13)],
    },
    "fills": [
        # red face rim around a green face
        ("runs", [(4, 2, 8), (5, 1, 9), (6, 1, 2), (6, 9, 10)], "R"),
        # big rolling eyes
        ("put", 6, 3, "W"),
        ("put", 6, 6, "W"),
        ("put", 6, 4, "K"),
        ("put", 6, 7, "K"),
        # pink tongue sticking out
        ("runs", [(8, 1, 2)], "T"),
        # light belly along the bottom edge
        ("runs", [(12, 5, 9), (13, 5, 10), (14, 5, 11), (15, 6, 11)], "L"),
        # dark back spots
        ("runs", [(10, 5, 6), (11, 6, 7), (12, 8, 9)], "K"),
        # tail fins with red accents
        ("runs", [(11, 13, 15), (12, 15, 17), (13, 17, 19), (14, 18, 20)],
         "R"),
        # claws
        ("put", 21, 6, "W"),
        ("put", 21, 8, "W"),
        ("put", 21, 11, "W"),
        ("put", 21, 13, "W"),
    ],
}
