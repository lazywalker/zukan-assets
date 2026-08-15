"""Brachydios, brute wyvern. The slime boxer: navy biped with a single
nose horn, tiny arms gone, both forelimbs swollen into huge glowing green
slime fists held low, slim legs, moderate tail."""

CONFIG = {
    "name": "brachydios",
    "size": (36, 24),
    "compare_to": "../icons/mhwi/brachydios.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (52, 60, 100, 255),    # navy body
        "D": (36, 42, 74, 255),     # darker navy shade
        "E": (168, 215, 110, 255),  # slime green glow
        "e": (118, 168, 78, 255),   # slime dark green
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        2:  [(3, 5)],                         # nose horn
        3:  [(2, 6)],
        4:  [(1, 7), (8, 8)],                 # head + neck spike
        5:  [(1, 8), (8, 10)],
        6:  [(0, 8), (9, 12)],                # head + neck
        7:  [(0, 8), (9, 14)],
        8:  [(1, 7), (9, 16)],
        9:  [(1, 6), (8, 18)],                # slime fist zone
        10: [(2, 5), (7, 19)],
        11: [(2, 4), (6, 20)],
        12: [(3, 19)],
        13: [(3, 18)],
        14: [(4, 17)],
        15: [(4, 16)],
        16: [(5, 15)],
        17: [(6, 13), (14, 16)],              # legs
        18: [(6, 12), (15, 16)],
        19: [(6, 11), (15, 15)],
        20: [(6, 10), (15, 15)],
        21: [(6, 6), (8, 8), (15, 15), (17, 17)],
    },
    "fills": [
        # navy crest over the skull, horn dark tip
        ("runs", [(3, 2, 6), (4, 1, 7)], "D"),
        # eye under the horn
        ("put", 6, 3, "W"),
        # huge glowing slime fists
        ("runs", [(9, 8, 14), (10, 7, 15), (11, 6, 15), (12, 6, 13)], "E"),
        ("runs", [(11, 11, 13), (12, 10, 11)], "e", "E"),
        # slime drips on the chest
        ("runs", [(8, 9, 11)], "E"),
        # dark back + tail top shade
        ("runs", [(12, 14, 19), (13, 14, 18), (14, 13, 17)], "D"),
        # legs darker
        ("runs", [(17, 14, 16), (18, 15, 16), (19, 15, 15)], "D"),
        # claws
        ("put", 21, 6, "W"),
        ("put", 21, 8, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 17, "W"),
    ],
}
