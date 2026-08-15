"""Hermitaur, carapaceon. The small shore crab, side view: a low red
shell dome with cream spikes and a cream rim along its bottom edge, a
cream face patch with beady eyes at the front, a small far claw and a
bigger near claw with an open pincer hanging down-forward, and three
pointed legs."""

CONFIG = {
    "name": "hermitaur",
    "size": (30, 24),
    "compare_to": "../icons/mhst2/hermitaur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (198, 72, 58, 255),     # red shell
        "D": (150, 48, 42, 255),     # dark red claws / legs
        "C": (226, 204, 168, 255),   # cream rim / face / spikes
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        1:  [(15, 16)],                        # spike tip
        2:  [(14, 17)],
        3:  [(9, 19)],                         # dome top
        4:  [(8, 21)],
        5:  [(8, 22)],
        6:  [(8, 23)],
        7:  [(8, 23)],
        8:  [(8, 23)],
        9:  [(8, 23)],
        10: [(8, 22)],
        11: [(8, 22)],
        12: [(0, 2), (3, 21)],                 # far claw + body band
        13: [(0, 2), (3, 21)],
        14: [(0, 1), (3, 20)],
        15: [(1, 7), (8, 19)],                 # claw top + body bottom
        16: [(0, 8), (9, 11), (14, 16), (18, 20)],
        17: [(0, 8), (10, 10), (15, 15), (19, 19)],
        18: [(5, 8)],                          # open pincer slot cols 0-4
        19: [(5, 8)],
        20: [(1, 8)],                          # lower pincer
        21: [(2, 7)],
    },
    "fills": [
        # near claw in darker red, white cutting edge on the upper pincer
        ("runs", [(15, 1, 7), (16, 0, 8), (17, 0, 8), (18, 5, 8),
                  (19, 5, 8), (20, 1, 8), (21, 2, 7)], "D"),
        ("runs", [(15, 2, 6), (16, 1, 6)], "W", "D"),
        ("put", 21, 2, "W"),
        # small far claw, dark
        ("runs", [(12, 0, 2), (13, 0, 2), (14, 0, 1)], "D"),
        ("put", 12, 0, "W"),
        # cream shell spikes
        ("runs", [(1, 15, 16), (2, 14, 17)], "C"),
        # dark spots on the dome
        ("runs", [(5, 13, 14), (6, 17, 18), (7, 11, 12),
                  (8, 15, 16), (8, 19, 20), (9, 13, 14)], "D"),
        # cream rim along the shell bottom edge
        ("runs", [(10, 9, 22), (11, 9, 22), (12, 8, 21)], "C"),
        # cream face patch at the front, beady eyes
        ("runs", [(12, 3, 7), (13, 3, 7), (14, 3, 7)], "C"),
        ("put", 13, 4, "K"),
        ("put", 13, 6, "K"),
        # pointed legs, dark with pale tips
        ("runs", [(16, 9, 11), (16, 14, 16), (16, 18, 20)], "D"),
        ("put", 17, 10, "W"),
        ("put", 17, 15, "W"),
        ("put", 17, 19, "W"),
    ],
}
