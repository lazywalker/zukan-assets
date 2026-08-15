"""Wulg, small fanged wyvern. The tundra fluffball: pale cream fluff over
a low round body, a dark brown head with a single cyan tusk jutting
forward, stubby legs, short fluffed tail."""

CONFIG = {
    "name": "wulg",
    "size": (24, 24),
    "compare_to": "../icons/mhwi/wulg.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (222, 210, 190, 255),  # cream fluff
        "D": (185, 172, 150, 255),  # fluff shade
        "H": (86, 60, 50, 255),     # dark brown head
        "T": (118, 190, 200, 255),  # cyan tusk
        "W": (245, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        6:  [(8, 12)],                         # head top
        7:  [(6, 14)],
        8:  [(4, 16), (17, 19)],               # head + tail fluff
        9:  [(3, 19)],
        10: [(2, 20)],
        11: [(2, 21)],                         # body
        12: [(3, 21)],
        13: [(4, 20)],
        14: [(5, 19)],
        15: [(6, 12), (16, 18)],               # legs + tail
        16: [(7, 8), (10, 10), (16, 16), (18, 18)],
    },
    "fills": [
        # cyan tusk jutting forward from the chin
        ("runs", [(9, 2, 4)], "T"),
        ("put", 8, 3, "T"),
        # dark head with a pale brow dot
        ("runs", [(6, 8, 12), (7, 6, 14), (8, 4, 14), (9, 5, 13)], "H"),
        ("put", 7, 8, "W"),
        # fluff shade along the belly
        ("runs", [(11, 3, 12), (12, 4, 13), (13, 5, 13), (14, 6, 12)], "D"),
        # fluff bumps on the back
        ("runs", [(9, 15, 16), (10, 17, 18)], "W", "F"),
        # claws
        ("put", 16, 7, "W"),
        ("put", 16, 10, "W"),
        ("put", 16, 16, "W"),
        ("put", 16, 18, "W"),
    ],
}
