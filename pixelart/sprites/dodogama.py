"""Dodogama, fanged wyvern. The boulder-chinned rounder: plump blue body
swelling into a huge pale boulder jaw, small dark back spikes, stubby
legs, tiny orange eye buried in the mass."""

CONFIG = {
    "name": "dodogama",
    "size": (28, 24),
    "compare_to": "../icons/mhw/dodogama.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (95, 132, 185, 255),   # blue body
        "D": (62, 96, 145, 255),    # darker blue spikes / shade
        "P": (188, 202, 212, 255),  # pale boulder chin
        "Y": (232, 165, 60, 255),   # orange eye
        "W": (245, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(9, 10), (16, 17)],              # back spike tips
        4:  [(7, 19)],
        5:  [(5, 21)],
        6:  [(4, 22)],
        7:  [(3, 23)],
        8:  [(2, 24)],
        9:  [(1, 25)],
        10: [(0, 25)],                        # chin mass pushes left
        11: [(0, 26)],
        12: [(0, 26)],
        13: [(1, 26)],
        14: [(2, 25)],
        15: [(4, 24)],
        16: [(6, 22)],
        17: [(7, 11), (16, 20)],              # legs
        18: [(7, 10), (17, 19)],
        19: [(7, 7), (9, 9), (17, 17), (19, 19)],
    },
    "fills": [
        # dark back spikes
        ("runs", [(3, 9, 10), (3, 16, 17), (4, 7, 8), (4, 18, 19)], "D"),
        # tiny orange eye high on the mass
        ("put", 7, 5, "K"),
        ("put", 7, 6, "Y"),
        # pale boulder chin, front-bottom third of the ball
        ("runs", [(9, 1, 8), (10, 0, 9), (11, 0, 10), (12, 0, 10),
                  (13, 1, 9), (14, 2, 7)], "P"),
        # boulder cracks
        ("runs", [(10, 4, 4), (11, 7, 7), (12, 3, 3), (12, 8, 8)], "D", "P"),
        # darker top shade
        ("runs", [(5, 12, 21), (6, 14, 22), (7, 16, 23)], "D"),
        # belly shade
        ("runs", [(14, 8, 24), (15, 9, 23), (16, 10, 21)], "D"),
        # claws
        ("put", 19, 7, "W"),
        ("put", 19, 9, "W"),
        ("put", 19, 17, "W"),
        ("put", 19, 19, "W"),
    ],
}
