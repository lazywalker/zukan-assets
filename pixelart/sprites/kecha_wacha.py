"""Kecha Wacha, fanged beast. The big-eared acrobat: an orange monkey
swinging by one huge flat hand held up-right, giant ear-fins flaring from
the round face, a second hand below, and a hooked tail."""

CONFIG = {
    "name": "kecha-wacha",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/kecha-wacha.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (206, 122, 58, 255),   # orange fur
        "D": (160, 90, 44, 255),    # darker orange
        "C": (232, 204, 160, 255),  # pale face / hands
        "E": (222, 148, 60, 255),   # bright ear rings
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        2:  [(13, 16)],                       # giant ear-fin top
        3:  [(12, 17), (18, 19)],             # ear + hand
        4:  [(10, 18), (18, 20)],
        5:  [(9, 18), (18, 21)],              # ear + hand
        6:  [(8, 17), (18, 21)],
        7:  [(7, 17), (18, 21)],
        8:  [(6, 16), (18, 20)],              # face + hand
        9:  [(5, 15), (17, 19)],
        10: [(5, 15), (17, 18)],
        11: [(5, 15), (17, 18)],              # body
        12: [(5, 15), (17, 18)],
        13: [(5, 15), (17, 18)],
        14: [(5, 15), (17, 18)],
        15: [(6, 15), (17, 19)],
        16: [(6, 14), (17, 20)],              # tail hook
        17: [(7, 13), (18, 21)],
        18: [(7, 12), (19, 21)],
        19: [(8, 12), (20, 21)],
        20: [(9, 11), (21, 21)],
        21: [(10, 11)],                       # hanging foot
    },
    "fills": [
        # giant pale ear-fins with bright rings
        ("runs", [(2, 13, 16), (3, 12, 17), (4, 10, 14), (5, 9, 12),
                  (6, 8, 10)], "C"),
        ("runs", [(3, 13, 16), (4, 12, 15)], "E", "C"),
        # round pale face
        ("runs", [(7, 8, 15), (8, 7, 14), (9, 6, 14), (10, 6, 14)], "C"),
        # big orange eyes
        ("put", 8, 9, "E"),
        ("put", 8, 13, "E"),
        ("put", 8, 10, "K"),
        ("put", 8, 12, "K"),
        # small nose + mouth
        ("put", 10, 11, "K"),
        # upper hand gripping
        ("runs", [(3, 18, 19), (4, 18, 20), (5, 18, 21), (6, 18, 21),
                  (7, 18, 21), (8, 18, 20)], "C"),
        # lower hand
        ("runs", [(15, 17, 19), (16, 17, 20), (17, 18, 21)], "C"),
        # tail hook pale
        ("runs", [(17, 19, 21), (18, 20, 21), (19, 20, 21)], "C"),
        # belly shade
        ("runs", [(13, 6, 14), (14, 6, 14), (15, 7, 14)], "D"),
        # hanging foot
        ("runs", [(20, 10, 11), (21, 10, 11)], "D"),
    ],
}
