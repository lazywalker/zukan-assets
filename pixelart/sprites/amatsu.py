"""Amatsu, elder dragon. The storm serpent: a dark slate serpentine body
flowing down-right, a horned head at the left crowned by a huge pale
webbed crest fin, pale fin ridges breaking the back line, a pale belly,
and a wide tail fin. The crested head and the ridged back are the
signature."""

CONFIG = {
    "name": "amatsu",
    "size": (38, 24),
    "compare_to": "../icons/mhgu/amatsu.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (62, 70, 92, 255),     # slate blue body
        "D": (46, 52, 70, 255),     # darker slate
        "C": (206, 218, 232, 255),  # pale webbing / belly
        "A": (120, 190, 210, 255),  # cyan fin accents
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(3, 4), (11, 12)],               # crest fin tips
        4:  [(2, 5), (10, 13)],
        5:  [(1, 6), (9, 14)],                # crest fin
        6:  [(1, 8), (8, 17)],                # head top + fin webbing
        7:  [(0, 10), (7, 20)],               # head + back start
        8:  [(0, 23)],
        9:  [(0, 26)],
        10: [(0, 28)],
        11: [(1, 30)],
        12: [(2, 32)],
        13: [(3, 34)],
        14: [(5, 35)],
        15: [(7, 36)],
        16: [(9, 35)],
        17: [(12, 33)],
        18: [(15, 30)],
        19: [(18, 26)],                       # tail taper
        20: [(21, 24)],                       # tail fin tip
    },
    "fills": [
        # huge pale crest fin webbing over the head
        ("runs", [(3, 3, 4), (4, 2, 5), (5, 1, 6), (6, 1, 8)], "C"),
        ("runs", [(4, 10, 13), (5, 9, 14), (6, 8, 14)], "C"),
        ("put", 3, 3, "A"),
        ("put", 3, 11, "A"),
        # horned snout below the crest
        ("runs", [(7, 0, 4), (8, 0, 4)], "D"),
        ("put", 8, 2, "W"),
        ("runs", [(9, 0, 3)], "C"),
        # pale fin ridges breaking the back line
        ("runs", [(7, 15, 17), (7, 19, 20), (8, 21, 23), (9, 24, 26),
                  (10, 27, 28)], "C"),
        # pale belly along the bottom edge
        ("runs", [(13, 8, 30), (14, 10, 31), (15, 12, 31)], "C"),
        # dark upper shade behind the head
        ("runs", [(9, 4, 10), (10, 5, 11)], "D"),
        # wide tail fin pale
        ("runs", [(18, 27, 30), (19, 24, 26), (20, 21, 24)], "C"),
        ("put", 18, 30, "A"),
        ("put", 19, 26, "A"),
    ],
}
