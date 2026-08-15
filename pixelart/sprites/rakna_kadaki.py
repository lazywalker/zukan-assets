"""Rakna-Kadaki, temnoceran. The ember widow: a pale yellow bulbous body
under a dark purple crown, orange legs splayed wide, and thread arms held
forward. The widow archetype the variants derive from."""

CONFIG = {
    "name": "rakna-kadaki",
    "size": (32, 24),
    "compare_to": "../icons/mhrise/rakna-kadaki.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "Y": (216, 202, 152, 255),  # pale yellow body
        "D": (178, 164, 118, 255),  # darker yellow
        "V": (88, 66, 116, 255),    # dark purple crown
        "O": (214, 118, 58, 255),   # orange legs
        "W": (246, 242, 230, 255),
    },
    "base": "Y",
    "spans": {
        2:  [(6, 10)],                        # crown
        3:  [(4, 12), (13, 14)],
        4:  [(3, 13), (12, 16)],
        5:  [(2, 14), (11, 17)],              # crown + legs
        6:  [(2, 15), (10, 18)],
        7:  [(1, 15), (9, 19)],
        8:  [(1, 16), (8, 20)],               # body
        9:  [(1, 16), (8, 21)],
        10: [(1, 16), (8, 21)],
        11: [(1, 16), (8, 21)],
        12: [(1, 16), (8, 20)],
        13: [(2, 15), (9, 19)],
        14: [(2, 14), (10, 18)],
        15: [(3, 13), (11, 17)],
        16: [(4, 12), (12, 15)],
        17: [(5, 7), (9, 11), (13, 14)],      # legs
        18: [(4, 4), (6, 6), (8, 8), (12, 12), (14, 14)],
    },
    "fills": [
        # dark purple crown swept over the head
        ("runs", [(2, 6, 10), (3, 4, 12), (4, 3, 12), (5, 2, 10),
                  (6, 2, 8)], "V"),
        # pale eyes on the crown edge
        ("put", 6, 4, "W"),
        # red fangs
        ("runs", [(7, 1, 3), (8, 1, 2)], "O"),
        # orange legs splayed wide
        ("runs", [(4, 12, 16), (5, 11, 17), (6, 10, 18)], "O"),
        ("runs", [(16, 12, 15), (17, 9, 11), (17, 13, 14)], "O"),
        # body shading + segments
        ("runs", [(10, 8, 16), (11, 8, 16), (12, 8, 15)], "D"),
        ("runs", [(9, 12, 16), (10, 12, 16)], "D"),
        # legs bottom
        ("put", 18, 4, "O"),
        ("put", 18, 6, "O"),
        ("put", 18, 8, "O"),
        ("put", 18, 12, "O"),
        ("put", 18, 14, "O"),
    ],
}
