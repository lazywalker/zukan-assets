"""Abiorugu, flying wyvern. The jaw blade: a dark red-black brute with a
great jaw horn, a mouth full of fangs, spiked shoulders, and a thick
blade tail."""

CONFIG = {
    "name": "abiorugu",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (122, 46, 44, 255),    # dark red-black hide
        "D": (88, 32, 32, 255),     # darker hide
        "C": (228, 208, 172, 255),  # pale jaw horn / fangs
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        3:  [(2, 5), (9, 10)],               # horn base + shoulder spikes
        4:  [(1, 6), (8, 11)],
        5:  [(1, 7), (7, 13)],
        6:  [(1, 8), (6, 15)],               # head + jaw horn
        7:  [(1, 9), (5, 17)],
        8:  [(0, 10), (5, 19)],
        9:  [(0, 10), (5, 21)],              # jaw + body
        10: [(0, 10), (5, 22)],
        11: [(0, 10), (5, 23)],
        12: [(0, 10), (5, 24)],
        13: [(0, 10), (5, 24)],
        14: [(0, 10), (5, 24)],
        15: [(0, 10), (5, 24)],
        16: [(0, 10), (5, 24)],
        17: [(0, 10), (5, 24)],
        18: [(1, 10), (5, 24)],
        19: [(1, 10), (6, 24)],
        20: [(2, 10), (7, 23)],
        21: [(3, 8), (10, 13), (16, 19), (21, 22)],  # legs + tail
        22: [(3, 7), (11, 12), (17, 18)],
    },
    "fills": [
        # great pale jaw horn curving up from the chin; the signature
        ("runs", [(2, 3, 4), (3, 2, 5), (4, 1, 5), (5, 1, 5), (6, 0, 3),
                  (7, 0, 2)], "C"),
        # shoulder spikes pale
        ("runs", [(3, 9, 10), (4, 8, 9)], "C"),
        # dark eye
        ("put", 6, 5, "W"),
        # mouth full of fangs
        ("runs", [(8, 1, 8)], "K"),
        ("put", 8, 2, "W"),
        ("put", 8, 4, "W"),
        ("put", 8, 6, "W"),
        ("put", 8, 8, "W"),
        # body shade
        ("runs", [(16, 1, 24), (17, 1, 24), (18, 2, 24)], "D"),
        # legs darker
        ("runs", [(21, 10, 13), (21, 16, 19)], "D"),
        # claws
        ("put", 22, 3, "W"),
        ("put", 22, 11, "W"),
        ("put", 22, 17, "W"),
    ],
}
