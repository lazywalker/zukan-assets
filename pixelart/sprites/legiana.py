"""Legiana, levitating flying wyvern. Fourth composition type: front-facing
axis-symmetric, like the source render and pokesprite's alomomola. Reference:
icons/mhw/legiana.png; spread layered blue wings with dark fingertips and
white spots, small head with long crest antennae and yellow eyes, white
chest diamond, dark legs and tail tip.
"""

CONFIG = {
    "name": "legiana",
    "size": (30, 24),
    "compare_to": "../icons/mhw/legiana.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "B": (150, 168, 224, 255),  # light blue wings
        "D": (105, 120, 190, 255),  # mid blue: wing layering, head
        "N": (45, 50, 90, 255),     # navy: fingertips, feet, antennae, tail
        "W": (238, 236, 226, 255),  # white chest
        "Y": (240, 210, 90, 255),   # yellow eyes
    },
    "base": "B",
    "spans": {
        3:  [(11, 11), (18, 18)],             # crest antennae tips
        4:  [(10, 11), (18, 19)],             # antennae + wing tips
        5:  [(3, 5), (9, 20), (24, 26)],      # wing tips + head + wing tips
        6:  [(2, 9), (10, 19), (20, 27)],
        7:  [(1, 9), (10, 19), (20, 28)],
        8:  [(1, 9), (10, 19), (20, 28)],
        9:  [(1, 10), (9, 20), (19, 28)],
        10: [(1, 10), (9, 20), (19, 28)],
        11: [(1, 11), (9, 20), (18, 28)],
        12: [(2, 11), (9, 20), (18, 27)],
        13: [(2, 11), (9, 20), (18, 27)],
        14: [(3, 12), (9, 20), (17, 26)],
        15: [(4, 13), (9, 20), (16, 25)],
        16: [(5, 13), (9, 20), (16, 24)],
        17: [(6, 13), (9, 20), (16, 23)],
        18: [(7, 20), (22, 22)],
        19: [(13, 16)],
        20: [(13, 16)],
        21: [(14, 15)],
        22: [(12, 13), (16, 17)],             # feet
    },
    "fills": [
        # wing fingertips navy (outer edge, both sides)
        ("runs", [(4, 10, 11), (4, 18, 19), (5, 3, 5), (5, 24, 26),
                  (6, 2, 4), (6, 25, 27), (7, 1, 3), (7, 26, 28),
                  (8, 1, 2), (8, 27, 28), (9, 1, 2), (9, 27, 28)], "N"),
        # wing layering: mid-blue diagonal bands inside
        ("runs", [(r, c, c) for r, c in ((7, 4), (7, 6), (8, 3), (8, 5),
                                         (8, 7), (9, 2), (9, 4), (9, 6),
                                         (10, 5), (10, 7), (11, 6),
                                         (11, 8))], "D"),
        ("runs", [(r, c, c) for r, c in ((7, 25), (7, 23), (8, 26), (8, 24),
                                         (8, 22), (9, 27), (9, 25), (9, 23),
                                         (10, 24), (10, 22), (11, 23),
                                         (11, 21))], "D"),
        # white spots on the dark fingertips
        ("runs", [(5, 4, 4), (5, 25, 25), (6, 3, 3), (6, 26, 26),
                  (7, 2, 2), (7, 27, 27)], "W"),
        # head: mid blue with yellow eyes
        ("runs", [(5, 12, 17), (6, 11, 18)], "D"),
        ("put", 7, 12, "Y"),
        ("put", 7, 17, "Y"),
        # white chest diamond
        ("runs", [(9, 13, 16), (10, 12, 17), (11, 12, 17), (12, 13, 16)], "W"),
        # wing finger notches on the bottom edge
        ("runs", [(15, 6, 7), (16, 9, 10), (15, 22, 23), (16, 19, 20)], "N"),
        # navy feet + tail tip
        ("runs", [(22, 12, 13), (22, 16, 17)], "N"),
        ("runs", [(21, 14, 15)], "N"),
    ],
}
