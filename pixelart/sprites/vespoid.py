"""Vespoid, neopteron. The wasp: a red-brown body with yellow bands, two
wings swept back to the right, antennae, a stinger, and thin legs. The
wasp archetype the other small neopterons derive from."""

CONFIG = {
    "name": "vespoid",
    "size": (26, 24),
    "compare_to": "../icons/mhwilds/vespoid.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (168, 76, 58, 255),    # red-brown body
        "Y": (224, 176, 70, 255),   # yellow bands
        "W": (226, 226, 216, 255),  # pale wings
        "D": (124, 54, 42, 255),    # darker shade
        "w": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        3:  [(9, 10), (13, 13)],              # antennae
        4:  [(7, 12), (12, 13)],
        5:  [(6, 13), (13, 15)],              # head + wing tip
        6:  [(5, 14), (12, 17)],
        7:  [(4, 14), (11, 18)],              # thorax + wing
        8:  [(4, 14), (10, 19)],
        9:  [(3, 14), (10, 19)],              # abdomen
        10: [(3, 14), (10, 20)],
        11: [(3, 14), (11, 20)],
        12: [(4, 14), (12, 19)],
        13: [(4, 13), (13, 18)],              # stinger
        14: [(5, 13), (14, 16)],
        15: [(5, 12), (15, 15)],
        16: [(6, 12)],
        17: [(6, 8), (10, 12)],               # legs
        18: [(6, 7), (9, 9), (11, 11)],
    },
    "fills": [
        # antennae dark
        ("runs", [(3, 9, 10), (3, 13, 13)], "D"),
        # big compound eye
        ("put", 5, 7, "w"),
        ("put", 5, 8, "K"),
        # wings pale with vein lines
        ("runs", [(5, 13, 15), (6, 12, 17), (7, 11, 18), (8, 10, 19)],
         "W"),
        ("runs", [(6, 14, 14), (7, 14, 15), (8, 14, 16)], "D", "W"),
        # yellow bands on the abdomen
        ("runs", [(10, 3, 9), (13, 4, 13), (15, 5, 12)], "Y"),
        # stinger dark
        ("runs", [(14, 12, 13)], "D"),
        # legs
        ("runs", [(17, 6, 8), (17, 10, 12)], "D"),
        ("put", 18, 6, "D"),
        ("put", 18, 9, "D"),
        ("put", 18, 11, "D"),
    ],
}
