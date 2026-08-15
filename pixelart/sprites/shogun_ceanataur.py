"""Shogun Ceanataur, carapaceon. The shogun blade crab, side view: a
bigger grey-banded body under a blue shell crowned with three spikes,
the massive scissor claw hanging down-forward with an open slot, a dark
blade and white cutting edge, a beady eye on the grey face, and four
thin pointed legs."""

CONFIG = {
    "name": "shogun-ceanataur",
    "size": (40, 24),
    "compare_to": "../icons/mhfu/shogun-ceanataur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (84, 122, 198, 255),    # blue shell
        "D": (56, 84, 150, 255),     # dark blue blade / shade
        "G": (172, 168, 156, 255),   # grey body / face
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        0:  [(24, 25), (31, 32)],              # crown spike tips
        1:  [(23, 26), (30, 33)],
        2:  [(13, 27), (29, 34)],
        3:  [(13, 33)],
        4:  [(12, 34)],
        5:  [(12, 35)],
        6:  [(12, 35)],
        7:  [(12, 35)],
        8:  [(12, 35)],
        9:  [(12, 35)],
        10: [(12, 35)],
        11: [(12, 35)],
        12: [(12, 34)],
        13: [(0, 3), (5, 33)],                 # far claw + body band
        14: [(0, 3), (5, 33)],
        15: [(0, 2), (5, 32)],
        16: [(1, 10), (11, 31)],               # blade top + body bottom
        17: [(0, 11), (13, 15), (18, 20), (23, 25), (27, 29)],
        18: [(0, 11), (14, 14), (19, 19), (24, 24), (28, 28)],
        19: [(7, 11)],                         # open scissor slot cols 0-6
        20: [(7, 11)],
        21: [(1, 11)],                         # lower blade
        22: [(2, 10)],
    },
    "fills": [
        # grey body band along the bottom edge
        ("runs", [(12, 12, 34), (13, 5, 33), (14, 5, 33),
                  (15, 5, 32)], "G"),
        # massive scissor claw, dark blade with white cutting edge
        ("runs", [(16, 1, 10), (17, 0, 11), (18, 0, 11), (19, 7, 11),
                  (20, 7, 11), (21, 1, 11), (22, 2, 10)], "D"),
        ("runs", [(16, 2, 9), (17, 1, 9), (19, 10, 10), (20, 10, 10)],
         "W", "D"),
        ("put", 22, 2, "W"),
        # small far claw
        ("runs", [(13, 0, 3), (14, 0, 3), (15, 0, 2)], "D"),
        ("put", 13, 0, "W"),
        # beady eye on the grey face
        ("put", 13, 6, "K"),
        ("put", 14, 6, "K"),
        # crown spikes over the shell
        ("runs", [(0, 24, 25), (0, 31, 32), (1, 23, 26), (1, 30, 33),
                  (2, 13, 18), (2, 22, 27), (2, 29, 34)], "D"),
        # shell back shade
        ("runs", [(4, 30, 34), (5, 31, 35), (6, 31, 35), (7, 31, 35),
                  (8, 31, 35), (9, 31, 35), (10, 31, 35),
                  (11, 31, 35), (12, 30, 34)], "D"),
        # thin pointed legs, dark with pale tips
        ("runs", [(17, 13, 15), (17, 18, 20), (17, 23, 25),
                  (17, 27, 29)], "D"),
        ("put", 18, 14, "W"),
        ("put", 18, 19, "W"),
        ("put", 18, 24, "W"),
        ("put", 18, 28, "W"),
    ],
}
