"""Ceanataur, carapaceon. The blade crab, side view: a low blue shell
dome with a tall back spike, a grey body band with a beady eye at the
front, the signature scissor claw hanging down-forward with an open
slot, a dark blade and white cutting edge, and three thin pointed
legs."""

CONFIG = {
    "name": "ceanataur",
    "size": (32, 24),
    "compare_to": "../icons/mhfu/ceanataur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (76, 110, 182, 255),    # blue shell
        "D": (52, 78, 140, 255),     # dark blue blade / shade
        "G": (168, 164, 152, 255),   # grey body / face
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(21, 23)],                        # back spike tip
        2:  [(20, 24)],
        3:  [(11, 25)],                        # dome top + spike base
        4:  [(10, 26)],
        5:  [(10, 27)],
        6:  [(10, 27)],
        7:  [(10, 27)],
        8:  [(10, 27)],
        9:  [(10, 26)],
        10: [(10, 26)],
        11: [(10, 25)],
        12: [(0, 2), (4, 24)],                 # far claw + body band
        13: [(0, 2), (4, 24)],
        14: [(0, 1), (4, 23)],
        15: [(1, 8), (9, 22)],                 # blade top + body bottom
        16: [(0, 9), (11, 13), (16, 18), (20, 21)],
        17: [(0, 9), (12, 12), (17, 17), (21, 21)],
        18: [(6, 9)],                          # open scissor slot cols 0-5
        19: [(6, 9)],
        20: [(1, 9)],                          # lower blade
        21: [(2, 8)],
    },
    "fills": [
        # grey body band along the bottom edge
        ("runs", [(11, 10, 25), (12, 4, 24), (13, 4, 24),
                  (14, 4, 23)], "G"),
        # scissor claw: dark blade with white cutting edge
        ("runs", [(15, 1, 8), (16, 0, 9), (17, 0, 9), (18, 6, 9),
                  (19, 6, 9), (20, 1, 9), (21, 2, 8)], "D"),
        ("runs", [(15, 2, 7), (16, 1, 7), (18, 8, 8), (19, 8, 8)],
         "W", "D"),
        ("put", 21, 2, "W"),
        # small far claw
        ("runs", [(12, 0, 2), (13, 0, 2), (14, 0, 1)], "D"),
        ("put", 12, 0, "W"),
        # beady eye on the grey face
        ("put", 12, 5, "K"),
        ("put", 13, 5, "K"),
        # shell back shade + dark spike
        ("runs", [(2, 20, 24), (3, 21, 25), (4, 23, 26), (5, 24, 27),
                  (6, 24, 27), (7, 24, 27), (8, 24, 27), (9, 23, 26),
                  (10, 23, 26), (11, 22, 25)], "D"),
        # thin pointed legs, dark with pale tips
        ("runs", [(16, 11, 13), (16, 16, 18), (16, 20, 21)], "D"),
        ("put", 17, 12, "W"),
        ("put", 17, 17, "W"),
        ("put", 17, 21, "W"),
    ],
}
