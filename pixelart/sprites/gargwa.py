"""Gargwa, bird wyvern. The grumpy farm bird: a plump olive-brown round
body, a pale face with a yellow beak, tiny folded wings, and thick yellow
legs. The plump-bird archetype porkeplume derives from."""

CONFIG = {
    "name": "gargwa",
    "size": (30, 24),
    "compare_to": "../icons/mhrise/gargwa.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (132, 132, 86, 255),   # olive-brown plumage
        "D": (102, 102, 66, 255),   # darker shade
        "C": (212, 202, 172, 255),  # pale face
        "Y": (222, 180, 70, 255),   # yellow beak / legs
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        4:  [(7, 12)],                        # head top
        5:  [(5, 14)],
        6:  [(4, 15), (14, 16)],
        7:  [(3, 16), (13, 18)],              # head + wing
        8:  [(2, 17), (12, 19)],
        9:  [(2, 18), (11, 20)],
        10: [(1, 19), (10, 21)],              # round body
        11: [(1, 20), (10, 22)],
        12: [(1, 20), (10, 22)],
        13: [(2, 20), (11, 21)],
        14: [(3, 19), (12, 20)],
        15: [(4, 18), (13, 19)],
        16: [(5, 17), (14, 18)],
        17: [(7, 11), (15, 17)],              # thick legs
        18: [(7, 10), (16, 16)],
        19: [(7, 7), (9, 9), (16, 16)],
    },
    "fills": [
        # pale grumpy face with a yellow beak
        ("runs", [(5, 5, 9), (6, 4, 10), (7, 3, 10), (8, 2, 9)], "C"),
        ("runs", [(7, 2, 4), (8, 2, 4)], "Y"),
        # small dark eyes
        ("put", 6, 6, "K"),
        ("put", 6, 9, "K"),
        # folded wing
        ("runs", [(8, 12, 18), (9, 12, 19), (10, 11, 19), (11, 11, 19),
                  (12, 11, 18)], "D"),
        # belly shade
        ("runs", [(13, 3, 12), (14, 4, 12), (15, 5, 11), (16, 6, 10)], "D"),
        # scaly legs
        ("runs", [(17, 7, 11), (17, 15, 17)], "Y"),
        ("put", 19, 7, "Y"),
        ("put", 19, 9, "Y"),
        ("put", 19, 16, "Y"),
    ],
}
