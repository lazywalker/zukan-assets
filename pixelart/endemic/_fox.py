"""Fox archetype: small fox facing left, pointed upright ears, slim snout,
compact body, a big bushy tail sweeping behind, four slim legs. Pelt
colors are species identity."""

CONFIG = {
    "name": "_fox",
    "size": (30, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (196, 140, 84, 255),   # pelt
        "D": (150, 104, 60, 255),   # darker pelt
        "C": (238, 228, 214, 255),  # chest / tail tip
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(7, 8), (10, 11)],
        6:  [(6, 9), (10, 12)],
        7:  [(5, 12)],
        8:  [(4, 12)],
        9:  [(3, 12)],
        10: [(3, 20)],
        11: [(3, 21)],
        12: [(4, 22)],
        13: [(4, 23)],
        14: [(5, 23)],
        15: [(6, 22)],
        16: [(7, 21)],
        17: [(8, 20)],
        18: [(9, 9), (14, 14), (18, 19)],
        19: [(9, 9), (14, 14), (18, 18)],
    },
    "fills": [
        # ears darker inside
        ("runs", [(5, 7, 8), (6, 6, 7)], "D"),
        # snout: pale muzzle + nose
        ("runs", [(8, 4, 5), (9, 3, 4)], "C"),
        ("put", 9, 3, "K"),
        # eye
        ("put", 8, 7, "K"),
        # back shade
        ("runs", [(10, 14, 20), (11, 15, 21)], "D"),
        # bushy tail with a pale tip
        ("runs", [(11, 18, 21), (12, 19, 22), (13, 20, 23), (14, 20, 23),
                  (15, 19, 22), (16, 18, 21), (17, 17, 20)], "D"),
        ("runs", [(13, 22, 23), (14, 22, 23)], "C"),
        # chest pale
        ("runs", [(10, 3, 4), (11, 3, 5), (12, 4, 6)], "C"),
    ],
}
