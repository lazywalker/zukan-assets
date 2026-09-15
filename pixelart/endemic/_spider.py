"""Spider archetype: round abdomen at the rear, smaller head at the front
with a row of eyes, eight legs (four visible pairs) splayed around the
body. Abdomen marking is species identity."""

CONFIG = {
    "name": "_spider",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (120, 96, 140, 255),   # body
        "D": (88, 68, 106, 255),    # legs / marking
        "C": (220, 190, 160, 255),  # abdomen marking
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(5, 10)],
        7:  [(4, 12)],
        8:  [(3, 22)],
        9:  [(3, 24)],
        10: [(3, 24)],
        11: [(4, 23)],
        12: [(5, 22)],
        13: [(6, 20)],
        14: [(3, 3), (8, 8), (13, 13), (17, 17)],
        15: [(3, 3), (8, 8), (13, 13), (17, 17)],
        16: [(4, 4), (9, 9), (14, 14)],
        17: [(5, 5), (10, 10), (15, 15)],
    },
    "fills": [
        # head darker with an eye row
        ("runs", [(6, 5, 10), (7, 4, 8)], "D"),
        ("put", 7, 6, "W"),
        ("put", 7, 8, "W"),
        ("put", 6, 7, "W"),
        # abdomen marking
        ("runs", [(9, 17, 21), (10, 18, 22), (11, 18, 20)], "C"),
        # legs darker
        ("runs", [(14, 3, 3), (14, 8, 8), (14, 13, 13), (14, 17, 17),
                  (15, 3, 3), (15, 8, 8), (15, 13, 13), (15, 17, 17)],
         "D"),
    ],
}
