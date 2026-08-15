"""Najarala, snake wyvern. The flute serpent: a long green snake body with
orange resonance flutes standing along the back, a big square head with a
pale jaw and white fangs, stubby legs, and the tail ending in an orange
rattle cluster. Long and low, most of the length is trunk."""

CONFIG = {
    "name": "najarala",
    "size": (44, 24),
    "compare_to": "../icons/mh4u/najarala.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (118, 148, 84, 255),   # green scales
        "D": (88, 114, 62, 255),    # darker green
        "F": (222, 130, 52, 255),   # orange flutes
        "R": (196, 72, 48, 255),    # red flute tips
        "C": (208, 200, 156, 255),  # pale belly
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        # flute tips + tail rattle tip
        5:  [(1, 8), (12, 14), (19, 21), (26, 28), (39, 40)],
        6:  [(0, 10), (12, 15), (19, 22), (26, 29), (38, 42)],
        7:  [(0, 31), (38, 43)],
        8:  [(0, 34), (37, 43)],
        9:  [(0, 37), (38, 43)],
        10: [(0, 38), (39, 43)],
        11: [(1, 41)],
        12: [(2, 41)],
        13: [(3, 40)],
        14: [(4, 39)],
        15: [(5, 37)],
        16: [(6, 36)],
        17: [(8, 35)],
        # stubby legs
        18: [(10, 12), (19, 21), (28, 30)],
        19: [(10, 12), (19, 21), (28, 30)],
        20: [(10, 10), (12, 12), (19, 19), (21, 21), (28, 28), (30, 30)],
    },
    "fills": [
        # orange flutes with red tips standing along the back
        ("runs", [(5, 12, 14), (6, 12, 15)], "F"),
        ("runs", [(5, 19, 21), (6, 19, 22)], "F"),
        ("runs", [(5, 26, 28), (6, 26, 29)], "F"),
        ("runs", [(5, 13, 13), (5, 20, 20), (5, 27, 27)], "R", "F"),
        # orange rattle cluster at the tail end
        ("runs", [(5, 39, 40), (6, 38, 42), (7, 38, 43), (8, 37, 43),
                  (9, 38, 43), (10, 39, 43)], "F"),
        ("runs", [(5, 39, 39), (6, 39, 40)], "R", "F"),
        # pale jaw + fangs
        ("runs", [(10, 0, 5), (11, 1, 5)], "C"),
        ("put", 10, 1, "W"),
        ("put", 10, 3, "W"),
        # eye
        ("put", 8, 3, "K"),
        # dark scale bands down the trunk
        ("runs", [(10, 16, 18), (11, 20, 22), (12, 17, 19),
                  (13, 22, 24), (14, 18, 20)], "D"),
        # cream belly along the bottom edge
        ("runs", [(15, 5, 36), (16, 6, 35), (17, 8, 34)], "C"),
        # legs darker
        ("runs", [(18, 10, 12), (18, 19, 21), (18, 28, 30),
                  (19, 10, 12), (19, 19, 21), (19, 28, 30),
                  (20, 10, 10), (20, 12, 12), (20, 19, 19), (20, 21, 21),
                  (20, 28, 28), (20, 30, 30)], "D"),
    ],
}
