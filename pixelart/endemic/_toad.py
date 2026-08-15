"""Toad archetype: round squat body, brow bumps with eyes on top, a wide
dark mouth line, folded hind legs, belly band, back spots. Paratoad's
pustules and friends' colors are species identity."""

CONFIG = {
    "name": "_toad",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (130, 140, 80, 255),   # back
        "D": (96, 106, 58, 255),    # darker: spots, legs
        "C": (214, 214, 170, 255),  # belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        7:  [(9, 12), (16, 19)],
        8:  [(8, 21)],
        9:  [(6, 22)],
        10: [(5, 23)],
        11: [(4, 23)],
        12: [(4, 23)],
        13: [(4, 22)],
        14: [(5, 21)],
        15: [(6, 20)],
        16: [(8, 19)],
        17: [(5, 9), (15, 19)],
        18: [(4, 10), (16, 20)],
        19: [(4, 4), (6, 6), (8, 10), (16, 16), (18, 20)],
    },
    "fills": [
        # brow bumps darker with eyes on top
        ("runs", [(7, 9, 12), (7, 16, 19)], "D"),
        ("put", 8, 10, "W"),
        ("put", 8, 11, "K"),
        ("put", 8, 17, "K"),
        ("put", 8, 18, "W"),
        # wide mouth line
        ("runs", [(13, 5, 20)], "K"),
        # back spots
        ("put", 10, 9, "D"),
        ("put", 11, 12, "D"),
        ("put", 11, 16, "D"),
        ("put", 12, 8, "D"),
        # belly band
        ("runs", [(14, 7, 18), (15, 8, 16), (16, 10, 15)], "C"),
        # folded hind legs darker
        ("runs", [(17, 5, 9), (17, 15, 19), (18, 4, 10), (18, 16, 20)],
         "D"),
    ],
}
