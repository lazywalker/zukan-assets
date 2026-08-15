"""Alatreon, elder dragon. The blazing black dragon: twin pale horns
sweeping up from the head, purple wing membrane rising above the back
with three dark finger bones and a spiked edge, red eye, thick legs,
tapering tail."""

CONFIG = {
    "name": "alatreon",
    "size": (36, 24),
    "compare_to": "../icons/mh3u/alatreon.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (45, 38, 58, 255),     # black scales
        "D": (30, 26, 40, 255),     # darker shade
        "M": (104, 82, 148, 255),   # purple wing membrane
        "H": (168, 158, 188, 255),  # pale horns
        "R": (215, 60, 50, 255),    # red eye
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        1:  [(2, 3), (6, 7), (15, 15), (21, 21), (27, 27)],
        2:  [(1, 4), (5, 8), (15, 15), (21, 21), (27, 27)],
        3:  [(1, 5), (5, 9), (15, 15), (21, 21), (27, 27)],
        4:  [(1, 10), (12, 28)],              # head top + wing top
        5:  [(1, 7), (8, 11), (11, 28)],
        6:  [(1, 28)],                        # head + wing + body merged
        7:  [(1, 28)],
        8:  [(1, 28)],
        9:  [(1, 27)],
        10: [(2, 26)],
        11: [(2, 25)],
        12: [(3, 24)],
        13: [(4, 23)],
        14: [(5, 22)],
        15: [(6, 20)],
        16: [(8, 11), (17, 20)],              # legs
        17: [(8, 11), (17, 20)],
        18: [(8, 8), (10, 10), (17, 17), (19, 19)],
    },
    "fills": [
        # twin swept horns, pale and tall
        ("runs", [(1, 2, 3), (2, 1, 4), (3, 1, 5), (4, 1, 5)], "H"),
        ("runs", [(1, 6, 7), (2, 5, 8), (3, 5, 9), (4, 6, 10)], "H"),
        # red eye + brow
        ("put", 5, 3, "H"),
        ("put", 6, 3, "R"),
        # purple wing membrane above the back
        ("runs", [(4, 12, 28), (5, 11, 28), (6, 12, 28), (7, 13, 28),
                  (8, 14, 28)], "M"),
        # three dark finger bones radiating
        ("runs", [(4, 15, 15), (5, 16, 16), (6, 17, 17)], "D"),
        ("runs", [(4, 21, 21), (5, 22, 22), (6, 23, 23)], "D"),
        ("runs", [(4, 27, 27), (5, 27, 28), (6, 27, 28)], "D"),
        # wing spike tips pale
        ("put", 3, 15, "H"),
        ("put", 3, 21, "H"),
        ("put", 3, 27, "H"),
        # body underside shade
        ("runs", [(13, 5, 9), (14, 6, 9), (15, 7, 9)], "D"),
        # tail tip spikes
        ("runs", [(10, 25, 26), (11, 24, 25)], "D"),
        # claws
        ("put", 18, 8, "W"),
        ("put", 18, 10, "W"),
        ("put", 18, 17, "W"),
        ("put", 18, 19, "W"),
    ],
}
