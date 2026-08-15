"""Xeno'jiiva, elder dragon. The otherworldly newborn: pale blue-white
horizontal body, wing arms spread ABOVE the back with a glowing cyan edge,
two antennae, big pale eyes, four short legs hanging from the belly, wide
tail fin at the right."""

CONFIG = {
    "name": "xenojiiva",
    "size": (36, 24),
    "compare_to": "../icons/mhw/xenojiiva.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (205, 218, 238, 255),  # pale blue-white body
        "D": (160, 175, 205, 255),  # darker shade
        "C": (160, 225, 235, 255),  # glowing cyan accents
        "W": (246, 250, 250, 255),  # eye
    },
    "base": "P",
    "spans": {
        2:  [(3, 4), (7, 8)],                 # antennae
        3:  [(2, 5), (6, 9)],
        4:  [(1, 6), (14, 24)],               # head + wing top edge
        5:  [(1, 7), (13, 26)],
        6:  [(1, 8), (12, 27)],
        7:  [(1, 9), (11, 28)],
        8:  [(1, 10), (11, 28)],
        9:  [(1, 11), (11, 28)],
        10: [(2, 12), (10, 29)],
        11: [(3, 13), (9, 30)],
        12: [(4, 14), (9, 31)],
        13: [(5, 15), (9, 31)],
        14: [(5, 16), (9, 30)],
        15: [(5, 17), (9, 29)],               # belly bottom edge
        16: [(10, 11), (14, 15), (19, 20), (23, 24)],   # four legs
        17: [(10, 11), (14, 15), (19, 20), (23, 24)],
        18: [(11, 11), (15, 15), (20, 20), (24, 24)],   # feet
        19: [(11, 11), (15, 15), (20, 20), (24, 24)],
        20: [(12, 12), (15, 15), (21, 21), (23, 23)],   # claw tips
    },
    "fills": [
        # antennae, cyan tips
        ("runs", [(2, 3, 3), (2, 7, 7), (3, 3, 3)], "C"),
        # big pale eyes
        ("put", 6, 2, "W"),
        ("put", 6, 5, "W"),
        # wing lower band, darker, with glow edge
        ("runs", [(7, 15, 26), (8, 16, 27), (9, 16, 27)], "D"),
        ("runs", [(8, 27, 27), (9, 27, 28), (10, 29, 29)], "C"),
        # neck shade
        ("runs", [(5, 12, 13), (6, 12, 13), (7, 13, 14)], "D"),
        # legs, darker
        ("runs", [(16, 10, 11), (17, 10, 11), (16, 14, 15), (17, 14, 15),
                  (16, 19, 20), (17, 19, 20), (16, 23, 24), (17, 23, 24)],
         "D"),
        # tail fin glow
        ("runs", [(13, 29, 31), (14, 30, 30)], "C"),
    ],
}
