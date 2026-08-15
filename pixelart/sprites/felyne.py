"""Felyne, lynian. The palico: a small biped cat standing upright, big
pointed ears, round head, compact body, tail held up, tiny paws. The
lynian archetype the others derive from."""

CONFIG = {
    "name": "felyne",
    "size": (24, 24),
    "compare_to": "../icons/mhrise/felyne.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (226, 216, 196, 255),  # cream fur
        "D": (188, 176, 156, 255),  # fur shade
        "N": (80, 70, 62, 255),     # dark ear tips / eyes
        "R": (200, 90, 70, 255),    # nose
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        3:  [(6, 7), (11, 12)],               # ear tips
        4:  [(5, 13)],
        5:  [(5, 14)],                        # head
        6:  [(4, 15)],
        7:  [(4, 15)],                        # head + body
        8:  [(4, 15)],
        9:  [(3, 16)],                        # body
        10: [(3, 16), (16, 17)],              # tail
        11: [(3, 16), (16, 18)],
        12: [(4, 15), (17, 18)],
        13: [(5, 14)],
        14: [(6, 13)],
        15: [(7, 11), (12, 13)],              # legs
        16: [(7, 7), (9, 9), (12, 12)],
    },
    "fills": [
        # dark ear tips
        ("runs", [(3, 6, 7), (3, 11, 12)], "N"),
        # big round eyes
        ("put", 6, 7, "K"),
        ("put", 6, 12, "K"),
        # pink nose + mouth
        ("put", 8, 9, "R"),
        ("put", 9, 9, "N"),
        # fur shade on the belly and tail
        ("runs", [(10, 4, 7), (11, 4, 7), (12, 5, 7)], "D"),
        ("runs", [(11, 16, 18), (12, 17, 18)], "D"),
        # paws
        ("put", 16, 7, "D"),
        ("put", 16, 9, "D"),
        ("put", 16, 12, "D"),
    ],
}
