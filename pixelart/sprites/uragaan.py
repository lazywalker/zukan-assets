"""Uragaan, brute wyvern. The rolling boulder: a near-circular armored
body, a tiny eye low on the face, a huge pale bone chin axe jutting
forward and curving up in front of the jaw, rocky plate segments with ore
glints on the back, stubby legs and a short blunt tail."""

CONFIG = {
    "name": "uragaan",
    "size": (34, 24),
    "compare_to": "../icons/mhw/uragaan.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (155, 75, 58, 255),    # maroon boulder body
        "D": (112, 52, 42, 255),    # darker plates / shade
        "C": (222, 206, 180, 255),  # bone chin axe
        "O": (212, 170, 70, 255),   # ore glints
        "S": (55, 28, 26, 255),     # mouth groove
        "L": (178, 158, 138, 255),  # gray belly band
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        3:  [(12, 22)],                       # boulder top
        4:  [(10, 24)],
        5:  [(8, 26)],
        6:  [(7, 27)],
        7:  [(6, 28)],
        8:  [(1, 29)],                        # chin axe tip + face
        9:  [(0, 30)],
        10: [(0, 30)],
        11: [(0, 30)],
        12: [(0, 30)],
        13: [(1, 32)],
        14: [(2, 33)],                        # tail nub right
        15: [(3, 32)],
        16: [(4, 30)],
        17: [(5, 29)],
        18: [(6, 28)],                        # boulder bottom
        19: [(8, 12), (15, 16), (18, 22)],    # legs + belly dip
        20: [(8, 12), (18, 22)],
        21: [(8, 12), (18, 22)],
        22: [(8, 8), (10, 10), (18, 18), (20, 20)],
    },
    "fills": [
        # rocky plate segments on the back
        ("runs", [(3, 13, 21), (4, 12, 16), (4, 19, 23), (5, 9, 13),
                  (5, 17, 21), (5, 24, 25), (6, 8, 11), (6, 15, 18)], "D"),
        # ore glints between the plates
        ("runs", [(4, 17, 18), (5, 14, 15), (6, 12, 13)], "O"),
        # bone chin axe, curving up in front of the face
        ("runs", [(8, 1, 3), (9, 0, 3), (10, 0, 3), (11, 0, 3), (12, 0, 3),
                  (13, 1, 3)], "C"),
        # mouth groove where the axe meets the jaw
        ("runs", [(11, 3, 3), (12, 3, 3)], "S", "C"),
        ("runs", [(11, 4, 4), (12, 4, 4)], "S"),
        # tiny eye low on the face
        ("put", 9, 5, "W"),
        ("put", 9, 6, "K"),
        # gray belly band along the bottom edge
        ("runs", [(15, 6, 12), (16, 6, 16), (17, 7, 18)], "L"),
        # tail underside shade
        ("runs", [(14, 29, 33), (15, 28, 32)], "D"),
        # rear leg darker
        ("runs", [(19, 18, 22), (20, 18, 22), (21, 18, 22)], "D"),
        # claws
        ("put", 22, 8, "W"),
        ("put", 22, 10, "W"),
        ("put", 22, 18, "W"),
        ("put", 22, 20, "W"),
    ],
}
