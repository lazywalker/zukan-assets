"""Great Jagras, fat hunched lizard. Quadruped archetype, low and bulky.
Reference pose from icons/mhw/great-jagras.png: blunt big head, vertical
bright-yellow neck stripes, dark green body, gold back spikes, orange-brown
belly, stubby legs.
"""

CONFIG = {
    "name": "great-jagras",
    "size": (34, 24),
    "compare_to": "../icons/mhw/great-jagras.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "G": (70, 95, 60, 255),     # dark green body
        "D": (46, 64, 40, 255),     # darker green shade
        "Y": (230, 215, 40, 255),   # bright yellow neck stripes
        "O": (180, 125, 30, 255),   # orange-brown belly
        "S": (200, 170, 50, 255),   # gold back spikes
        "W": (245, 242, 230, 255),  # teeth / eye
    },
    "base": "G",
    "spans": {
        4:  [(1, 6), (16, 17), (24, 26)],         # head top, spike, tail spike
        5:  [(1, 8), (15, 16), (20, 21), (23, 27), (26, 29)],
        6:  [(1, 9), (13, 14), (17, 18), (15, 25), (25, 30)],
        7:  [(1, 10), (12, 28), (24, 30)],
        8:  [(1, 1), (6, 10), (11, 29)],          # mouth gap c2-5
        9:  [(3, 10), (10, 30)],
        10: [(3, 10), (10, 30)],
        11: [(4, 10), (10, 30)],
        12: [(4, 29)],
        13: [(5, 28)],
        14: [(5, 27)],
        15: [(6, 26)],
        16: [(7, 25)],
        17: [(8, 12), (20, 24)],
        18: [(8, 12), (20, 24)],
        19: [(8, 11), (20, 23)],
        20: [(7, 11), (20, 23)],
        21: [(7, 7), (9, 9), (20, 20), (22, 22)],
    },
    "fills": [
        # eye + fangs in the mouth gap
        ("put", 6, 3, "WK"),
        ("put", 8, 3, "W"),
        ("put", 8, 5, "W"),
        # yellow vertical neck stripes (2px bands + accent)
        ("runs", [(r, 11, 12) for r in range(7, 13)]
               + [(r, 15, 16) for r in range(7, 12)]
               + [(r, 18, 18) for r in range(7, 11)], "Y"),
        # back + tail spikes gold
        ("runs", [(4, 16, 17), (4, 21, 21), (5, 15, 16), (5, 20, 21),
                  (5, 23, 27), (6, 13, 14), (6, 17, 18), (6, 25, 30)], "S"),
        # orange belly, lower half only
        ("runs", [(13, 6, 26), (14, 5, 25), (15, 6, 24), (16, 7, 23)], "O"),
        # dark green top shading
        ("runs", [(7, 12, 28), (8, 11, 29), (9, 20, 30)], "D"),
        # claws
        ("put", 21, 7, "W"),
        ("put", 21, 9, "W"),
        ("put", 21, 20, "W"),
        ("put", 21, 22, "W"),
    ],
}
