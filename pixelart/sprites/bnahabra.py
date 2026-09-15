"""Bnahabra, neopteron. The paralyzing fly, drawn in the front pose of its
icon: two cyan wings spread up and out, a dark body with big red
compound eyes, a yellow tail band and a red-tipped sting."""

CONFIG = {
    "name": "bnahabra",
    "size": (24, 24),
    "compare_to": "../icons/mhrise/bnahabra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (56, 46, 50, 255),      # dark body
        "D": (38, 32, 36, 255),      # darker shade
        "R": (226, 60, 64, 255),     # red eyes / sting tip
        "C": (120, 230, 230, 255),   # cyan wings
        "Q": (70, 160, 170, 255),    # dark cyan wing edge
        "Y": (240, 220, 80, 255),    # yellow band
    },
    "base": "B",
    "spans": {
        1:  [(5, 5), (18, 18)],                  # wing tips
        2:  [(4, 6), (17, 19)],
        3:  [(3, 6), (17, 20)],
        4:  [(2, 7), (16, 21)],                  # wings widest
        5:  [(2, 7), (16, 21)],
        6:  [(3, 6), (17, 20)],
        7:  [(4, 5), (18, 19)],                  # wing bottoms
        8:  [(9, 14)],                           # head top
        9:  [(8, 15)],                           # head
        10: [(8, 15)],
        11: [(7, 7), (9, 14), (16, 16)],         # legs + thorax
        12: [(7, 7), (10, 13), (16, 16)],        # abdomen
        13: [(7, 7), (10, 13), (16, 16)],
        14: [(11, 12)],                          # tail
        15: [(11, 12)],                          # sting
    },
    "fills": [
        # cyan wings with dark leading edge
        ("runs", [(1, 5, 5), (2, 4, 6), (3, 3, 6), (4, 2, 7), (5, 2, 7),
                  (6, 3, 6), (7, 4, 5), (1, 18, 18), (2, 17, 19),
                  (3, 17, 20), (4, 16, 21), (5, 16, 21), (6, 17, 20),
                  (7, 18, 19)], "C"),
        ("runs", [(2, 4, 4), (3, 3, 4), (4, 2, 3), (5, 2, 3), (6, 3, 4),
                  (7, 4, 4), (2, 19, 19), (3, 19, 20), (4, 20, 21),
                  (5, 20, 21), (6, 19, 20), (7, 19, 19)], "Q", "C"),
        # big red compound eyes
        ("runs", [(9, 8, 10), (9, 13, 15), (10, 8, 10), (10, 13, 15)],
         "R"),
        ("put", 9, 9, "K"),
        ("put", 9, 14, "K"),
        # dark head cap
        ("runs", [(8, 10, 13)], "D"),
        # yellow tail band and red sting tip
        ("runs", [(12, 10, 13), (13, 10, 13)], "Y", "B"),
        ("runs", [(15, 11, 12)], "R"),
        # dark legs
        ("runs", [(11, 7, 7), (12, 7, 7), (13, 7, 7), (11, 16, 16),
                  (12, 16, 16), (13, 16, 16)], "D"),
    ],
}
