"""Moofah, herbivore. The walking mop: a round snow-white fluff ball with
wavy fleece lines, a small dark face tucked low at the left, stub feet,
and a green sprout sprouting from the top."""

CONFIG = {
    "name": "moofah",
    "size": (26, 24),
    "compare_to": "../icons/mhgu/moofah.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (234, 232, 226, 255),  # white fleece
        "D": (196, 192, 184, 255),  # fleece wave lines
        "H": (74, 66, 60, 255),     # dark face
        "G": (128, 170, 84, 255),   # green sprout
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        2:  [(11, 12)],                       # sprout
        3:  [(10, 13)],
        4:  [(8, 15)],
        5:  [(6, 17)],
        6:  [(5, 18)],
        7:  [(4, 19)],
        8:  [(3, 20)],
        9:  [(3, 20)],
        10: [(2, 21)],
        11: [(2, 21)],
        12: [(2, 21)],
        13: [(3, 20)],
        14: [(4, 19)],
        15: [(5, 18)],
        16: [(6, 16)],
        17: [(8, 12), (14, 15)],              # feet
        18: [(8, 8), (10, 10), (14, 14)],
    },
    "fills": [
        # green sprout on top
        ("runs", [(2, 11, 12), (3, 10, 13)], "G"),
        # dark face tucked low at the left
        ("runs", [(8, 3, 7), (9, 3, 7), (10, 2, 6), (11, 2, 6),
                  (12, 2, 5)], "H"),
        # white eye dot
        ("put", 9, 4, "W"),
        # fleece wave lines
        ("runs", [(6, 8, 12), (7, 12, 16), (8, 12, 16), (10, 8, 12),
                  (11, 12, 17), (13, 8, 12), (13, 16, 19),
                  (14, 9, 13), (15, 12, 16)], "D"),
        # feet
        ("put", 18, 8, "D"),
        ("put", 18, 10, "D"),
        ("put", 18, 14, "D"),
    ],
}
