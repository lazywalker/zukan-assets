"""Shogun Ceanataur, carapaceon. The shogun blade crab, drawn in the
front pose of its icon: two huge steel blue blade pincers raised in a
high V with white cutting edges, a dark slate shell dome with a pale
horn cluster between them, yellow eyes on a dark face band, and three
pointed leg pairs under the wide body."""

CONFIG = {
    "name": "shogun-ceanataur",
    "size": (40, 24),
    "compare_to": "../icons/mhfu/shogun-ceanataur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (168, 162, 138, 255),   # grey shell
        "D": (116, 110, 94, 255),    # dark slate dome / legs
        "P": (38, 134, 242, 255),    # blue blade pincer
        "Q": (18, 94, 206, 255),     # dark blue blade edge
        "C": (222, 218, 192, 255),   # pale rim / cutting edge
        "Y": (246, 210, 64, 255),    # eye yellow
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(5, 6), (33, 34)],                  # blade tips
        2:  [(4, 7), (32, 35)],
        3:  [(3, 8), (31, 36)],
        4:  [(3, 9), (30, 36)],
        5:  [(2, 10), (29, 37)],
        6:  [(2, 10), (29, 37)],
        7:  [(2, 10), (29, 37)],                 # tall blade body
        8:  [(3, 10), (18, 21), (29, 36)],       # blade base + horn
        9:  [(4, 10), (17, 22), (29, 35)],
        10: [(5, 10), (14, 25), (29, 34)],       # arms + dome top
        11: [(5, 10), (13, 26), (29, 34)],
        12: [(5, 10), (13, 26), (29, 34)],
        13: [(6, 9), (11, 28), (30, 33)],
        14: [(6, 9), (11, 28), (30, 33)],
        15: [(3, 36)],                           # body
        16: [(3, 36)],
        17: [(3, 36)],
        18: [(4, 8), (10, 12), (14, 25), (27, 29), (31, 35)],   # legs
        19: [(4, 8), (10, 12), (14, 25), (27, 29), (31, 35)],
        20: [(4, 7), (10, 11), (16, 23), (28, 29), (32, 35)],
        21: [(4, 4), (10, 10), (18, 21), (29, 29), (35, 35)],   # tips
    },
    "fills": [
        # raised blade pincers and arms, bright blue
        ("runs", [(1, 5, 6), (2, 4, 7), (3, 3, 8), (4, 3, 9), (5, 2, 10),
                  (6, 2, 10), (7, 2, 10), (8, 3, 10), (9, 4, 10),
                  (10, 5, 10), (11, 5, 10), (12, 5, 10), (13, 6, 9),
                  (14, 6, 9), (1, 33, 34), (2, 32, 35), (3, 31, 36),
                  (4, 30, 36), (5, 29, 37), (6, 29, 37), (7, 29, 37),
                  (8, 29, 36), (9, 29, 35), (10, 29, 34), (11, 29, 34),
                  (12, 29, 34), (13, 30, 33), (14, 30, 33)], "P"),
        # white cutting edge along each blade inner rim
        ("runs", [(2, 6, 7), (3, 7, 8), (4, 8, 9), (5, 9, 10), (6, 9, 10),
                  (7, 9, 10), (8, 9, 10), (9, 9, 10), (2, 32, 33),
                  (3, 31, 32), (4, 30, 31), (5, 29, 30), (6, 29, 30),
                  (7, 29, 30), (8, 29, 30), (9, 29, 30)], "C", "P"),
        # dark outer edge on each blade
        ("runs", [(4, 3, 4), (5, 2, 3), (6, 2, 3), (7, 2, 3), (4, 35, 36),
                  (5, 36, 37), (6, 36, 37), (7, 36, 37)], "Q", "P"),
        # pale horn cluster over the dome
        ("runs", [(8, 18, 21), (9, 17, 22)], "C"),
        # dark dome with pale rim
        ("runs", [(10, 14, 25), (11, 13, 26), (12, 13, 26), (13, 11, 28),
                  (14, 11, 28)], "D"),
        ("runs", [(10, 15, 24), (11, 14, 25)], "B", "D"),
        # dark face band, glaring yellow eyes with dark pupils
        ("runs", [(13, 13, 26), (14, 13, 26)], "D"),
        ("runs", [(12, 16, 18), (12, 21, 23)], "Y", "D"),
        ("put", 13, 17, "K"),
        ("put", 13, 22, "K"),
        # pale mandibles on the mouth band
        ("put", 14, 18, "W"),
        ("put", 14, 21, "W"),
        # pale rim along the body bottom edge
        ("runs", [(16, 4, 35), (17, 5, 34)], "C"),
        # dark body corners for roundness
        ("runs", [(15, 3, 5), (15, 34, 36), (16, 3, 4), (16, 35, 36)], "D"),
        # legs dark with pale tips
        ("runs", [(18, 4, 8), (18, 10, 12), (18, 14, 25), (19, 4, 8),
                  (19, 10, 12), (19, 14, 25), (20, 4, 7), (20, 10, 11),
                  (20, 16, 23), (21, 4, 4), (21, 10, 10), (21, 18, 21)],
         "D"),
        ("put", 21, 4, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 29, "W"),
        ("put", 21, 35, "W"),
    ],
}
