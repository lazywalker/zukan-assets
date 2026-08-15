"""Khezu, flying wyvern. The blind flesh wyvern: a pale plump body with
no eyes, wing-claws folded like crumpled arms, a gaping sucker mouth
ringed with teeth, and a musky tail. The khezu archetype red-khezu
derives from."""

CONFIG = {
    "name": "khezu",
    "size": (28, 24),
    "compare_to": "../icons/mh4u/khezu.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (204, 196, 186, 255),  # pale flesh
        "D": (168, 158, 148, 255),  # darker flesh shade
        "R": (188, 74, 64, 255),    # red mouth interior
        "W": (246, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        3:  [(3, 10)],                        # head top
        4:  [(2, 11), (12, 14)],
        5:  [(1, 12), (11, 16)],
        6:  [(1, 12), (10, 18)],              # head + wing arm
        7:  [(1, 12), (9, 19)],
        8:  [(0, 12), (9, 20)],               # mouth zone + wing
        9:  [(0, 12), (8, 21)],
        10: [(0, 12), (8, 21)],
        11: [(0, 12), (8, 21)],
        12: [(1, 12), (8, 21)],
        13: [(1, 12), (8, 20)],
        14: [(2, 12), (8, 19)],
        15: [(2, 12), (8, 18)],
        16: [(3, 12), (8, 16)],
        17: [(4, 11), (8, 13)],
        18: [(5, 11)],
        19: [(6, 11), (8, 10)],
    },
    "fills": [
        # gaping sucker mouth: red interior ringed with teeth
        ("runs", [(8, 1, 8), (9, 0, 8)], "R"),
        ("put", 8, 1, "W"),
        ("put", 8, 4, "W"),
        ("put", 8, 7, "W"),
        ("put", 9, 0, "W"),
        ("put", 9, 3, "W"),
        ("put", 9, 6, "W"),
        ("put", 9, 8, "W"),
        # nostril slits, no eyes
        ("runs", [(5, 2, 4)], "D"),
        # wing-claw claws
        ("put", 4, 13, "D"),
        ("put", 5, 15, "D"),
        ("put", 6, 17, "D"),
        # body shade along the bottom
        ("runs", [(15, 3, 11), (16, 4, 11), (17, 5, 10)], "D"),
        # tail stub
        ("runs", [(19, 6, 10)], "D"),
    ],
}
