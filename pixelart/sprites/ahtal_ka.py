"""Ahtal-Ka, neopteron elder. The golden pharaoh mantis: a gold-striped
body with a tall crown, big violet forearms held up, thin rear legs, and
purple wing panels."""

CONFIG = {
    "name": "ahtal-ka",
    "size": (34, 24),
    "compare_to": "../icons/mhgu/ahtal-ka.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (206, 168, 74, 255),   # gold armor
        "D": (160, 126, 52, 255),   # darker gold
        "V": (108, 78, 158, 255),   # violet forearms / wings
        "v": (82, 58, 124, 255),    # darker violet
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(6, 7), (11, 12)],               # crown tips
        3:  [(5, 8), (10, 13)],
        4:  [(4, 9), (9, 14)],
        5:  [(3, 10), (9, 16)],               # head + wing start
        6:  [(2, 11), (8, 18)],
        7:  [(2, 12), (8, 20)],
        8:  [(2, 12), (7, 21)],               # body + forearm
        9:  [(2, 13), (7, 22)],
        10: [(2, 13), (6, 22)],
        11: [(3, 13), (6, 21)],
        12: [(3, 13), (7, 20)],
        13: [(4, 13), (8, 19)],
        14: [(4, 12), (10, 18)],
        15: [(5, 11), (12, 17)],
        16: [(6, 10), (13, 16)],
        17: [(7, 9), (13, 15)],               # rear legs
        18: [(7, 8), (14, 14)],
        19: [(7, 7), (14, 14)],
    },
    "fills": [
        # gold crown with dark stripes
        ("runs", [(2, 6, 7), (2, 11, 12), (3, 5, 8), (3, 10, 13),
                  (4, 4, 9), (4, 10, 13)], "D"),
        # violet eyes on the head
        ("put", 5, 5, "V"),
        ("put", 5, 7, "V"),
        # violet forearms held up
        ("runs", [(8, 7, 13), (9, 7, 13), (10, 6, 12), (11, 6, 11)], "V"),
        ("runs", [(9, 9, 11), (10, 8, 10)], "v", "V"),
        # violet wing panels over the back
        ("runs", [(5, 9, 16), (6, 9, 18), (7, 9, 19), (8, 14, 21),
                  (9, 14, 22)], "v"),
        # gold segment bands across the abdomen
        ("runs", [(10, 7, 13), (12, 8, 13), (14, 9, 12)], "D"),
        # rear legs dark
        ("runs", [(17, 7, 9), (17, 13, 15), (18, 7, 8)], "D"),
    ],
}
