"""Bullfango, fanged beast. The charging boar: bristly brown body with a
dark mane ridge along the back, a pale curved tusk jutting up from the
jaw, blunt snout, stocky legs, thin curled tail."""

CONFIG = {
    "name": "bullfango",
    "size": (28, 24),
    "compare_to": "../icons/mhrise/bullfango.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (120, 85, 58, 255),     # brown hide
        "D": (85, 58, 40, 255),      # dark brown shade
        "M": (58, 42, 32, 255),      # near-black mane
        "C": (225, 210, 180, 255),   # pale tusk
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        5:  [(3, 12)],                         # mane ridge
        6:  [(1, 14)],
        7:  [(1, 14), (15, 17)],               # head + body start
        8:  [(0, 14), (13, 19)],
        9:  [(0, 14), (12, 20)],
        10: [(1, 14), (12, 21)],
        11: [(2, 14), (12, 22)],
        12: [(3, 14), (12, 22)],
        13: [(4, 14), (12, 22)],
        14: [(5, 13), (12, 22)],
        15: [(6, 13), (12, 21)],
        16: [(12, 21)],
        17: [(6, 9), (13, 16), (19, 22)],      # legs
        18: [(6, 9), (13, 16), (19, 22)],
        19: [(6, 9), (13, 16), (19, 22)],
        20: [(6, 6), (8, 8), (13, 13), (15, 15), (19, 19), (21, 21)],
    },
    "fills": [
        # dark mane ridge along the back and head top
        ("runs", [(5, 3, 12), (6, 8, 14), (7, 8, 14), (8, 9, 14),
                  (9, 10, 14)], "M"),
        # dark mouth gap
        ("runs", [(9, 2, 5)], "K"),
        # pale tusk curving up from the jaw
        ("runs", [(7, 1, 2), (8, 0, 2), (9, 0, 1)], "C"),
        # eye
        ("put", 7, 4, "W"),
        ("put", 7, 5, "K"),
        # hide shade along the belly
        ("runs", [(13, 5, 11), (14, 6, 12), (15, 7, 12)], "D"),
        # curled tail
        ("runs", [(14, 20, 22), (15, 20, 21)], "D"),
        # rear leg darker
        ("runs", [(17, 19, 22), (18, 19, 22), (19, 19, 22)], "D"),
        # claws
        ("put", 20, 6, "W"),
        ("put", 20, 8, "W"),
        ("put", 20, 13, "W"),
        ("put", 20, 15, "W"),
        ("put", 20, 19, "W"),
        ("put", 20, 21, "W"),
    ],
}
