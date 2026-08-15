"""Gigginox, flying wyvern. The cave stalker: a flattened red-purple body
with a pale head crest, a wide toothy maw, wing-claws, and a twin-headed
tail. The gigginox archetype its variants derive from."""

CONFIG = {
    "name": "gigginox",
    "size": (32, 24),
    "compare_to": "../icons/mh3u/gigginox.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (148, 84, 96, 255),    # red-purple body
        "D": (112, 60, 74, 255),    # darker purple
        "C": (216, 198, 176, 255),  # pale head crest / belly
        "W": (246, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        4:  [(3, 9)],                         # head top
        5:  [(2, 11), (12, 13)],
        6:  [(1, 12), (11, 15)],
        7:  [(1, 13), (10, 17)],              # head + wing arm
        8:  [(1, 13), (9, 19)],
        9:  [(0, 13), (9, 20)],               # maw + body
        10: [(0, 13), (9, 21)],
        11: [(0, 13), (9, 21)],
        12: [(0, 13), (9, 21)],
        13: [(1, 13), (9, 21)],               # tail head zone
        14: [(1, 13), (9, 22)],
        15: [(2, 13), (10, 22)],
        16: [(2, 13), (11, 22)],
        17: [(3, 12), (12, 22)],
        18: [(4, 12), (14, 21)],
        19: [(5, 11), (16, 20)],
        20: [(6, 11), (18, 19)],
        21: [(6, 9), (18, 18)],
    },
    "fills": [
        # pale head crest swept back
        ("runs", [(4, 3, 9), (5, 2, 10), (6, 1, 10), (7, 1, 8)], "C"),
        # pale twin tail heads
        ("runs", [(13, 18, 21), (14, 18, 22), (15, 17, 22)], "C"),
        # dark eye dots on the tail heads
        ("put", 14, 19, "K"),
        ("put", 14, 21, "K"),
        # wide toothy maw
        ("runs", [(9, 0, 8)], "D"),
        ("put", 9, 1, "W"),
        ("put", 9, 4, "W"),
        ("put", 9, 7, "W"),
        # body shade along the bottom
        ("runs", [(15, 3, 12), (16, 3, 12), (17, 4, 11)], "D"),
        # wing-claw claws
        ("put", 5, 13, "D"),
        ("put", 6, 14, "D"),
        ("put", 7, 16, "D"),
    ],
}
