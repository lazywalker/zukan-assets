"""Garangolm, fanged beast. The moss golem: a hulking green-grey body with
mossy garden arms, one arm raised, a flat brow face, and stone knuckles."""

CONFIG = {
    "name": "garangolm",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (122, 128, 108, 255),  # grey-green hide
        "D": (92, 98, 80, 255),     # darker shade
        "M": (110, 152, 84, 255),   # moss garden
        "O": (196, 130, 60, 255),   # amber eyes
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(5, 8), (11, 13)],               # brow ridge
        3:  [(4, 14)],
        4:  [(3, 15)],
        5:  [(2, 16)],
        6:  [(2, 18)],                        # shoulders
        7:  [(1, 19), (19, 21)],              # raised fist
        8:  [(1, 19), (19, 22)],
        9:  [(1, 19), (18, 22)],
        10: [(1, 19), (18, 22)],
        11: [(1, 19), (18, 22)],
        12: [(1, 19), (18, 22)],
        13: [(1, 19), (18, 22)],
        14: [(2, 19), (18, 22)],
        15: [(2, 19), (18, 21)],
        16: [(3, 19), (18, 21)],
        17: [(4, 19), (18, 21)],
        18: [(5, 12), (15, 18)],              # legs
        19: [(5, 11), (16, 17)],
        20: [(5, 10), (16, 16)],
    },
    "fills": [
        # flat brow with amber eyes
        ("runs", [(2, 5, 13), (3, 4, 14)], "D"),
        ("put", 4, 6, "O"),
        ("put", 4, 11, "O"),
        # moss garden growing over the shoulders and raised fist
        ("runs", [(2, 5, 8), (2, 11, 13), (6, 1, 8), (7, 1, 10),
                  (8, 1, 8)], "M"),
        ("runs", [(7, 19, 21), (8, 19, 22), (9, 18, 21)], "M"),
        # stone knuckles
        ("runs", [(12, 18, 22), (13, 18, 22)], "D"),
        # chest shade
        ("runs", [(14, 3, 18), (15, 3, 18), (16, 4, 18), (17, 5, 18)], "D"),
        # legs darker
        ("runs", [(18, 15, 18), (19, 16, 17)], "D"),
        # claws
        ("put", 20, 5, "W"),
        ("put", 20, 8, "W"),
        ("put", 20, 16, "W"),
    ],
}
