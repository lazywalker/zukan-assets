"""Fatalis, elder dragon. The black dragon: classic western wyvern;
near-black scales, gray chest, curved swept horns, red eye, big folded
wing with dark membrane, thick tail. Minimal palette, maximum menace."""

CONFIG = {
    "name": "fatalis",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/fatalis.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (38, 34, 42, 255),     # black scales
        "D": (26, 24, 32, 255),     # darker shade
        "G": (120, 115, 125, 255),  # gray chest
        "R": (200, 50, 45, 255),    # red eye
        "W": (240, 236, 226, 255),  # horn / claws
    },
    "base": "B",
    "spans": {
        3:  [(2, 3), (15, 24)],
        4:  [(1, 4), (13, 26)],
        5:  [(1, 6), (12, 27)],
        6:  [(1, 7), (12, 28)],
        7:  [(1, 8), (12, 28)],
        8:  [(1, 9), (12, 27)],
        9:  [(1, 26)],
        10: [(1, 25)],
        11: [(1, 24)],
        12: [(1, 23)],
        13: [(2, 23)],
        14: [(3, 22)],
        15: [(4, 22)],
        16: [(5, 22)],
        17: [(6, 11), (21, 22)],
        18: [(7, 11), (22, 22)],
        19: [(8, 12), (23, 23)],
        20: [(9, 12), (24, 24)],
        21: [(10, 10), (13, 13), (23, 23)],
    },
    "fills": [
        # curved swept horns, pale
        ("runs", [(3, 2, 2), (4, 1, 2), (5, 1, 1)], "W"),
        ("runs", [(3, 15, 16), (4, 14, 15)], "W"),
        # red eye
        ("put", 6, 3, "R"),
        # folded wing: darker membrane
        ("runs", [(5, 13, 26), (6, 13, 27), (7, 13, 27), (8, 13, 27),
                  (9, 14, 26), (10, 15, 25), (11, 16, 24), (12, 17, 23)],
         "D"),
        # wing finger bones
        ("runs", [(6, 14, 15), (7, 15, 16), (8, 17, 18), (9, 19, 20)], "B"),
        # gray chest running into a gray belly along the bottom edge
        ("runs", [(10, 2, 4), (11, 2, 5), (12, 2, 6), (13, 3, 6),
                  (14, 4, 7), (15, 5, 8), (16, 6, 9), (17, 7, 10)], "G"),
        # claws
        ("put", 21, 10, "W"),
        ("put", 21, 13, "W"),
        ("put", 21, 23, "W"),
    ],
}
