"""Almudron, leviathan. The mud swimmer: a grey-blue serpentine body
rising from a mud mound, an orange-red frill flaring behind the head,
mud dripping off the flanks, small flipper arms."""

CONFIG = {
    "name": "almudron",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/almudron.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (128, 140, 156, 255),  # grey-blue body
        "D": (98, 110, 126, 255),   # darker shade
        "R": (222, 96, 58, 255),    # orange-red head frill
        "M": (140, 110, 78, 255),   # mud patches
        "C": (196, 200, 190, 255),  # pale belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(8, 10), (14, 16)],              # frill tips
        3:  [(6, 12), (13, 18)],
        4:  [(5, 19)],
        5:  [(4, 20)],
        6:  [(3, 21)],
        7:  [(2, 22)],                        # head + neck arch
        8:  [(2, 22), (23, 24)],
        9:  [(1, 22), (22, 26)],
        10: [(1, 22), (21, 28)],
        11: [(1, 22), (21, 30)],
        12: [(2, 22), (20, 31)],
        13: [(2, 21), (20, 32)],
        14: [(3, 21), (19, 33)],
        15: [(3, 20), (19, 33)],
        16: [(4, 19), (20, 32)],
        17: [(5, 18), (22, 31)],
        18: [(7, 17), (25, 29)],
        19: [(9, 12), (16, 17), (27, 28)],    # flippers
    },
    "fills": [
        # orange-red frill flaring behind the head
        ("runs", [(2, 8, 10), (2, 14, 16), (3, 6, 12), (3, 13, 18),
                  (4, 5, 12), (4, 16, 19), (5, 17, 20)], "R"),
        # yellow eye on the head
        ("put", 7, 5, "W"),
        ("put", 7, 6, "K"),
        # mud drips off the flanks
        ("runs", [(9, 23, 25), (10, 24, 27), (11, 23, 26)], "M"),
        ("runs", [(12, 28, 30), (13, 29, 31)], "M"),
        # pale belly along the bottom edge
        ("runs", [(14, 4, 18), (15, 4, 19), (16, 5, 18), (17, 6, 17)], "C"),
        # body shade
        ("runs", [(10, 14, 21), (11, 15, 21), (12, 14, 21)], "D"),
        # flippers dark
        ("runs", [(19, 9, 12), (19, 16, 17), (19, 27, 28)], "D"),
    ],
}
