"""Jagras, small pack fanged wyvern. The little monitor: blunt head with
an open fanged jaw, yellow-green body with dark bands, low tail, four
stubby legs. The pack-lizard archetype the girros variants derive from."""

CONFIG = {
    "name": "jagras",
    "size": (26, 24),
    "compare_to": "../icons/mhrise/jagras.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (150, 160, 100, 255),  # yellow-green scales
        "D": (105, 115, 72, 255),   # darker bands / shade
        "Y": (228, 205, 60, 255),   # yellow neck stripes / spikes
        "O": (180, 150, 80, 255),   # tan belly
        "W": (245, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        5:  [(2, 5)],                         # head top
        6:  [(1, 7), (11, 11), (14, 14)],     # head + back spikes
        7:  [(0, 9), (10, 16)],
        8:  [(6, 18)],                        # open mouth gap cols 0-5
        9:  [(0, 5), (7, 20)],                # lower jaw + body
        10: [(1, 5), (8, 21)],
        11: [(2, 21)],
        12: [(2, 22)],
        13: [(3, 23)],
        14: [(4, 24)],
        15: [(5, 25)],
        16: [(7, 25)],                        # tail tip
        17: [(6, 9), (13, 15), (19, 22)],     # legs
        18: [(6, 6), (8, 8), (13, 13), (15, 15), (19, 19), (21, 21)],
    },
    "fills": [
        # eye
        ("put", 6, 3, "W"),
        ("put", 6, 4, "K"),
        # fangs in the mouth gap
        ("put", 8, 1, "W"),
        ("put", 8, 4, "W"),
        # yellow neck stripes
        ("runs", [(9, 8, 9), (10, 8, 9), (11, 9, 10), (12, 10, 11),
                  (9, 12, 13), (10, 12, 13), (11, 13, 14)], "Y"),
        # dark bands on the back and tail
        ("runs", [(9, 15, 16), (10, 17, 18), (11, 18, 19), (12, 19, 20),
                  (13, 20, 21), (14, 21, 22), (15, 22, 23)], "D"),
        # tan belly along the bottom edge
        ("runs", [(13, 4, 16), (14, 5, 18), (15, 6, 19)], "O"),
        # yellow back spikes
        ("runs", [(6, 11, 11), (6, 14, 14)], "Y"),
        # claws
        ("put", 18, 6, "W"),
        ("put", 18, 8, "W"),
        ("put", 18, 13, "W"),
        ("put", 18, 15, "W"),
        ("put", 18, 19, "W"),
        ("put", 18, 21, "W"),
    ],
}
