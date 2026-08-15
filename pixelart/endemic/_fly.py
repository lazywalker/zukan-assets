"""Fly archetype: a flier with two raised wings separated from the body
by a 1px channel, round thorax, segmented abdomen, big eye, and dangling
legs. Hoppers patch big hind legs onto it."""

CONFIG = {
    "name": "_fly",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (110, 116, 140, 255),  # body
        "D": (82, 88, 110, 255),    # darker abdomen
        "W": (230, 232, 240, 255),  # wings
        "G": (240, 210, 90, 255),   # glow accent
    },
    "base": "B",
    "spans": {
        3:  [(10, 12), (16, 18)],
        4:  [(9, 13), (15, 19)],
        5:  [(9, 13), (15, 19)],
        6:  [(9, 12), (15, 18)],
        7:  [(8, 12), (14, 20)],
        8:  [(6, 12), (13, 21)],
        9:  [(5, 22)],
        10: [(4, 23)],
        11: [(4, 23)],
        12: [(5, 22)],
        13: [(6, 20)],
        14: [(7, 9), (13, 15)],
        15: [(7, 7), (9, 9), (13, 13), (15, 15)],
    },
    "fills": [
        # wings translucent with a vein line
        ("runs", [(3, 10, 12), (4, 9, 13), (5, 9, 13), (6, 9, 12)], "W"),
        ("runs", [(3, 16, 18), (4, 15, 19), (5, 15, 19), (6, 15, 18)],
         "W"),
        ("put", 4, 11, "D"),
        ("put", 4, 17, "D"),
        # thorax + abdomen split
        ("runs", [(8, 6, 12), (9, 5, 10)], "D"),
        ("runs", [(10, 14, 23), (11, 14, 23), (12, 15, 22)], "D"),
        # big eye + glow dot on the abdomen
        ("put", 8, 8, "K"),
        ("put", 8, 7, "W"),
        ("put", 11, 18, "G"),
    ],
}
