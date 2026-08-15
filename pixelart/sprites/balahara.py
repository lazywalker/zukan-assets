"""Balahara, leviathan. The sand flower: a purple serpentine body with the
giant petal-fan mouth flared wide at the left, a teal chin beneath, and
the body winding right into a pointed tail."""

CONFIG = {
    "name": "balahara",
    "size": (36, 24),
    "compare_to": "../icons/mhwilds/balahara.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (148, 108, 158, 255),  # purple scales
        "D": (116, 82, 128, 255),   # darker purple
        "T": (118, 178, 156, 255),  # teal chin
        "S": (196, 168, 200, 255),  # pale petal fan
        "Y": (232, 190, 70, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        1:  [(2, 4), (7, 9), (12, 13)],       # petal tips
        2:  [(1, 5), (6, 10), (11, 14)],
        3:  [(0, 6), (5, 11), (10, 15)],
        4:  [(0, 7), (4, 12), (9, 16)],       # fan mouth wide open
        5:  [(0, 8), (3, 13), (8, 17)],
        6:  [(0, 9), (2, 14), (7, 18)],
        7:  [(1, 10), (1, 15), (6, 19)],      # jaw pivot + head
        8:  [(1, 10), (5, 20)],
        9:  [(1, 10), (5, 22)],
        10: [(1, 10), (6, 24)],
        11: [(2, 10), (8, 26)],
        12: [(2, 10), (10, 28)],
        13: [(3, 10), (12, 30)],
        14: [(3, 10), (15, 32)],
        15: [(4, 10), (18, 34)],
        16: [(4, 10), (22, 35)],
        17: [(5, 10), (26, 35)],
        18: [(5, 10), (30, 34)],              # tail tip
        19: [(5, 10), (32, 33)],
    },
    "fills": [
        # pale petal fan with dark seams
        ("runs", [(1, 2, 4), (2, 1, 5), (3, 0, 6), (4, 0, 7),
                  (5, 0, 8), (6, 0, 9)], "S"),
        ("runs", [(1, 7, 9), (2, 6, 10), (3, 5, 11), (4, 4, 12)], "S"),
        ("runs", [(1, 12, 13), (2, 11, 14), (3, 10, 15), (4, 9, 16),
                  (5, 8, 17)], "S"),
        ("runs", [(3, 6, 6), (4, 8, 8), (5, 10, 10), (6, 12, 12)], "D"),
        # teal chin under the fan
        ("runs", [(7, 1, 10), (8, 1, 9)], "T"),
        # yellow eyes above the chin
        ("put", 6, 7, "Y"),
        ("put", 6, 9, "Y"),
        # body shade along the top
        ("runs", [(9, 12, 21), (10, 14, 23), (11, 16, 25),
                  (12, 18, 27)], "D"),
        # pale belly along the bottom edge
        ("runs", [(15, 5, 9), (16, 5, 9), (17, 5, 9), (18, 5, 9)], "S"),
        # tail tip dark
        ("runs", [(17, 30, 35), (18, 31, 34)], "D"),
    ],
}
