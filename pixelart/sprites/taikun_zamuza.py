"""Taikun Zamuza, carapaceon. The samurai flail: a blue-shelled crab with a
horned helmet crest, one giant spiked flail claw, and a hard underbelly."""

CONFIG = {
    "name": "taikun-zamuza",
    "size": (34, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (84, 112, 178, 255),   # blue shell
        "D": (56, 80, 138, 255),    # darker blue
        "C": (210, 190, 152, 255),  # tan underbelly
        "O": (232, 152, 58, 255),   # flail spikes
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        2:  [(2, 5), (8, 9)],                 # flail top + crest tip
        3:  [(1, 6), (7, 10), (12, 14)],
        4:  [(1, 7), (6, 11), (11, 16)],      # flail + crest + body
        5:  [(1, 8), (5, 12), (10, 18)],
        6:  [(1, 9), (5, 13), (9, 20)],
        7:  [(1, 9), (4, 14), (8, 22)],
        8:  [(0, 10), (4, 15), (7, 23)],      # flail + face + shell
        9:  [(0, 10), (4, 16), (7, 24)],
        10: [(0, 10), (4, 16), (7, 25)],
        11: [(0, 10), (4, 16), (7, 25)],
        12: [(1, 10), (4, 16), (7, 25)],
        13: [(1, 10), (4, 16), (7, 25)],
        14: [(1, 10), (4, 16), (8, 25)],
        15: [(1, 10), (4, 15), (9, 24)],
        16: [(2, 10), (5, 14), (11, 23)],
        17: [(2, 9), (6, 13), (13, 21)],      # legs
        18: [(2, 8), (7, 12), (14, 20)],
        19: [(3, 4), (6, 6), (8, 8), (14, 15), (17, 18)],
    },
    "fills": [
        # gold-tipped flail spikes
        ("runs", [(2, 2, 5), (3, 1, 6), (4, 1, 5)], "O"),
        ("put", 2, 3, "W"),
        # samurai crest horn on the head
        ("runs", [(2, 8, 9), (3, 7, 10), (4, 6, 9)], "D"),
        # pale eye
        ("put", 6, 6, "W"),
        # spiked flail ball
        ("runs", [(6, 1, 7), (7, 1, 8), (8, 1, 9)], "O", "B"),
        ("runs", [(7, 3, 3), (7, 5, 5), (8, 3, 3), (8, 6, 6)], "W", "O"),
        # tan underbelly along the bottom edge
        ("runs", [(14, 4, 15), (15, 4, 14), (16, 5, 13), (17, 6, 12)], "C"),
        # legs darker
        ("runs", [(17, 13, 21), (18, 14, 20)], "D"),
        # claws
        ("put", 19, 3, "W"),
        ("put", 19, 6, "W"),
        ("put", 19, 14, "W"),
        ("put", 19, 17, "W"),
    ],
}
