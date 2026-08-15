"""Aknosom, bird wyvern. The crested comb bird: compact round body with a
mushroom crest comb sitting on the head, pale white face with dark eyes and
pink cheeks, pale beak, short pointed tail, two clawed legs. Level belly
bottom, legs hang from it."""

CONFIG = {
    "name": "aknosom",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/aknosom.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (220, 120, 70, 255),   # orange-red plumage
        "C": (230, 160, 90, 255),   # crest comb
        "P": (235, 180, 160, 255),  # pink cheeks / belly
        "F": (240, 225, 210, 255),  # pale face
        "D": (170, 85, 50, 255),    # darker shade
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        2:  [(4, 12)],                        # crest comb top
        3:  [(3, 13)],
        4:  [(3, 13)],
        5:  [(2, 11)],                        # pale face top
        6:  [(1, 11)],                        # eyes
        7:  [(1, 11)],                        # cheeks
        8:  [(1, 11)],                        # beak
        9:  [(2, 13)],                        # chin -> body top
        10: [(3, 15), (14, 16)],              # body + short tail start
        11: [(4, 16), (15, 17)],
        12: [(4, 17)],
        13: [(4, 17)],
        14: [(4, 16)],
        15: [(5, 15)],
        16: [(5, 13)],                        # belly bottom
        17: [(4, 6), (9, 11)],                # legs
        18: [(4, 6), (9, 11)],
        19: [(4, 5), (9, 10)],
        20: [(4, 4), (10, 10)],
        21: [(4, 4), (10, 10)],
    },
    "fills": [
        # mushroom crest comb
        ("runs", [(2, 4, 12), (3, 3, 13)], "C"),
        ("runs", [(3, 5, 6), (3, 11, 12)], "D"),
        # pale face, dark eyes, pink cheeks
        ("runs", [(5, 3, 11), (6, 2, 11), (7, 2, 11)], "F"),
        ("runs", [(7, 2, 2), (7, 11, 11)], "P"),
        ("put", 6, 4, "K"),
        ("put", 6, 9, "K"),
        # pale beak
        ("runs", [(8, 2, 5), (9, 3, 4)], "P"),
        # body: orange with darker folded wing
        ("runs", [(10, 8, 13), (11, 9, 13), (12, 10, 13), (13, 11, 13),
                  (14, 11, 13)], "D"),
        # short tail tip, darker
        ("runs", [(11, 15, 17), (12, 16, 17)], "D"),
        # claws
        ("put", 21, 4, "W"),
        ("put", 21, 10, "W"),
    ],
}
