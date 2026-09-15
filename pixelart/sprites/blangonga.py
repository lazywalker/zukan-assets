"""Blangonga, fanged beast. The whisker chieftain, drawn in the face-front
of its icon: an orange-red crown mane over a broad white face, a purple
muzzle plate, the huge red-orange mustache bristling sideways, yellow
tusks under the jaw, and a white-furred body below."""

CONFIG = {
    "name": "blangonga",
    "size": (32, 24),
    "compare_to": "../icons/mhwilds/blangonga.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (246, 242, 232, 255),   # white fur
        "C": (214, 204, 194, 255),   # fur shade
        "R": (210, 85, 50, 255),     # orange-red mane / mustache
        "D": (160, 55, 35, 255),     # dark red shade
        "P": (150, 125, 140, 255),   # purple-grey muzzle
        "Y": (235, 200, 80, 255),    # tusk yellow
    },
    "base": "W",
    "spans": {
        1:  [(11, 12), (19, 20)],                # mane tips
        2:  [(9, 14), (17, 22)],
        3:  [(7, 15), (16, 24)],
        4:  [(6, 25)],
        5:  [(5, 26)],
        6:  [(4, 27)],                           # face top
        7:  [(4, 27)],
        8:  [(4, 27)],
        9:  [(4, 27)],
        10: [(4, 27)],
        11: [(1, 9), (10, 21), (22, 30)],        # mustache + muzzle
        12: [(1, 8), (10, 21), (23, 30)],
        13: [(2, 8), (10, 21), (23, 29)],
        14: [(3, 28)],                           # jaw
        15: [(5, 26)],                           # body
        16: [(5, 26)],
        17: [(6, 25)],
        18: [(6, 25)],
        19: [(8, 11), (13, 18), (20, 23)],       # legs
        20: [(8, 11), (13, 18), (20, 23)],
    },
    "fills": [
        # orange-red crown mane with dark spikes
        ("runs", [(1, 11, 12), (1, 19, 20), (2, 9, 10), (2, 13, 14),
                  (2, 17, 18), (2, 21, 22), (3, 7, 9), (3, 14, 15),
                  (3, 20, 21), (3, 23, 24), (4, 6, 8), (4, 12, 13),
                  (4, 18, 19), (4, 23, 25), (5, 5, 7), (5, 13, 14),
                  (5, 17, 18), (5, 24, 26)], "R"),
        ("runs", [(1, 11, 12), (1, 19, 20), (2, 13, 14), (2, 21, 22),
                  (3, 14, 15), (4, 12, 13), (4, 23, 25), (5, 24, 26)],
         "D", "R"),
        # dark angry brows over small eyes
        ("runs", [(7, 9, 12), (7, 19, 22)], "C", "W"),
        ("put", 8, 10, "K"),
        ("put", 8, 21, "K"),
        # purple muzzle plate with dark nose dots
        ("runs", [(9, 10, 21), (10, 10, 21)], "P"),
        ("put", 10, 13, "K"),
        ("put", 10, 18, "K"),
        # huge red-orange mustache bristling sideways
        ("runs", [(11, 1, 9), (11, 22, 30), (12, 1, 8), (12, 23, 30),
                  (13, 2, 8), (13, 23, 29)], "R"),
        ("runs", [(11, 1, 3), (12, 1, 2), (11, 28, 30), (12, 29, 30),
                  (13, 2, 3), (13, 28, 29)], "D", "R"),
        ("runs", [(11, 10, 21), (12, 10, 21), (13, 10, 21)], "P"),
        # yellow tusks under the jaw
        ("runs", [(14, 12, 13), (14, 18, 19), (15, 12, 13), (15, 18, 19)],
         "Y", "W"),
        # white body with pale shading
        ("runs", [(15, 5, 9), (15, 22, 26), (16, 5, 8), (16, 23, 26),
                  (17, 6, 9), (17, 22, 25), (18, 6, 9), (18, 22, 25)],
         "C", "W"),
        ("runs", [(16, 12, 19), (17, 12, 19)], "C", "W"),
        # dark legs with pale claws
        ("runs", [(19, 8, 11), (19, 20, 23), (20, 8, 11), (20, 20, 23),
                  (19, 13, 18), (20, 13, 18)], "C", "W"),
        ("put", 20, 9, "K"),
        ("put", 20, 22, "K"),
    ],
}
