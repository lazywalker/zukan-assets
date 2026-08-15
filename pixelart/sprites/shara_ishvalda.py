"""Shara Ishvalda, elder dragon. The rock singer: a pale rock-shell body
with crumbling stone plates, a small round face with huge hollow eyes,
and wing-plates risen like shattered slabs."""

CONFIG = {
    "name": "shara-ishvalda",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (196, 186, 166, 255),  # pale rock shell
        "D": (158, 148, 130, 255),  # darker rock
        "C": (226, 220, 204, 255),  # pale face plate
        "N": (58, 52, 56, 255),     # hollow eyes
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(8, 10)],                        # face crown
        3:  [(6, 12)],
        4:  [(5, 14), (15, 17)],
        5:  [(4, 15), (14, 19)],              # face + wing slabs
        6:  [(3, 16), (13, 21)],
        7:  [(2, 17), (12, 23)],
        8:  [(2, 18), (11, 24)],
        9:  [(1, 18), (10, 25)],
        10: [(1, 18), (10, 26)],
        11: [(1, 18), (10, 26)],
        12: [(1, 18), (10, 26)],
        13: [(1, 18), (10, 26)],
        14: [(1, 18), (10, 26)],
        15: [(2, 18), (10, 26)],
        16: [(2, 18), (10, 25)],
        17: [(3, 18), (11, 24)],
        18: [(4, 17), (12, 22)],
        19: [(5, 16), (14, 19)],              # legs
        20: [(5, 15), (15, 18)],
        21: [(5, 5), (7, 7), (14, 14), (16, 16)],
    },
    "fills": [
        # round pale face with huge hollow eyes
        ("runs", [(3, 6, 12), (4, 5, 14), (5, 4, 14), (6, 4, 13),
                  (7, 3, 12)], "C"),
        ("runs", [(5, 6, 7), (5, 11, 12), (6, 6, 7), (6, 11, 12)], "N"),
        # crumbling rock plates on the shell
        ("runs", [(5, 15, 19), (6, 14, 21), (7, 13, 23), (8, 12, 24),
                  (9, 11, 25)], "D", "G"),
        ("runs", [(7, 17, 18), (8, 18, 19), (9, 19, 20),
                  (10, 20, 21)], "C", "D"),
        # body shade
        ("runs", [(16, 2, 18), (17, 3, 18), (18, 4, 17)], "D"),
        # legs darker
        ("runs", [(19, 14, 19), (20, 15, 18)], "D"),
        # claws
        ("put", 21, 5, "W"),
        ("put", 21, 7, "W"),
        ("put", 21, 14, "W"),
        ("put", 21, 16, "W"),
    ],
}
