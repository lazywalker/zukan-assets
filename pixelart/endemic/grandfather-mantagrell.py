"""Grandfather mantagrell: a wide manta ray gliding; big diamond wings, a
long thin tail, and two head fins at the front."""
CONFIG = {
    "name": "grandfather-mantagrell",
    "size": (36, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (90, 110, 140, 255),   # back
        "D": (64, 80, 108, 255),    # darker edge
        "C": (200, 212, 228, 255),  # pale underside
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        8:  [(16, 20)],
        9:  [(12, 24)],
        10: [(9, 27)],
        11: [(6, 30)],
        12: [(4, 32)],
        13: [(2, 33)],
        14: [(2, 34)],
        15: [(3, 33)],
        16: [(5, 12), (26, 32)],
        17: [(8, 11), (24, 30)],
        18: [(11, 10), (26, 21), (30, 33)],
        19: [(28, 33), (32, 34)],
        20: [(33, 35)],
    },
    "fills": [
        # head fins at the front
        ("runs", [(8, 16, 20), (9, 12, 15)], "D"),
        # wing edge shading
        ("runs", [(10, 9, 11), (11, 6, 8), (12, 4, 6), (13, 2, 4),
                  (14, 2, 3)], "D"),
        ("runs", [(10, 25, 27), (11, 28, 30), (12, 30, 32), (13, 31, 33),
                  (14, 32, 34)], "D"),
        # pale underside band across the middle
        ("runs", [(13, 6, 12), (14, 6, 13), (15, 7, 13), (16, 6, 10)], "C"),
        # eyes + the thin tail
        ("put", 12, 14, "W"),
        ("put", 12, 15, "K"),
        ("runs", [(18, 31, 35), (19, 32, 34), (20, 33, 35)], "D"),
    ],
}
