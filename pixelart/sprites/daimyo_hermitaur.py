"""Daimyo Hermitaur, carapaceon. The crab daimyo, side view: a big red
shell dome wearing a cream samurai-helm band with two tall crest spikes,
a cream face with glaring eyes at the front, a small far claw and a
huge near claw with an open pincer hanging down-forward, and four
pointed legs."""

CONFIG = {
    "name": "daimyo-hermitaur",
    "size": (38, 24),
    "compare_to": "../icons/mhst2/daimyo-hermitaur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (196, 66, 52, 255),     # red shell
        "D": (146, 42, 38, 255),     # dark red claws / legs
        "C": (228, 208, 172, 255),   # cream helm band / face / rim
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        0:  [(20, 21), (27, 28)],              # crest spike tips
        1:  [(19, 22), (26, 29)],
        2:  [(12, 24), (25, 30)],
        3:  [(11, 25)],
        4:  [(10, 26)],
        5:  [(10, 27)],
        6:  [(10, 27)],
        7:  [(10, 28)],
        8:  [(10, 28)],
        9:  [(10, 28)],
        10: [(10, 28)],
        11: [(10, 27)],
        12: [(0, 3), (4, 26)],                 # far claw + body band
        13: [(0, 3), (4, 26)],
        14: [(0, 2), (4, 25)],
        15: [(1, 9), (10, 24)],                # claw top + body bottom
        16: [(0, 10), (12, 14), (17, 19), (22, 24)],
        17: [(0, 10), (13, 13), (18, 18), (23, 23)],
        18: [(6, 10)],                         # open pincer slot cols 0-5
        19: [(6, 10)],
        20: [(1, 10)],                         # lower pincer
        21: [(2, 9)],
    },
    "fills": [
        # cream helm band wrapped over the dome top
        ("runs", [(2, 12, 24), (2, 25, 30), (3, 11, 25), (4, 10, 26)],
         "C"),
        # massive near claw, darker red with white pincer stripes
        ("runs", [(15, 1, 9), (16, 0, 10), (17, 0, 10), (18, 6, 10),
                  (19, 6, 10), (20, 1, 10), (21, 2, 9)], "D"),
        ("runs", [(15, 2, 8), (16, 1, 8), (18, 9, 9), (19, 9, 9)],
         "W", "D"),
        ("put", 21, 2, "W"),
        # small far claw
        ("runs", [(12, 0, 3), (13, 0, 3), (14, 0, 2)], "D"),
        ("put", 12, 0, "W"),
        # dark spots on the dome
        ("runs", [(6, 15, 16), (7, 20, 21), (8, 13, 14),
                  (9, 18, 19), (9, 23, 24), (10, 15, 16),
                  (11, 20, 21)], "D"),
        # cream rim along the shell bottom edge
        ("runs", [(11, 11, 27), (12, 10, 26), (13, 10, 26)], "C"),
        # cream face at the front, glaring eyes
        ("runs", [(12, 4, 9), (13, 4, 9), (14, 4, 9)], "C"),
        ("put", 13, 5, "K"),
        ("put", 13, 8, "K"),
        ("put", 14, 5, "K"),
        ("put", 14, 8, "K"),
        # pointed legs, dark with pale tips
        ("runs", [(16, 12, 14), (16, 17, 19), (16, 22, 24)], "D"),
        ("put", 17, 13, "W"),
        ("put", 17, 18, "W"),
        ("put", 17, 23, "W"),
    ],
}
