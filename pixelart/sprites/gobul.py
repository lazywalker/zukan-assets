"""Gobul, leviathan. The anglerfish puffer, side view: a bulbous
purple-slate body ringed by cream bone spines, a huge gaping mouth with
thin teeth, a small yellow eye high on the head, dark spots over the
back, a glowing green lure bulb hanging from the chin on a thin stem,
and a small tapering tail."""

CONFIG = {
    "name": "gobul",
    "size": (34, 24),
    "compare_to": "../icons/mh3u/gobul.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (118, 106, 146, 255),   # purple-slate body
        "D": (86, 74, 112, 255),     # dark purple spots / shade
        "C": (222, 208, 184, 255),   # pale spines / belly
        "Y": (232, 192, 74, 255),
        "G": (150, 220, 180, 255),   # lure glow
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(13, 13), (18, 18), (23, 23)],    # spine tips
        3:  [(12, 14), (17, 19), (22, 24)],
        4:  [(11, 15), (16, 20), (21, 25)],
        5:  [(10, 26)],
        6:  [(9, 27)],
        7:  [(8, 28)],
        8:  [(7, 29)],
        9:  [(5, 30)],
        10: [(4, 30)],
        11: [(3, 31)],
        12: [(10, 31)],                        # mouth gap cols 2-9
        13: [(10, 30)],
        14: [(2, 9), (11, 29)],                # lower jaw + body
        15: [(3, 9), (11, 27)],
        16: [(6, 24), (4, 4)],                 # body bottom + lure stem
        17: [(7, 21), (3, 5)],                 # body + lure bulb
        18: [(8, 18), (3, 5)],
        19: [(9, 15)],
        20: [(10, 14)],
    },
    "fills": [
        # cream bone spines fanning over the back
        ("runs", [(2, 13, 13), (2, 18, 18), (2, 23, 23),
                  (3, 12, 14), (3, 17, 19), (3, 22, 24),
                  (4, 11, 15), (4, 16, 20), (4, 21, 25)], "C"),
        # small yellow eye high on the head, dark lid over it
        ("put", 8, 5, "K"),
        ("put", 9, 5, "Y"),
        ("put", 9, 6, "K"),
        # gaping mouth: thin teeth along both jaws
        ("put", 12, 3, "W"),
        ("put", 12, 5, "W"),
        ("put", 12, 7, "W"),
        ("put", 13, 4, "W"),
        ("put", 13, 6, "W"),
        ("put", 13, 8, "W"),
        # pale lower jaw
        ("runs", [(14, 2, 9), (15, 3, 9)], "C"),
        # dark spots over the round body
        ("runs", [(7, 14, 15), (8, 20, 21), (9, 11, 12), (10, 25, 26),
                  (11, 16, 17), (12, 22, 23), (11, 28, 28)], "D"),
        # pale belly along the bottom edge
        ("runs", [(14, 12, 24), (15, 13, 24), (16, 14, 22)], "C"),
        # tail tapers dark
        ("runs", [(16, 18, 24), (17, 16, 21), (18, 13, 18),
                  (19, 11, 15), (20, 11, 14)], "D"),
        # glowing lure: green bulb under the chin
        ("runs", [(17, 3, 5), (18, 3, 5)], "G"),
        ("put", 16, 4, "D"),
    ],
}
