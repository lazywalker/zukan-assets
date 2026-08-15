"""Gypceros, bird wyvern. The poison rubber bird: purple-blue rubbery
body, a wide crest comb like a fan on top of the head with an orange knob
at the front, a long straight pale beak, white ringed eye, green poison
only on the tail tip. No mouth blob."""

CONFIG = {
    "name": "gypceros",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/gypceros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (140, 120, 175, 255),  # purple-blue rubber body
        "C": (185, 170, 210, 255),  # pale lavender belly
        "H": (170, 150, 200, 255),  # crest comb
        "G": (150, 190, 90, 255),   # green poison (tail tip)
        "O": (235, 150, 60, 255),   # orange head knob
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(3, 12)],                        # crest comb
        4:  [(2, 12), (10, 11)],
        5:  [(1, 12), (11, 11)],
        6:  [(0, 12)],
        7:  [(0, 12)],
        8:  [(1, 11)],
        9:  [(2, 12), (13, 24)],
        10: [(3, 13), (14, 26)],
        11: [(4, 14), (15, 27)],
        12: [(5, 14), (16, 28)],
        13: [(6, 14), (17, 29)],
        14: [(7, 14), (18, 30)],
        15: [(8, 20), (21, 30)],
        16: [(9, 21), (22, 29)],
        17: [(11, 14), (15, 18), (20, 23), (24, 28)],
        18: [(11, 14), (21, 23), (24, 27)],
        19: [(11, 13), (21, 22), (25, 26)],
        20: [(12, 13), (21, 22)],
        21: [(12, 12), (13, 13), (21, 21), (22, 22)],
    },
    "fills": [
        # wide crest comb fan, orange knob at the front
        ("runs", [(3, 3, 12), (4, 2, 10)], "H"),
        ("runs", [(4, 2, 3), (5, 1, 2)], "O"),
        # white ringed eye
        ("put", 6, 4, "W"),
        ("put", 6, 5, "K"),
        # long straight pale beak
        ("runs", [(6, 0, 1), (7, 0, 1), (8, 1, 2)], "C"),
        # pale belly along the bottom edge
        ("runs", [(14, 8, 13), (15, 8, 13), (16, 9, 13)], "C"),
        # green poison only at the tail tip
        ("runs", [(13, 26, 28), (14, 27, 29)], "G"),
        # claws
        ("put", 21, 12, "W"),
        ("put", 21, 13, "W"),
        ("put", 21, 21, "W"),
        ("put", 21, 22, "W"),
    ],
}
