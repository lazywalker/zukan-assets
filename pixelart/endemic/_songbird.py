"""Songbird archetype: small perching bird facing left, round head, tiny
beak, darker folded wing, tail stepping down-right, two thin legs. Head
and breast colors are species identity."""

CONFIG = {
    "name": "_songbird",
    "size": (26, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (150, 120, 90, 255),   # head / breast
        "D": (110, 86, 62, 255),    # wing / tail
        "C": (222, 204, 170, 255),  # belly
        "Y": (226, 178, 70, 255),   # beak
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(9, 13)],
        6:  [(8, 14)],
        7:  [(6, 14)],
        8:  [(6, 14)],
        9:  [(7, 14)],
        10: [(7, 13), (14, 19)],
        11: [(8, 13), (14, 21)],
        12: [(9, 13), (16, 22)],
        13: [(9, 12), (19, 22)],
        14: [(9, 12), (21, 22)],
        15: [(10, 10), (12, 12)],
        16: [(10, 10), (12, 12)],
    },
    "fills": [
        # beak
        ("runs", [(7, 6, 7)], "Y"),
        # eye
        ("put", 7, 10, "W"),
        ("put", 7, 11, "K"),
        # folded wing darker
        ("runs", [(10, 8, 13), (11, 9, 13), (12, 10, 13)], "D"),
        # belly lighter
        ("runs", [(10, 7, 7), (11, 8, 8)], "C"),
        # tail darker stepping down
        ("runs", [(10, 14, 19), (11, 14, 21), (12, 16, 22), (13, 19, 22),
                  (14, 21, 22)], "D"),
    ],
}
