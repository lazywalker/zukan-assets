"""Gore Magala, elder dragon. The black eclipse: a hunched body draped in
the tattered wing cloak whose bottom edge is cut by deep V notches, a low
head with two thin feeler-horns sweeping up-back to pale tips, tiny legs
peeking below the cloak front. The ragged cloak edge is the signature."""

CONFIG = {
    "name": "gore-magala",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/gore-magala.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (40, 35, 55, 255),     # near-black body
        "D": (28, 25, 40, 255),     # darker shade
        "P": (120, 90, 160, 255),   # purple: ragged cloak hem
        "W": (230, 228, 240, 255),  # pale feeler tips, eye
    },
    "base": "B",
    "spans": {
        2:  [(8, 8)],                     # near feeler tip
        3:  [(7, 8)],                     # feeler
        4:  [(6, 7), (11, 11)],           # feeler base + far feeler tip
        5:  [(5, 7), (10, 12)],           # head top + far feeler
        6:  [(4, 9), (9, 13)],            # head + far feeler base
        7:  [(3, 10), (8, 14)],           # head + cloak top edge
        8:  [(3, 22)],                    # head/neck/cloak merged
        9:  [(2, 25)],
        10: [(1, 27)],
        11: [(1, 28)],
        12: [(0, 28)],
        13: [(0, 27), (28, 30)],          # cloak hem + thin tail tip
        14: [(0, 27), (29, 31)],
        15: [(1, 24)],                    # notch 1 open at the hem
        16: [(1, 26)],                    # tatter 2
        17: [(2, 22)],                    # notch 2
        18: [(3, 24)],                    # tatter 3
        19: [(4, 20)],                    # notch 3
        20: [(5, 18)],                    # tatter 4
        21: [(6, 8), (11, 13)],           # tiny legs
        22: [(6, 6), (8, 8), (11, 11), (13, 13)],
    },
    "fills": [
        # feelers purple with pale tips
        ("runs", [(2, 8, 8), (3, 7, 8), (4, 6, 7), (5, 5, 6)], "P"),
        ("runs", [(4, 11, 11), (5, 10, 11), (6, 9, 11)], "P"),
        ("put", 2, 8, "W"),
        ("put", 4, 11, "W"),
        # brow shade + pale eye on the low head
        ("put", 5, 4, "D"),
        ("put", 6, 4, "WK"),
        # purple only on the tatter spikes below the hem line
        ("runs", [(15, 20, 23), (16, 22, 25), (17, 18, 21), (18, 19, 23),
                  (19, 13, 18), (20, 10, 16)], "P", "B"),
        # chest shade
        ("runs", [(8, 3, 6), (9, 2, 5), (10, 1, 4)], "D"),
        # legs dark with pale claws
        ("runs", [(21, 6, 8), (21, 11, 13), (22, 6, 6), (22, 8, 8),
                  (22, 11, 11), (22, 13, 13)], "D"),
        ("put", 22, 6, "W"),
        ("put", 22, 11, "W"),
    ],
}
