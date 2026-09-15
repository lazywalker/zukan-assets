"""Kushala Daora, elder dragon. The storm wolf, drawn head-on under its
dark horn hood: a wide curved crest over a grey face with pale glowing
eyes, wind swirls drifting off both sides, and a fanged snout."""

CONFIG = {
    "name": "kushala-daora",
    "size": (32, 24),
    "compare_to": "../icons/mh4u/kushala-daora.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (142, 150, 158, 255),
        "D": (90, 98, 110, 255),
        "C": (205, 214, 222, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        1:  [(5, 10), (21, 26)],              # horn hood
        2:  [(3, 12), (19, 28)],
        3:  [(2, 14), (17, 29)],
        4:  [(1, 15), (16, 30)],
        5:  [(1, 30)],                        # hood brim
        6:  [(0, 0), (7, 24), (31, 31)],      # wind swirls + face
        7:  [(6, 25)],
        8:  [(5, 26)],
        9:  [(0, 1), (4, 27), (30, 31)],
        10: [(4, 27)],
        11: [(5, 26)],
        12: [(1, 2), (6, 25), (29, 30)],
        13: [(7, 24)],
        14: [(5, 26)],
        15: [(5, 26)],
        16: [(6, 25)],
        17: [(7, 24)],
        18: [(6, 11), (13, 18), (20, 25)],    # forepaws
        19: [(5, 10), (14, 17), (21, 26)],
        20: [(4, 9), (15, 16), (22, 27)],
        21: [(4, 4), (6, 6), (8, 8), (15, 15), (17, 17), (23, 23),
             (25, 25), (27, 27)],
    },
    "fills": [
        # dark horn hood over the head
        ("runs", [(1, 5, 10), (1, 21, 26), (2, 3, 12), (2, 19, 28),
                  (3, 2, 14), (3, 17, 29), (4, 1, 15), (4, 16, 30),
                  (5, 1, 30)], "D"),
        # scale glints on the hood
        ("runs", [(2, 6, 8), (2, 23, 25), (3, 10, 12), (3, 19, 21),
                  (4, 4, 6), (4, 25, 27)], "C"),
        # pale glowing eyes under the hood brim
        ("runs", [(7, 10, 11), (7, 20, 21)], "C"),
        ("put", 7, 11, "K"),
        ("put", 7, 20, "K"),
        # nostrils on the snout
        ("put", 10, 13, "K"),
        ("put", 10, 18, "K"),
        # jaw line with small fangs
        ("runs", [(12, 7, 24)], "D"),
        ("put", 12, 8, "W"),
        ("put", 12, 23, "W"),
        ("put", 13, 8, "W"),
        ("put", 13, 23, "W"),
        # body shade and forepaw claws
        ("runs", [(14, 5, 8), (15, 4, 6), (15, 24, 26), (16, 5, 7),
                  (16, 24, 26)], "D"),
        ("runs", [(21, 4, 4), (21, 6, 6), (21, 8, 8), (21, 15, 15),
                  (21, 17, 17), (21, 23, 23), (21, 25, 25), (21, 27, 27)],
         "W"),
    ],
}
