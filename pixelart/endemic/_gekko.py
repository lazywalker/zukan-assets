"""Gecko archetype: low long lizard facing left, rounded head with a big
lidded eye and lip line, long body, a tail extending right and curling
down, four splayed toes. Spots and a back stripe are species identity."""

CONFIG = {
    "name": "_gekko",
    "size": (34, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (120, 150, 90, 255),   # skin
        "D": (88, 114, 62, 255),    # darker: stripe, tail
        "C": (214, 220, 180, 255),  # belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        10: [(2, 8)],
        11: [(1, 10)],
        12: [(1, 27)],
        13: [(1, 29)],
        14: [(2, 29)],
        15: [(3, 30)],
        16: [(4, 31)],
        17: [(5, 32)],
        18: [(6, 32)],
        19: [(8, 30)],
        20: [(11, 11), (17, 17), (23, 23)],   # far legs
        21: [(4, 4), (6, 6), (12, 12), (14, 14), (19, 19), (21, 21)],
    },
    "fills": [
        # head: big lidded eye + lip line
        ("put", 11, 4, "W"),
        ("put", 11, 5, "K"),
        ("runs", [(12, 1, 3), (13, 1, 2)], "D"),
        # back stripe head to tail
        ("runs", [(12, 6, 24), (13, 6, 26), (14, 7, 27), (15, 8, 28),
                  (16, 9, 29), (17, 10, 30), (18, 11, 30)], "D"),
        # belly band
        ("runs", [(15, 4, 20), (16, 5, 20), (17, 6, 20), (18, 7, 20)], "C"),
        # spots
        ("put", 14, 10, "D"),
        ("put", 15, 12, "D"),
        ("put", 16, 14, "D"),
        # tail tip darker
        ("runs", [(17, 28, 32), (18, 29, 32), (19, 28, 30)], "D"),
    ],
}
