"""Ceratonoth, herbivore. The desert triceratops: tan body with THREE
tall pale horns rising from the head, a spiked ridge down the back, cream
belly, plodding legs. The horned-herbivore archetype kestodon and
dalthydon derive from."""

CONFIG = {
    "name": "ceratonoth",
    "size": (32, 24),
    "compare_to": "../icons/mhwilds/ceratonoth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "T": (192, 166, 120, 255),  # tan hide
        "D": (152, 128, 90, 255),   # darker shade
        "S": (224, 208, 176, 255),  # pale horns / spikes
        "C": (222, 208, 178, 255),  # cream belly
        "W": (246, 242, 230, 255),
    },
    "base": "T",
    "spans": {
        1:  [(8, 9), (12, 13), (16, 17)],     # three horn tips
        2:  [(7, 10), (11, 14), (15, 18)],
        3:  [(6, 11), (10, 15), (14, 18)],
        4:  [(5, 12), (9, 15), (13, 18)],     # horn bases
        5:  [(4, 13), (12, 19)],
        6:  [(3, 14), (11, 21)],
        7:  [(2, 15), (10, 23)],
        8:  [(1, 16), (10, 25)],
        9:  [(1, 17), (9, 26)],
        10: [(2, 18), (9, 27)],
        11: [(2, 19), (8, 28)],
        12: [(3, 19), (8, 28)],
        13: [(3, 18), (9, 28)],
        14: [(4, 17), (10, 28)],
        15: [(5, 16), (12, 27)],
        16: [(6, 15), (14, 26)],
        17: [(7, 11), (16, 18), (20, 24)],    # legs
        18: [(7, 10), (17, 17), (21, 23)],
        19: [(7, 7), (9, 9), (21, 21), (23, 23)],
    },
    "fills": [
        # three pale horns
        ("runs", [(1, 8, 9), (2, 7, 10), (3, 6, 11), (4, 5, 8),
                  (1, 12, 13), (2, 11, 14), (3, 10, 15), (4, 9, 11),
                  (1, 16, 17), (2, 15, 18), (3, 14, 18), (4, 13, 18)],
         "S"),
        # eye under the middle horn
        ("put", 5, 5, "K"),
        # spiked ridge along the back
        ("runs", [(6, 12, 13), (7, 11, 12), (8, 12, 13), (9, 11, 12),
                  (10, 13, 14), (11, 12, 13)], "S"),
        # cream belly along the bottom edge
        ("runs", [(12, 4, 16), (13, 4, 16), (14, 5, 15), (15, 6, 14),
                  (16, 7, 13)], "C"),
        # back shade
        ("runs", [(10, 19, 26), (11, 20, 27), (12, 20, 27)], "D"),
        # hooves
        ("put", 19, 7, "D"),
        ("put", 19, 9, "D"),
        ("put", 19, 21, "D"),
        ("put", 19, 23, "D"),
    ],
}
