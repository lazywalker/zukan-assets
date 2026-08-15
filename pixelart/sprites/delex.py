"""Delex, piscine wyvern. The sand dart: a slim yellow bullet-fish at a
jumping angle, snout up-left, a red eye, fin crest along the spine, and a
split tail, drawn mid-leap out of the sand."""

CONFIG = {
    "name": "delex",
    "size": (26, 24),
    "compare_to": "../icons/mhrise/delex.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "Y": (216, 186, 96, 255),   # sandy yellow body
        "D": (172, 142, 68, 255),   # darker yellow bands
        "R": (204, 70, 58, 255),    # red eye / fin
        "C": (232, 212, 160, 255),  # pale belly
        "W": (246, 242, 230, 255),
    },
    "base": "Y",
    "spans": {
        5:  [(6, 9), (14, 15)],               # crest + tail tip
        6:  [(5, 10), (13, 16)],
        7:  [(4, 11), (12, 18)],
        8:  [(3, 12), (11, 20)],              # snout + body
        9:  [(2, 12), (10, 21)],
        10: [(1, 12), (10, 22)],              # snout tip col 1
        11: [(1, 11), (10, 23)],
        12: [(2, 11), (11, 24)],
        13: [(3, 10), (13, 24)],              # tail split
        14: [(4, 10), (16, 23)],
        15: [(5, 9), (19, 22)],
        16: [(6, 8), (21, 21)],
    },
    "fills": [
        # red fin crest along the spine
        ("runs", [(5, 14, 15), (6, 13, 16), (7, 12, 17)], "R"),
        # big red eye near the snout
        ("put", 8, 4, "K"),
        ("put", 8, 5, "R"),
        # jagged grin
        ("runs", [(10, 2, 6)], "K"),
        ("put", 10, 3, "W"),
        ("put", 10, 5, "W"),
        # darker bands across the body
        ("runs", [(9, 14, 16), (10, 16, 18), (11, 18, 20),
                  (12, 19, 21)], "D"),
        # pale belly along the bottom edge
        ("runs", [(12, 3, 9), (13, 4, 9), (14, 5, 9), (15, 6, 8)], "C"),
        # tail split red
        ("runs", [(13, 20, 24), (14, 21, 23)], "R"),
        ("put", 16, 21, "R"),
    ],
}
