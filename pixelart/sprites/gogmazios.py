"""Gogmazios, elder dragon. The oil dragon: a massive black-bronze bulk
dripping sticky oil, a halberd stuck in its back, small horns, and a
dim orange glow behind the forearms."""

CONFIG = {
    "name": "gogmazios",
    "size": (36, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (64, 56, 52, 255),     # black-bronze bulk
        "D": (46, 40, 38, 255),     # darker bulk
        "O": (198, 128, 56, 255),   # bronze glow
        "T": (96, 84, 96, 255),     # halberd steel
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        2:  [(5, 6), (9, 10)],                # horn tips
        3:  [(4, 11)],
        4:  [(3, 12), (13, 15)],
        5:  [(2, 14), (12, 17)],
        6:  [(1, 15), (11, 19)],
        7:  [(1, 16), (10, 22)],              # bulk + halberd
        8:  [(0, 17), (9, 24)],
        9:  [(0, 17), (9, 26)],
        10: [(0, 17), (9, 28)],
        11: [(0, 17), (9, 30)],
        12: [(0, 17), (9, 31)],
        13: [(0, 17), (9, 32)],
        14: [(0, 17), (9, 33)],
        15: [(0, 17), (9, 33)],
        16: [(0, 17), (9, 33)],
        17: [(0, 17), (9, 33)],
        18: [(1, 17), (9, 33)],
        19: [(1, 17), (9, 33)],
        20: [(2, 17), (10, 33)],
        21: [(4, 10), (13, 17), (20, 24), (28, 32)],  # legs
        22: [(4, 9), (14, 16), (21, 23), (29, 31)],
    },
    "fills": [
        # small horns dark, raised one row
        ("runs", [(1, 5, 5), (1, 9, 9), (2, 4, 6), (2, 8, 10),
                  (3, 4, 9)], "D"),
        # pale eye
        ("put", 6, 5, "W"),
        # tusked mouth: dark gap with pale tusks
        ("runs", [(7, 1, 4)], "K"),
        ("put", 7, 1, "W"),
        ("put", 7, 4, "W"),
        ("put", 8, 1, "W"),
        ("put", 8, 4, "W"),
        # halberd blade stuck in the back
        ("runs", [(4, 13, 15), (5, 12, 17), (6, 11, 19), (7, 10, 16)],
         "T"),
        # oil drips down the flank
        ("runs", [(10, 25, 27), (11, 27, 29), (12, 29, 30),
                  (13, 30, 31)], "O", "N"),
        # bronze glow behind the forearms
        ("runs", [(15, 1, 6), (16, 1, 6), (17, 1, 6)], "O", "N"),
        # bulk shade
        ("runs", [(16, 1, 33), (17, 1, 33), (18, 2, 33)], "D"),
        # legs darker
        ("runs", [(21, 13, 17), (21, 20, 24), (22, 14, 16)], "D"),
    ],
}
