"""Daimyo Hermitaur, carapaceon. The shield crab, drawn in the front pose
of its icon: two dark red pincer claws raised in a high V with white
bands and a pincer gap opening through the inner edge, a gold skull
shield between them, a red face with pale eyes under the shield, and
three pointed leg pairs."""

CONFIG = {
    "name": "daimyo-hermitaur",
    "size": (38, 24),
    "compare_to": "../icons/mhst2/daimyo-hermitaur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (214, 54, 40, 255),     # red shell
        "D": (160, 36, 32, 255),     # dark red claws / legs
        "C": (246, 242, 232, 255),   # pale bands / eyes / tips
        "G": (198, 164, 54, 255),    # gold skull shield
        "E": (152, 120, 34, 255),    # dark gold relief
        "Y": (246, 244, 150, 255),   # pale belly rim
    },
    "base": "R",
    "spans": {
        1:  [(5, 6), (31, 32)],                  # claw tips
        2:  [(4, 7), (30, 33)],
        3:  [(3, 8), (29, 34)],
        4:  [(2, 9), (28, 35)],
        5:  [(2, 10), (16, 21)],
        6:  [(2, 10), (14, 23)],                 # claw + dome top
        7:  [(3, 7), (13, 24), (30, 34)],        # pincer gap opens right
        8:  [(3, 10), (13, 24), (27, 34)],
        9:  [(4, 10), (12, 25), (27, 33)],
        10: [(5, 10), (12, 25), (27, 32)],       # arm + dome base
        11: [(5, 32)],                           # fused body top
        12: [(5, 32)],
        13: [(4, 33)],
        14: [(4, 33)],
        15: [(4, 33)],
        16: [(5, 32)],
        17: [(5, 9), (11, 13), (15, 22)],        # legs
        18: [(5, 9), (11, 13), (15, 22)],
        19: [(5, 8), (11, 12), (16, 21)],
        20: [(5, 8), (11, 12), (17, 20)],
        21: [(5, 5), (11, 11), (18, 19), (26, 26), (32, 32)],   # tips
    },
    "fills": [
        # dark red claws and arms
        ("runs", [(1, 5, 6), (2, 4, 7), (3, 3, 8), (4, 2, 9), (5, 2, 10),
                  (6, 2, 10), (7, 3, 7), (8, 3, 10), (9, 4, 10),
                  (10, 5, 10), (1, 31, 32), (2, 30, 33), (3, 29, 34),
                  (4, 28, 35), (5, 27, 35), (6, 27, 35), (7, 30, 34),
                  (8, 27, 34), (9, 27, 33), (10, 27, 32)], "D"),
        # gold skull shield
        ("runs", [(5, 16, 21), (6, 14, 23), (7, 13, 24), (8, 13, 24),
                  (9, 12, 25), (10, 12, 25)], "G"),
        # dark skull relief on the shield
        ("runs", [(7, 16, 21), (8, 17, 20), (9, 18, 19), (6, 17, 18),
                  (6, 19, 20)], "E", "G"),
        # white bands across each claw
        ("runs", [(4, 4, 7), (5, 3, 9), (4, 30, 33), (5, 28, 34)],
         "C", "D"),
        # pale claw tips
        ("runs", [(1, 5, 6), (1, 31, 32)], "C", "D"),
        # pale eyes with dark pupils on the red face
        ("runs", [(12, 14, 16), (12, 21, 23)], "C"),
        ("put", 13, 15, "K"),
        ("put", 13, 22, "K"),
        # dark mouth band with pale mandibles
        ("runs", [(13, 17, 20)], "D"),
        ("put", 13, 17, "C"),
        ("put", 13, 20, "C"),
        # pale belly rim along the body bottom edge
        ("runs", [(15, 6, 31), (16, 7, 30)], "Y"),
        # legs dark with pale tips
        ("runs", [(17, 5, 9), (17, 11, 13), (17, 15, 22), (18, 5, 9),
                  (18, 11, 13), (18, 15, 22), (19, 5, 8), (19, 11, 12),
                  (19, 16, 21), (20, 5, 8), (20, 11, 12), (20, 17, 20),
                  (21, 5, 5), (21, 11, 11), (21, 18, 19)], "D"),
        ("put", 21, 5, "C"),
        ("put", 21, 11, "C"),
        ("put", 21, 18, "C"),
        ("put", 21, 19, "C"),
        ("put", 21, 26, "C"),
        ("put", 21, 32, "C"),
    ],
}
