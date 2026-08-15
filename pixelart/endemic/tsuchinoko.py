"""Tsuchinoko: the legendary fat snake; a thick stubby coil with a wide
flat head, tiny tail, and a smirk."""
CONFIG = {
    "name": "tsuchinoko",
    "size": (30, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (150, 130, 90, 255),   # sandy body
        "D": (114, 96, 64, 255),    # darker bands
        "C": (216, 198, 152, 255),  # belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        8:  [(4, 10)],
        9:  [(3, 12)],
        10: [(3, 24)],
        11: [(3, 26)],
        12: [(3, 27)],
        13: [(3, 27)],
        14: [(3, 26)],
        15: [(4, 24)],
        16: [(5, 22)],
        17: [(6, 19)],
        18: [(8, 16)],
    },
    "fills": [
        # wide flat head with dot eyes
        ("runs", [(8, 4, 10), (9, 3, 6)], "C"),
        ("put", 9, 5, "K"),
        ("put", 9, 9, "K"),
        # smirk mouth
        ("runs", [(10, 4, 5)], "K"),
        # dark bands down the fat coil
        ("runs", [(11, 8, 11), (12, 8, 12), (13, 14, 18), (14, 15, 19),
                  (15, 10, 13), (16, 11, 15)], "D"),
        # belly band
        ("runs", [(13, 4, 8), (14, 4, 9), (15, 4, 9), (16, 5, 9),
                  (17, 6, 10)], "C"),
    ],
}
