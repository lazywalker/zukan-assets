"""Hypnocatrice, bird wyvern. The sleep bird: green-yellow plumage, pale
face, small crest, sleep-green spit. Kut-ku family but slimmer."""

CONFIG = {
    "name": "hypnocatrice",
    "size": (34, 24),
    "compare_to": "../icons/mhfu/hypnocatrice.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (140, 170, 110, 255),  # green plumage
        "Y": (220, 210, 130, 255),  # yellow face and belly
        "F": (110, 135, 90, 255),   # darker crest / shade
        "S": (95, 110, 80, 255),    # spots
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {**__import__("great_jaggi").CONFIG["spans"],
        3:  [(7, 11)],
        4:  [(5, 11)],
    },
    "fills": [
        ("runs", [(3, 7, 11), (4, 5, 9), (5, 10, 12)], "F"),
        ("runs", [(6, 1, 3), (7, 1, 3)], "Y"),
        ("runs", [(8, 2, 3)], "S"),
        # pale face
        ("runs", [(6, 4, 5), (7, 4, 5)], "Y"),
        ("put", 7, 5, "W"),
        # sleep spit
        ("runs", [(8, 1, 2)], "Y"),
        # cream belly along the bottom edge
        ("runs", [(14, 8, 11), (15, 8, 11), (16, 9, 11)], "Y"),
        # spots
        ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22)], "S"),
        # tail frill
        ("runs", [(9, 24, 25), (10, 26, 27)], "F"),
        ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28)], "S"),
        ("put", 21, 11, "W"),
        ("put", 21, 13, "W"),
        ("put", 21, 21, "W"),
    ],
}
