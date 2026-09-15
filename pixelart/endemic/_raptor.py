"""Raptor bird archetype: a bigger bird of prey facing left, hooked beak,
heavy brow, folded wing, long tail feathers stepping down, strong legs
with talons."""

CONFIG = {
    "name": "_raptor",
    "size": (32, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (140, 110, 80, 255),   # body
        "D": (100, 78, 56, 255),    # wing / tail
        "C": (226, 206, 176, 255),  # breast
        "Y": (226, 178, 70, 255),   # beak / talons
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(10, 15)],
        6:  [(9, 16)],
        7:  [(7, 16)],
        8:  [(7, 16)],
        9:  [(8, 16)],
        10: [(8, 15), (16, 22)],
        11: [(9, 15), (16, 24)],
        12: [(10, 15), (18, 26)],
        13: [(10, 14), (21, 26)],
        14: [(10, 14), (24, 25)],
        15: [(11, 11), (14, 14)],
        16: [(11, 11), (14, 14)],
    },
    "fills": [
        # hooked beak
        ("runs", [(7, 7, 8)], "Y"),
        ("put", 8, 7, "Y"),
        # heavy brow + eye
        ("put", 6, 10, "D"),
        ("put", 7, 11, "W"),
        ("put", 7, 12, "K"),
        # folded wing darker
        ("runs", [(10, 9, 15), (11, 10, 15), (12, 11, 15), (13, 11, 14)],
         "D"),
        # breast pale
        ("runs", [(10, 8, 8), (11, 9, 9), (12, 10, 10)], "C"),
        # tail feathers stepping down
        ("runs", [(10, 16, 22), (11, 16, 24), (12, 18, 26), (13, 21, 26)],
         "D"),
        # talons
        ("runs", [(15, 11, 11), (15, 14, 14), (16, 11, 11), (16, 14, 14)],
         "Y"),
    ],
}
