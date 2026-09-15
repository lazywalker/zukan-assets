"""Akantor, flying wyvern. The black fang, drawn in the maned front of
its icon: a blazing orange spike mane radiating around a dark face with
glaring yellow eyes, giant pale tusks curving up on both sides, a white
fang row under the snout, and an orange banded body below."""

CONFIG = {
    "name": "akantor",
    "size": (36, 24),
    "compare_to": "../icons/mh4u/akantor.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (238, 108, 26, 255),    # blazing orange mane
        "R": (150, 54, 18, 255),     # dark rust spikes
        "D": (70, 32, 14, 255),      # dark brown face
        "C": (225, 195, 145, 255),   # pale tusks
        "E": (190, 150, 100, 255),   # dark tusk shade
        "Y": (240, 190, 60, 255),    # eye yellow
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        1:  [(16, 19)],                          # mane peak
        2:  [(13, 22)],
        3:  [(11, 24)],
        4:  [(9, 15), (20, 26)],                 # mane splits for face
        5:  [(8, 14), (21, 27)],
        6:  [(4, 7), (12, 13), (22, 23), (28, 31)],   # tusks + mane
        7:  [(4, 8), (10, 12), (23, 25), (27, 31)],
        8:  [(3, 9), (9, 26), (26, 32)],         # mane ring + face
        9:  [(3, 9), (8, 27), (26, 32)],
        10: [(3, 9), (8, 27), (26, 32)],
        11: [(3, 9), (8, 27), (26, 32)],
        12: [(4, 9), (8, 27), (26, 31)],         # tusk bases
        13: [(5, 9), (8, 27), (26, 30)],         # face bottom
        14: [(6, 29)],                           # jaw
        15: [(7, 28)],                           # body
        16: [(7, 28)],
        17: [(8, 27)],
        18: [(9, 26)],
        19: [(10, 25)],
        20: [(12, 23)],
    },
    "fills": [
        # dark rust spikes across the mane crown
        ("runs", [(2, 14, 15), (2, 20, 21), (3, 12, 13), (3, 22, 23),
                  (4, 10, 11), (4, 24, 25), (5, 9, 10), (5, 25, 26)],
         "R", "O"),
        # dark face between the mane
        ("runs", [(4, 16, 19), (5, 15, 20), (6, 14, 21), (7, 13, 22),
                  (8, 10, 25), (9, 9, 26), (10, 9, 26), (11, 9, 26),
                  (12, 10, 25), (13, 9, 26)], "D"),
        # giant pale tusks curving up both sides
        ("runs", [(6, 4, 7), (7, 4, 8), (8, 3, 9), (9, 3, 9), (10, 3, 9),
                  (11, 3, 9), (12, 4, 9), (13, 5, 9), (6, 28, 31),
                  (7, 27, 31), (8, 26, 32), (9, 26, 32), (10, 26, 32),
                  (11, 26, 32), (12, 26, 31), (13, 26, 30)], "C", "O"),
        ("runs", [(7, 4, 5), (8, 3, 4), (9, 3, 4), (10, 3, 4),
                  (7, 30, 31), (8, 31, 32), (9, 31, 32), (10, 31, 32)],
         "E", "C"),
        # glaring yellow eyes with dark pupils
        ("runs", [(9, 12, 14), (9, 21, 23), (10, 12, 14), (10, 21, 23)],
         "Y", "D"),
        ("put", 9, 13, "K"),
        ("put", 9, 22, "K"),
        # white fang row under the snout
        ("runs", [(13, 14, 21)], "D", "D"),
        ("put", 13, 14, "W"),
        ("put", 13, 16, "W"),
        ("put", 13, 19, "W"),
        ("put", 13, 21, "W"),
        # orange body with rust bands
        ("runs", [(15, 8, 12), (15, 23, 27), (16, 8, 11), (16, 24, 27),
                  (17, 9, 12), (17, 23, 26)], "R", "O"),
        ("runs", [(16, 15, 20)], "D", "O"),
        ("runs", [(18, 13, 22)], "D", "O"),
        ("runs", [(19, 14, 21), (20, 16, 19)], "R", "O"),
    ],
}
