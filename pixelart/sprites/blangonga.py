"""Blangonga, fanged beast. The whisker chieftain: a white-furred baboon
quadruped with a purple face plate, a huge red-orange mustache of
whiskers bristling sideways, yellow tusks under the jaw, and a long pale
tail. The baboon archetype blango derives from."""

CONFIG = {
    "name": "blangonga",
    "size": (32, 24),
    "compare_to": "../icons/mhwilds/blangonga.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (222, 218, 206, 255),  # white fur
        "D": (184, 180, 168, 255),  # fur shade
        "V": (108, 88, 128, 255),   # purple face
        "R": (212, 96, 52, 255),    # red-orange whiskers
        "Y": (232, 196, 90, 255),   # yellow tusks / mane
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        3:  [(5, 8), (12, 13)],               # mane tufts
        4:  [(3, 10), (11, 15)],
        5:  [(2, 11), (10, 17)],
        6:  [(1, 12), (9, 19)],
        7:  [(1, 13), (8, 21)],               # head + back
        8:  [(0, 13), (7, 22)],
        9:  [(0, 14), (7, 23)],
        10: [(0, 15), (6, 24)],
        11: [(0, 15), (6, 25)],
        12: [(0, 15), (7, 26)],               # whisker tips
        13: [(1, 14), (8, 26)],
        14: [(1, 14), (9, 26)],
        15: [(2, 13), (10, 25)],
        16: [(3, 12), (12, 24)],
        17: [(5, 11), (14, 22)],
        18: [(5, 10), (15, 21)],
        19: [(5, 9), (16, 20)],
        20: [(5, 8), (17, 19)],               # legs + tail tip
        21: [(5, 7), (9, 9), (17, 17), (19, 19)],
    },
    "fills": [
        # purple face plate
        ("runs", [(5, 3, 10), (6, 2, 11), (7, 2, 11), (8, 2, 12),
                  (9, 2, 12)], "V"),
        # pale eyes
        ("put", 7, 4, "W"),
        ("put", 7, 9, "W"),
        # huge red-orange mustache whiskers bristling sideways
        ("runs", [(9, 0, 1), (10, 0, 1), (11, 0, 0), (12, 0, 0),
                  (9, 14, 15), (10, 15, 15), (11, 16, 15)], "R"),
        ("runs", [(10, 0, 14), (11, 0, 15), (12, 1, 15)], "R", "V"),
        ("runs", [(10, 16, 24), (11, 17, 25), (12, 16, 26)], "R", "F"),
        # yellow tusks under the jaw
        ("runs", [(13, 3, 4), (13, 9, 10)], "Y"),
        # gold mane tufts
        ("runs", [(3, 5, 8), (3, 12, 13), (4, 11, 15)], "Y"),
        # fur shade along the belly
        ("runs", [(14, 2, 12), (15, 3, 11), (16, 4, 10)], "D"),
        # tail pale
        ("runs", [(17, 20, 22), (18, 19, 21), (19, 18, 20),
                  (20, 17, 19)], "D"),
        # claws
        ("put", 21, 5, "W"),
        ("put", 21, 9, "W"),
        ("put", 21, 17, "W"),
        ("put", 21, 19, "W"),
    ],
}
