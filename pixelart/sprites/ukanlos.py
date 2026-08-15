"""Ukanlos, flying wyvern. The shovel jaw: a grey-white tank whose huge
pale spade jaw protrudes forward past the head, small sunk eyes high on
the skull, dark back spines, heavy legs with dark claws."""

CONFIG = {
    "name": "ukanlos",
    "size": (36, 24),
    "compare_to": "../icons/mh4u/ukanlos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (172, 176, 178, 255),  # grey-white hide
        "D": (134, 138, 142, 255),  # darker shade
        "N": (76, 80, 86, 255),     # dark spines
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(7, 10), (14, 15)],              # back spines
        4:  [(5, 12), (13, 16)],
        5:  [(3, 14), (12, 18)],
        6:  [(2, 15), (10, 20)],
        7:  [(2, 16), (9, 21)],               # skull top
        8:  [(1, 17), (8, 22)],               # head
        9:  [(0, 17), (7, 23)],               # jaw protrudes past the head
        10: [(0, 18), (6, 24)],
        11: [(0, 16), (6, 24)],               # jaw bottom
        12: [(1, 17), (6, 24)],
        13: [(1, 17), (6, 24)],
        14: [(1, 17), (6, 24)],
        15: [(1, 17), (6, 24)],
        16: [(1, 17), (6, 24)],
        17: [(1, 17), (6, 24)],
        18: [(2, 17), (6, 24)],
        19: [(2, 17), (7, 24)],
        20: [(3, 17), (8, 24)],
        21: [(4, 10), (13, 16), (19, 22)],    # legs
        22: [(4, 9), (14, 15), (20, 21)],
        23: [(4, 4), (6, 6), (14, 14), (20, 20)],
    },
    "fills": [
        # dark back spines
        ("runs", [(3, 7, 10), (3, 14, 15), (4, 5, 7), (4, 13, 15),
                  (5, 12, 14)], "N"),
        # small sunk eyes high on the skull
        ("put", 7, 4, "N"),
        ("put", 7, 8, "N"),
        # huge pale spade jaw edge with dark teeth
        ("runs", [(9, 0, 14)], "W"),
        ("runs", [(10, 0, 16), (11, 0, 14)], "D"),
        ("runs", [(9, 2, 2), (9, 5, 5), (9, 8, 8), (9, 11, 11)],
         "D", "W"),
        # jaw hinge shadow
        ("runs", [(9, 12, 17)], "D"),
        # body shade
        ("runs", [(18, 3, 16), (19, 3, 16), (20, 4, 16)], "D"),
        # dark claws
        ("put", 23, 4, "N"),
        ("put", 23, 6, "N"),
        ("put", 23, 14, "N"),
        ("put", 23, 20, "N"),
    ],
}
