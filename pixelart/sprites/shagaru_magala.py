"""Shagaru Magala, elder dragon. The golden heaven: Gore Magala's mature
form; golden scales, wing-limbs spread in a radiant arc, ram horns, purple
accents, pale gold eyes. Radiant symmetric arc is the signature."""

CONFIG = {
    "name": "shagaru-magala",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/shagaru-magala.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (220, 180, 80, 255),   # golden scales
        "L": (240, 215, 140, 255),  # light gold: wings
        "P": (120, 80, 160, 255),   # purple accents
        "D": (170, 130, 55, 255),   # dark gold shade
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(6, 7), (13, 14), (24, 25)],
        4:  [(4, 8), (12, 16), (23, 26)],
        5:  [(3, 9), (11, 18), (22, 27)],
        6:  [(2, 10), (10, 20), (21, 28)],
        7:  [(1, 11), (9, 22), (20, 28)],
        8:  [(1, 12), (9, 22), (20, 28)],
        9:  [(1, 13), (9, 21), (19, 27)],
        10: [(2, 13), (10, 21), (19, 26)],
        11: [(3, 13), (11, 20), (18, 25)],
        12: [(4, 13), (12, 19), (17, 24)],
        13: [(5, 13), (13, 18), (16, 23)],
        14: [(6, 13), (14, 17), (16, 22)],
        15: [(7, 12), (16, 21)],
        16: [(8, 11), (17, 20)],
        17: [(9, 10), (18, 19)],
        18: [(10, 12), (17, 18)],
        19: [(11, 12), (17, 17)],
    },
    "fills": [
        # ram horns, purple
        ("runs", [(3, 6, 7), (4, 4, 5), (5, 3, 4)], "P"),
        ("runs", [(3, 13, 14), (4, 15, 16), (5, 16, 17)], "P"),
        # white eyes
        ("put", 6, 4, "W"),
        ("put", 6, 8, "W"),
        # radiant wing arcs: light gold with purple tips
        ("runs", [(3, 24, 25), (4, 23, 26), (5, 22, 27), (6, 21, 28),
                  (7, 20, 28), (8, 20, 28), (9, 19, 27), (10, 19, 26)],
         "L"),
        ("runs", [(6, 28, 28), (7, 27, 28), (8, 27, 28)], "P"),
        # body shade
        ("runs", [(13, 6, 9), (14, 6, 8), (15, 7, 9)], "D"),
        # tail spikes
        ("runs", [(15, 16, 17), (16, 17, 18), (17, 18, 19)], "P"),
    ],
}
