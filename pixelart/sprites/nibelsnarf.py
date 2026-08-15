"""Nibelsnarf, leviathan. The sand-swallowing tube: a very long, low
tan body whose whole front third is an agape ring mouth with thin teeth
all around, two tiny goofy eyes on top of the head, a spiked sand-fin
arch on the back, dark pattern bands, a cream underside, small leg fins,
and a flat tail fan."""

CONFIG = {
    "name": "nibelsnarf",
    "size": (46, 24),
    "compare_to": "../icons/mhgu/nibelsnarf.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "T": (194, 152, 102, 255),   # tan hide
        "D": (146, 108, 66, 255),    # brown pattern / fins
        "C": (228, 206, 168, 255),   # pale underside
        "W": (246, 242, 230, 255),
    },
    "base": "T",
    "spans": {
        2:  [(15, 16), (27, 28)],              # sand fin tips
        3:  [(14, 17), (26, 29)],
        4:  [(13, 18), (25, 30)],
        5:  [(2, 19), (24, 32)],
        6:  [(1, 33), (23, 34)],
        7:  [(0, 35), (37, 40)],
        8:  [(0, 36), (36, 42)],
        9:  [(0, 37), (35, 44)],
        10: [(0, 38), (35, 45)],
        11: [(0, 38), (34, 45)],
        12: [(11, 38), (34, 44)],              # mouth gap cols 0-10
        13: [(11, 37), (33, 43)],
        14: [(11, 36), (32, 42)],
        15: [(0, 10), (12, 34), (33, 40)],     # lower jaw + belly + tail
        16: [(1, 10), (13, 32), (35, 38)],
        17: [(2, 9), (14, 17), (22, 25), (36, 36)],
        18: [(3, 7), (14, 15), (17, 17), (22, 23), (25, 25)],
    },
    "fills": [
        # two tiny goofy eyes on top of the head
        ("put", 6, 4, "K"),
        ("put", 6, 9, "K"),
        # ring mouth: thin teeth all around the black gap
        ("put", 12, 2, "W"),
        ("put", 12, 5, "W"),
        ("put", 12, 8, "W"),
        ("put", 14, 3, "W"),
        ("put", 14, 6, "W"),
        ("put", 14, 9, "W"),
        ("put", 16, 2, "W"),
        ("put", 16, 5, "W"),
        ("put", 16, 8, "W"),
        # dark sand-fin arch on the back
        ("runs", [(2, 15, 16), (2, 27, 28), (3, 14, 17), (3, 26, 29),
                  (4, 13, 18), (4, 25, 30), (5, 13, 18), (5, 25, 32)],
         "D"),
        # dark pattern bands over the body
        ("runs", [(7, 20, 21), (8, 26, 27), (9, 22, 23), (10, 30, 31),
                  (11, 25, 26), (12, 29, 30), (8, 14, 15), (10, 17, 18)],
         "D"),
        # cream underside along the bottom edge
        ("runs", [(14, 13, 28), (15, 12, 32), (16, 13, 30)], "C"),
        # flat tail fan, darker
        ("runs", [(7, 37, 40), (8, 36, 42), (9, 35, 44), (10, 35, 45),
                  (11, 34, 45), (12, 34, 44), (13, 33, 43),
                  (14, 32, 42), (15, 33, 40), (16, 35, 38)], "D"),
        ("runs", [(9, 40, 40), (10, 42, 42), (11, 43, 43),
                  (12, 42, 42), (13, 40, 40)], "C", "D"),
        # pale lower jaw
        ("runs", [(15, 0, 10), (16, 1, 10), (17, 2, 9), (18, 3, 7)], "C"),
        # small leg fins
        ("runs", [(17, 14, 17), (18, 14, 15), (18, 17, 17)], "D", "T"),
        ("runs", [(17, 22, 25), (18, 22, 23), (18, 25, 25)], "D", "T"),
        ("put", 18, 14, "W"),
        ("put", 18, 17, "W"),
        ("put", 18, 22, "W"),
        ("put", 18, 25, "W"),
    ],
}
