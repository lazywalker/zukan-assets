"""Nu Udra, cephalopod. The fire octopus: a round dark-olive mantle with
a crown of yellow flame horns and an eye, its tentacles fanning down and
away to the right in purple and teal sucker stripes."""

CONFIG = {
    "name": "nu-udra",
    "size": (34, 24),
    "compare_to": "../icons/mhwilds/nu-udra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (96, 92, 78, 255),     # dark olive mantle
        "D": (70, 66, 56, 255),     # darker shade
        "Y": (222, 198, 70, 255),   # yellow flame horns
        "P": (156, 74, 122, 255),   # purple arm stripes
        "T": (86, 158, 128, 255),   # teal arm stripes
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        2:  [(5, 5), (9, 9), (13, 13)],       # flame horn tips
        3:  [(4, 6), (8, 10), (12, 14)],
        4:  [(3, 15)],                        # round mantle
        5:  [(2, 17)],
        6:  [(1, 18)],
        7:  [(1, 18)],
        8:  [(2, 17)],
        9:  [(3, 16), (16, 19)],              # tentacles fan out
        10: [(3, 14), (15, 22)],
        11: [(4, 13), (14, 24)],
        12: [(5, 12), (13, 26)],
        13: [(6, 10), (12, 27)],
        14: [(7, 9), (11, 28)],
        15: [(8, 8), (10, 28)],
    },
    "fills": [
        # yellow flame horns with white tips
        ("runs", [(2, 5, 5), (2, 9, 9), (2, 13, 13), (3, 4, 6),
                  (3, 8, 10), (3, 12, 14)], "Y"),
        ("put", 2, 5, "W"),
        ("put", 2, 13, "W"),
        # eye on the mantle
        ("put", 5, 4, "W"),
        ("put", 5, 5, "K"),
        # suckered arms: purple and teal stripe bands
        ("runs", [(10, 16, 21), (11, 15, 22), (12, 14, 23)], "P", "O"),
        ("runs", [(12, 24, 25), (13, 23, 26), (14, 22, 27)], "T", "O"),
        ("runs", [(13, 12, 13), (14, 11, 12)], "P", "O"),
        # arm undersides darker
        ("runs", [(14, 11, 28), (15, 10, 28)], "D"),
        # mantle shade
        ("runs", [(6, 14, 18), (7, 14, 18), (8, 13, 17)], "D"),
    ],
}
