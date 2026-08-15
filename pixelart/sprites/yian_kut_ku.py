"""Yian Kut-Ku, bird wyvern. The classic pink-orange frillbird: a long
pointed beak with a pale tip and visible teeth, a huge cream ear-frill
flaring BACKWARD from behind the eye (not covering the face), pink-orange
scales, cream underbelly, spotted neck, striped tail. Derived from the
great-jaggi leader pose with enlarged frills and palette swap."""

CONFIG = {
    "name": "yian-kut-ku",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/yian-kut-ku.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (225, 140, 110, 255),  # pink-orange scales
        "C": (235, 190, 150, 255),  # cream frills and belly
        "B": (200, 170, 140, 255),  # beak
        "S": (170, 95, 75, 255),    # dark spots / shade
        "F": (235, 190, 150, 255),  # inherited frill color (cream)
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {**__import__("great_jaggi").CONFIG["spans"],
        3:  [(6, 8), (10, 14)],               # frill flares back
        4:  [(4, 9), (9, 15)],
        5:  [(2, 9), (8, 16)],
        6:  [(0, 9), (7, 16), (31, 32)],      # long beak
        7:  [(0, 9), (7, 16), (30, 33)],
        8:  [(1, 8), (7, 15), (29, 33)],
    },
    "fills": list(__import__("great_jaggi").CONFIG["fills"]) + [
        # cream ear-frill flaring backward behind the eye
        ("runs", [(3, 10, 14), (4, 10, 15), (5, 9, 16), (6, 8, 13),
                  (7, 9, 13), (8, 9, 14)], "C"),
        ("runs", [(4, 13, 15), (5, 14, 16), (6, 12, 13)], "O"),
        # long beak with pale tip
        ("runs", [(6, 0, 2), (7, 0, 2)], "B"),
        ("put", 6, 4, "W"),
        # orange head above the beak line
        ("runs", [(5, 4, 8), (6, 3, 8), (7, 4, 8)], "O"),
        # dark spots on the neck
        ("runs", [(10, 8, 9), (11, 10, 11)], "S"),
    ],
}
