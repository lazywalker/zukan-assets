"""Jyuratodus, piscine wyvern. The mud fish: a tan-brown eel body caked
with mud, a big blunt head with a jagged grin, red side and crest fins,
paddle fins, thick tapering tail. The mud-fish archetype beotodus and
lavasioth derive from."""

CONFIG = {
    "name": "jyuratodus",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/jyuratodus.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (156, 130, 104, 255),  # mud-brown body
        "D": (118, 96, 74, 255),    # darker mud shade
        "R": (196, 88, 72, 255),    # red fins
        "C": (214, 196, 158, 255),  # pale belly
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        4:  [(6, 12)],                        # head top
        5:  [(4, 15), (16, 17)],              # head + crest fin
        6:  [(2, 17), (15, 19)],
        7:  [(1, 18), (14, 22)],
        8:  [(0, 18), (13, 24)],              # jaw + body
        9:  [(0, 17), (12, 26)],
        10: [(1, 17), (11, 28)],
        11: [(1, 17), (11, 29)],
        12: [(2, 16), (11, 30)],
        13: [(2, 16), (12, 31)],
        14: [(3, 15), (13, 32)],
        15: [(4, 15), (15, 33)],
        16: [(5, 14), (17, 33)],              # tail fin
        17: [(6, 13), (20, 32)],
        18: [(7, 12), (24, 30)],
        19: [(8, 11), (27, 28)],
    },
    "fills": [
        # red crest fin along the back
        ("runs", [(5, 16, 17), (6, 15, 19), (7, 14, 18)], "R"),
        # jagged white grin
        ("runs", [(8, 3, 12)], "K"),
        ("put", 8, 4, "W"),
        ("put", 8, 6, "W"),
        ("put", 8, 8, "W"),
        ("put", 8, 10, "W"),
        # pale eye
        ("put", 6, 5, "W"),
        ("put", 6, 6, "K"),
        # red side fin on the flank
        ("runs", [(11, 14, 17), (12, 13, 17), (13, 13, 16)], "R"),
        # pale belly along the bottom edge
        ("runs", [(13, 4, 12), (14, 5, 13), (15, 6, 13), (16, 7, 12)], "C"),
        # mud patches on the back
        ("runs", [(10, 18, 21), (11, 22, 25), (12, 20, 23),
                  (13, 24, 27)], "D"),
        # red tail fin
        ("runs", [(16, 28, 33), (17, 27, 32), (18, 26, 30)], "R"),
        # claws
        ("put", 19, 8, "W"),
        ("put", 19, 10, "W"),
    ],
}
