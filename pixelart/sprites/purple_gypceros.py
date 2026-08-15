"""Purple Gypceros, gypceros subspecies. The one deliberate front-pose
sprite in the set (user-reviewed 2026-09; all other monsters stay side
view): oversized cream head with a gaping toothy mouth opening through
the left silhouette edge, red-brown crest comb behind the head, symmetric
spread wings with orange membrane, big banded cream belly, green poison
sac at the chest, orange ringed tail curling at the bottom-right."""

CONFIG = {
    "name": "purple-gypceros",
    "size": (32, 24),
    "compare_to": "../icons/mh4u/purple-gypceros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (115, 98, 152, 255),    # violet-blue body
        "C": (218, 192, 152, 255),   # cream head and belly
        "S": (150, 125, 90, 255),    # tan: spots, belly bands, rings
        "H": (150, 65, 50, 255),     # red-brown crest comb
        "O": (205, 125, 60, 255),    # orange wing membrane and tail
        "G": (150, 190, 90, 255),    # green poison sac
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        0:  [(16, 22)],                        # crest top
        1:  [(15, 24)],
        2:  [(6, 13), (15, 24)],
        3:  [(3, 14), (16, 24)],
        4:  [(2, 15), (17, 24)],
        5:  [(2, 16), (18, 23)],
        6:  [(0, 16), (19, 22), (29, 31)],
        7:  [(3, 4), (8, 9), (12, 16), (27, 31)],   # fangs + hinge + wing
        8:  [(3, 4), (8, 9), (12, 16), (26, 31)],
        9:  [(5, 6), (12, 16), (25, 31)],      # lower tusk + hinge + wing
        10: [(1, 20), (24, 31)],               # lower jaw + neck
        11: [(0, 2), (4, 20), (23, 30)],       # wing root + jaw bottom
        12: [(2, 22), (23, 30)],
        13: [(3, 9), (8, 23), (23, 29)],
        14: [(3, 4), (6, 9), (8, 25), (27, 28)],
        15: [(4, 5), (7, 8), (9, 24), (26, 27)],
        16: [(5, 8), (9, 22), (26, 30)],
        17: [(10, 21), (26, 30)],
        18: [(10, 21), (25, 29)],
        19: [(11, 20), (24, 28)],
        20: [(11, 20), (23, 27)],
        21: [(11, 12), (15, 15), (18, 19)],    # toes
    },
    "fills": [
        # red-brown crest comb, separated from the head by a 1px channel
        ("runs", [(0, 16, 22), (1, 15, 24), (2, 15, 24), (3, 16, 24),
                  (4, 17, 24), (5, 18, 23), (6, 19, 22), (7, 19, 22)], "H"),
        ("runs", [(1, 19, 19), (2, 19, 19), (3, 19, 19), (4, 19, 19)],
         "K", "H"),
        ("runs", [(2, 21, 21), (3, 21, 21), (4, 21, 21)], "K", "H"),
        # orange wing membranes (left wing starts below the jaw)
        ("runs", [(11, 0, 2), (12, 2, 8), (13, 3, 7), (14, 3, 4),
                  (14, 6, 9), (15, 4, 5), (15, 7, 8), (16, 5, 8)], "O"),
        ("runs", [(6, 29, 31), (7, 27, 31), (8, 26, 31), (9, 25, 31),
                  (10, 24, 31), (11, 23, 30), (12, 23, 30), (13, 23, 29),
                  (14, 22, 25), (14, 27, 28), (15, 23, 24), (15, 26, 27)],
         "O"),
        # thin violet rim along the outer wing edges
        ("runs", [(11, 0, 0), (12, 2, 2), (13, 3, 3), (14, 3, 3)],
         "B", "O"),
        ("runs", [(6, 30, 31), (7, 30, 31), (8, 30, 31), (9, 30, 31),
                  (10, 30, 31), (11, 30, 30), (12, 30, 30), (13, 29, 29),
                  (14, 27, 27)], "B", "O"),
        # wing claw tips
        ("put", 11, 0, "W"),
        ("put", 6, 31, "W"),
        # cream head: flat angular upper jaw, gaping mouth, chunky jaw
        ("runs", [(2, 6, 13), (3, 3, 14), (4, 2, 15), (5, 2, 16),
                  (6, 0, 16), (7, 12, 16), (8, 12, 16), (9, 12, 16),
                  (10, 1, 16), (11, 4, 13)], "C"),
        ("runs", [(3, 6, 8), (4, 4, 5), (5, 5, 7)], "S"),
        # angry eye: brow over light+pupil
        ("put", 3, 11, "K"),
        ("put", 4, 11, "W"),
        ("put", 4, 12, "K"),
        # fang blocks attached to the jaws
        ("runs", [(7, 3, 4), (8, 3, 4), (7, 8, 9), (8, 8, 9)], "W"),
        ("runs", [(9, 5, 6)], "W"),
        # green poison sac where neck meets belly
        ("runs", [(11, 15, 18), (12, 15, 18)], "G"),
        # big banded cream belly
        ("runs", [(13, 9, 22), (14, 9, 22), (15, 10, 21), (16, 10, 21),
                  (17, 11, 20), (18, 11, 20), (19, 12, 19)], "C"),
        ("runs", [(15, 11, 20), (17, 12, 19)], "S", "C"),
        # orange ringed tail curl
        ("runs", [(16, 26, 30), (17, 26, 30), (18, 25, 29), (19, 24, 28),
                  (20, 23, 27)], "O"),
        ("runs", [(17, 29, 29), (18, 28, 28), (19, 27, 27), (20, 26, 26)],
         "S", "O"),
        # toes
        ("put", 21, 11, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 19, "W"),
    ],
}
