"""Wiggler: the yellow caterpillar that curls like a spring, with a tiny
face at the front."""
CONFIG = {
    "name": "wiggler",
    "size": (30, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "Y": (232, 198, 90, 255),   # yellow segments
        "D": (188, 152, 58, 255),   # segment shade
        "C": (248, 226, 150, 255),  # pale underside
        "R": (206, 80, 60, 255),    # head
        "W": (246, 242, 230, 255),
    },
    "base": "Y",
    "spans": {
        10: [(2, 7)],
        11: [(2, 12)],
        12: [(2, 17)],
        13: [(2, 22)],
        14: [(2, 27)],
        15: [(2, 28)],
        16: [(3, 28)],
        17: [(4, 28)],
        18: [(6, 27)],
        19: [(8, 25)],
    },
    "fills": [
        # red head at the front with dot eyes
        ("runs", [(10, 2, 6), (11, 2, 6)], "R"),
        ("put", 11, 4, "W"),
        ("put", 11, 5, "K"),
        # segment bands
        ("runs", [(12, 8, 11), (13, 8, 11), (14, 13, 16), (15, 13, 16),
                  (16, 18, 21), (17, 18, 21), (18, 21, 24), (19, 20, 23)],
         "D"),
        # pale underside
        ("runs", [(15, 4, 11), (16, 4, 12), (17, 5, 12)], "C"),
    ],
}
