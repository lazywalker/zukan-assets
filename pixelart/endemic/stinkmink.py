"""Stinkmink: a slim pink weasel with a long low body and a smug face."""
CONFIG = {
    "name": "stinkmink",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (222, 150, 140, 255),  # pink pelt
        "D": (178, 112, 104, 255),  # darker pelt
        "C": (244, 214, 204, 255),  # belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        10: [(2, 8)],
        11: [(1, 10)],
        12: [(1, 26)],
        13: [(1, 28)],
        14: [(2, 28)],
        15: [(3, 27)],
        16: [(5, 25)],
        17: [(7, 23)],
        18: [(10, 20)],
        19: [(13, 13), (17, 17), (21, 21)],
    },
    "fills": [
        # head with a smug closed-eye and a small ear
        ("put", 10, 6, "D"),
        ("runs", [(11, 4, 5), (12, 4, 4)], "C"),
        ("put", 12, 5, "K"),
        # back stripe darker
        ("runs", [(12, 8, 24), (13, 9, 26)], "D"),
        # belly band
        ("runs", [(14, 4, 22), (15, 5, 21), (16, 6, 19)], "C"),
        # tail tip dark
        ("runs", [(16, 22, 25), (17, 20, 23)], "D"),
    ],
}
