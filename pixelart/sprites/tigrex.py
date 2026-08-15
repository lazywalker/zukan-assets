"""Tigrex, flying wyvern with a brute's stance. Third archetype: crouched
runner, huge jaw, wing-claw forelimbs. Reference pose from
icons/mhrise/tigrex.png: navy crown ridge, orange body with vertical navy
stripe bands, cream lower jaw and belly, white fangs, cyan eye.

New vs earlier configs: striped texture, expressed as runs comprehensions
over the body columns; no engine change.
"""

CONFIG = {
    "name": "tigrex",
    "size": (36, 24),
    "compare_to": "../icons/mhrise/tigrex.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "O": (238, 156, 31, 255),   # orange body
        "N": (76, 92, 175, 255),    # navy: crown ridge + stripes
        "M": (231, 199, 157, 255),  # cream: lower jaw, belly, paw shade
        "W": (250, 248, 240, 255),  # fangs / teeth
        "C": (60, 185, 185, 255),   # cyan eye
        "V": (120, 80, 40, 255),    # claw brown
    },
    "base": "O",
    "spans": {
        # head: navy crown rows 2-4, face 5-7, huge jaw rows 8-11
        2:  [(4, 8), (29, 30)],               # crown ridge + tail tip
        3:  [(3, 10), (28, 31)],
        4:  [(2, 11), (27, 31)],
        5:  [(1, 12), (26, 31)],
        6:  [(1, 13), (25, 31)],              # brow + neck + tail
        7:  [(1, 13), (13, 24), (25, 30)],    # snout + body + tail
        8:  [(5, 13), (13, 25), (25, 28)],    # mouth gap c1-4
        9:  [(2, 12), (12, 25)],
        10: [(2, 11), (12, 25)],
        11: [(3, 11), (12, 25)],
        12: [(12, 25)],
        13: [(12, 24)],
        14: [(13, 23)],
        15: [(13, 22)],
        16: [(14, 18), (22, 26)],             # foreleg + hind leg
        17: [(14, 18), (22, 26)],
        18: [(14, 17), (22, 25)],
        19: [(14, 17), (22, 25)],
        20: [(13, 17), (22, 25)],             # paws
        21: [(13, 13), (15, 15), (22, 22), (24, 24)],  # claws
    },
    "fills": [
        # navy crown ridge over the skull top
        ("runs", [(2, 4, 8), (3, 3, 10), (4, 2, 11)], "N"),
        # neck band behind the eye
        ("runs", [(5, 11, 12), (6, 11, 13), (7, 11, 13)], "N"),
        # vertical stripe bands across the body
        ("runs", [(r, a, b) for r in range(7, 13)
                  for a, b in ((15, 16), (19, 20), (22, 23))], "N"),
        # tail bands
        ("runs", [(2, 29, 30), (3, 28, 30), (4, 27, 30), (5, 26, 30),
                  (6, 25, 28)], "N"),
        # cream lower jaw + chin
        ("runs", [(9, 2, 12), (10, 2, 11), (11, 3, 11)], "M"),
        # cream belly
        ("runs", [(12, 12, 19), (13, 12, 19), (14, 13, 18), (15, 13, 18)], "M"),
        # leg stripe bands
        ("runs", [(17, 15, 17), (18, 15, 17), (17, 23, 25), (18, 23, 25)], "N"),
        # eye + fangs + teeth
        ("put", 6, 4, "CK"),
        ("put", 7, 2, "W"),
        ("put", 7, 4, "W"),
        ("put", 8, 3, "W"),
        # claws
        ("put", 21, 13, "V"),
        ("put", 21, 15, "V"),
        ("put", 21, 22, "V"),
        ("put", 21, 24, "V"),
    ],
}
