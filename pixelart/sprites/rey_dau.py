"""Rey Dau, flying wyvern. The thunder rail: a storm-yellow wyvern with
thin black rail horns rising from the head, a white toothy grin, a black
wing-gun wing folded over the back with coil lines, and a slim tail with
a black lightning tip."""

CONFIG = {
    "name": "rey-dau",
    "size": (36, 24),
    "compare_to": "../icons/mhwilds/rey-dau.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "Y": (222, 180, 62, 255),   # storm yellow body
        "D": (176, 138, 44, 255),   # darker yellow
        "N": (44, 44, 52, 255),     # black horns / wing guns
        "W": (246, 242, 230, 255),
    },
    "base": "Y",
    "spans": {
        2:  [(4, 4), (8, 8)],                 # rail horn tips
        3:  [(3, 5), (7, 9), (16, 16)],       # horns + wing spike
        4:  [(2, 6), (6, 10), (13, 25)],      # horns + wing top
        5:  [(1, 7), (5, 11), (12, 27)],      # head + wing + tail
        6:  [(1, 27)],                        # head + wing + body merged
        7:  [(0, 27)],
        8:  [(0, 26)],
        9:  [(1, 25)],
        10: [(1, 24)],
        11: [(2, 23)],
        12: [(3, 22)],
        13: [(5, 20)],
        14: [(7, 12), (16, 19)],              # legs
        15: [(7, 12), (16, 19)],
        16: [(7, 7), (9, 9), (11, 11), (16, 16), (18, 18)],
    },
    "fills": [
        # thin black rail horns
        ("runs", [(2, 4, 4), (3, 3, 5), (4, 2, 6)], "N"),
        ("runs", [(2, 8, 8), (3, 7, 9), (4, 6, 10)], "N"),
        # dark eye + white toothy grin
        ("put", 5, 3, "N"),
        ("runs", [(6, 1, 4)], "K"),
        ("put", 6, 1, "W"),
        ("put", 6, 3, "W"),
        # black wing-gun wing with coil lines
        ("runs", [(4, 13, 21), (5, 12, 20), (6, 12, 20)], "N"),
        ("runs", [(5, 14, 14), (5, 18, 18), (6, 13, 13), (6, 16, 16),
                  (6, 19, 19)], "D", "N"),
        # wing spike + lightning tail tip black
        ("put", 3, 16, "N"),
        ("runs", [(4, 24, 25), (5, 25, 27), (6, 25, 27)], "N"),
        # body shade along the bottom
        ("runs", [(11, 3, 22), (12, 4, 21), (13, 6, 19)], "D"),
        # claws
        ("put", 16, 7, "W"),
        ("put", 16, 9, "W"),
        ("put", 16, 11, "W"),
        ("put", 16, 16, "W"),
        ("put", 16, 18, "W"),
    ],
}
