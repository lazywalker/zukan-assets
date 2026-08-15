"""Anjanath, brute wyvern. Bulky biped with a big sail. Reference:
icons/mhrise/anjanath.png; pink head and front body, huge gold sail with
orange zigzag marks over the back, dark gray rear and tail, yellow fanged
jaw, tiny arms.
"""

CONFIG = {
    "name": "anjanath",
    "size": (36, 24),
    "compare_to": "../icons/mhrise/anjanath.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "P": (222, 110, 105, 255),  # pink body
        "p": (236, 165, 158, 255),  # light pink: face highlight, belly
        "D": (106, 95, 94, 255),    # dark gray: rear, tail, legs
        "d": (78, 70, 70, 255),     # darker gray: tail underside
        "G": (221, 172, 81, 255),   # gold sail
        "O": (196, 110, 60, 255),   # sail zigzag marks
        "W": (248, 245, 235, 255),  # teeth / eye
        "N": (48, 50, 84, 255),     # dark nose ridge
    },
    "base": "P",
    "spans": {
        # sail rows 1-7, head rows 3-9
        1:  [(12, 22)],
        2:  [(11, 23)],
        3:  [(2, 6), (11, 24)],
        4:  [(1, 8), (11, 24)],
        5:  [(1, 9), (11, 24)],
        6:  [(1, 10), (11, 24)],
        7:  [(1, 10), (11, 24)],
        8:  [(2, 10), (11, 23)],              # mouth gap c3-4
        9:  [(3, 10), (8, 24)],
        10: [(4, 24)],
        11: [(5, 25)],
        12: [(5, 26)],
        13: [(6, 26)],
        14: [(6, 28)],
        15: [(7, 28)],
        16: [(8, 28)],
        17: [(10, 15), (21, 26)],             # legs
        18: [(10, 15), (21, 26)],
        19: [(10, 14), (21, 25)],
        20: [(10, 14), (21, 25)],
        21: [(10, 14), (21, 25)],
        22: [(10, 10), (12, 12), (21, 21), (23, 23)],  # claws
    },
    "fills": [
        # gold sail + orange zigzag
        ("runs", [(1, 12, 22), (2, 11, 23), (3, 13, 23), (4, 15, 24),
                  (5, 17, 24), (6, 19, 24), (7, 21, 24)], "G"),
        ("runs", [(1, 15, 19), (2, 17, 21), (3, 19, 23), (4, 21, 24)],
         "O", "G"),
        # dark nose ridge + eye + teeth
        ("runs", [(4, 1, 3), (5, 1, 3)], "N"),
        ("put", 6, 4, "WK"),
        ("put", 8, 3, "W"),
        ("put", 8, 6, "W"),
        ("put", 9, 4, "W"),
        # light pink face + belly
        ("runs", [(5, 5, 9), (6, 6, 10), (7, 6, 10)], "p"),
        ("runs", [(11, 6, 16), (12, 6, 17), (13, 7, 17)], "p"),
        # dark gray rear + tail
        ("runs", [(10, 20, 24), (11, 20, 25), (12, 20, 26), (13, 19, 26),
                  (14, 19, 28), (15, 19, 28), (16, 19, 28)], "D"),
        ("runs", [(14, 24, 28), (15, 24, 28), (16, 24, 28)], "d"),
        # legs dark gray
        ("runs", [(r, 21, b) for r, b in ((17, 26), (18, 26), (19, 25),
                                          (20, 25), (21, 25))], "D"),
        # claws
        ("put", 22, 10, "W"),
        ("put", 22, 12, "W"),
        ("put", 22, 21, "W"),
        ("put", 22, 23, "W"),
    ],
}
