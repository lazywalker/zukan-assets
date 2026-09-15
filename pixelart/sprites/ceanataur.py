"""Ceanataur, carapaceon. The blue axe-claw crab, drawn in the front pose
of its icon: two bright blue pincer blades raised in a high V with pale
inner rims, a grey olive shell dome with a pale crown spike between them,
yellow eyes over a dark face band, and three pointed leg pairs below."""

CONFIG = {
    "name": "ceanataur",
    "size": (32, 24),
    "compare_to": "../icons/mhfu/ceanataur.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (184, 176, 148, 255),   # olive grey shell
        "D": (138, 126, 104, 255),   # dark shell / legs
        "P": (38, 134, 242, 255),    # blue pincer blade
        "Q": (18, 94, 206, 255),     # dark blue blade edge
        "C": (222, 218, 192, 255),   # pale rim
        "Y": (246, 210, 64, 255),    # eye yellow
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(6, 7), (24, 25)],                  # pincer tips
        2:  [(5, 8), (23, 26)],
        3:  [(4, 9), (22, 27)],
        4:  [(3, 10), (21, 28)],
        5:  [(3, 11), (20, 28)],
        6:  [(3, 11), (20, 28)],
        7:  [(3, 10), (15, 16), (21, 28)],       # blade base + crown spike
        8:  [(5, 8), (13, 18), (23, 26)],        # arms + dome top
        9:  [(5, 8), (12, 19), (23, 26)],
        10: [(5, 8), (11, 20), (23, 26)],
        11: [(5, 8), (10, 21), (23, 26)],
        12: [(5, 8), (9, 22), (23, 26)],
        13: [(5, 7), (9, 22), (24, 26)],
        14: [(4, 27)],                           # body
        15: [(4, 27)],
        16: [(4, 27)],
        17: [(4, 27)],
        18: [(5, 8), (10, 12), (14, 17), (19, 21), (23, 26)],   # legs
        19: [(5, 8), (10, 12), (14, 17), (19, 21), (23, 26)],
        20: [(5, 7), (10, 11), (15, 16), (20, 21), (24, 26)],
        21: [(5, 5), (10, 10), (15, 16), (21, 21), (26, 26)],   # tips
    },
    "fills": [
        # raised pincer blades and arms, bright blue
        ("runs", [(1, 6, 7), (2, 5, 8), (3, 4, 9), (4, 3, 10), (5, 2, 11),
                  (6, 2, 11), (7, 3, 10), (1, 24, 25), (2, 23, 26),
                  (3, 22, 27), (4, 21, 28), (5, 20, 29), (6, 20, 29),
                  (7, 21, 28), (8, 5, 8), (9, 5, 8), (10, 5, 8),
                  (11, 5, 8), (12, 5, 8), (13, 5, 7), (8, 23, 26),
                  (9, 23, 26), (10, 23, 26), (11, 23, 26), (12, 23, 26),
                  (13, 24, 26)], "P"),
        # pale inner rim along each blade
        ("runs", [(2, 7, 8), (3, 8, 9), (4, 9, 10), (5, 10, 11),
                  (6, 10, 11), (7, 9, 10), (2, 23, 24), (3, 22, 23),
                  (4, 21, 22), (5, 20, 21), (6, 20, 21), (7, 21, 22)],
         "C", "P"),
        # yellow diagonal band across each blade
        ("runs", [(3, 6, 7), (4, 7, 8), (5, 8, 9), (6, 8, 9), (3, 24, 25),
                  (4, 23, 24), (5, 22, 23), (6, 22, 23)], "Y", "P"),
        # dark outer edge on each blade
        ("runs", [(4, 3, 4), (5, 3, 4), (6, 3, 4), (4, 27, 28),
                  (5, 27, 28), (6, 27, 28)], "Q", "P"),
        # dark lower arms
        ("runs", [(12, 5, 8), (13, 5, 7), (12, 23, 26), (13, 24, 26)],
         "Q", "P"),
        # pale crown on the dome top
        ("runs", [(7, 15, 16), (8, 14, 17)], "C"),
        # dark spots across the upper dome
        ("runs", [(9, 12, 13), (9, 18, 19), (10, 15, 16)], "D"),
        # dark dome sides for roundness
        ("runs", [(11, 10, 11), (11, 20, 21), (12, 9, 10), (12, 21, 22),
                  (13, 9, 10), (13, 21, 22)], "D"),
        # dark face band with angry brows
        ("runs", [(12, 11, 20), (13, 12, 19)], "D"),
        ("runs", [(11, 11, 12), (11, 19, 20)], "D"),
        # glaring yellow eyes with dark pupils
        ("runs", [(11, 13, 14), (11, 17, 18)], "Y"),
        ("put", 12, 13, "K"),
        ("put", 12, 18, "K"),
        # pale mandibles on the mouth band
        ("put", 13, 14, "W"),
        ("put", 13, 17, "W"),
        # pale rim along the body bottom edge
        ("runs", [(16, 5, 26), (17, 6, 25)], "C"),
        # dark body corners for roundness
        ("runs", [(14, 4, 6), (14, 25, 27), (15, 4, 5), (15, 26, 27)], "D"),
        # legs dark with pale tips
        ("runs", [(18, 5, 8), (18, 10, 12), (18, 14, 17), (18, 19, 21),
                  (18, 23, 26), (19, 5, 8), (19, 10, 12), (19, 14, 17),
                  (19, 19, 21), (19, 23, 26), (20, 5, 7), (20, 10, 11),
                  (20, 15, 16), (20, 20, 21), (20, 24, 26), (21, 5, 5),
                  (21, 10, 10), (21, 15, 16), (21, 21, 21), (21, 26, 26)],
         "D"),
        ("put", 21, 5, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 21, "W"),
        ("put", 21, 26, "W"),
    ],
}
