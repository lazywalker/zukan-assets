"""Plesioth, leviathan. The fish wyvern, drawn long and low like its
leviathan kin: a blunt orange head with an open toothy jaw and a gill
line, a jagged slate dorsal fin on the arched back, a dark pectoral fin
fan on the chest, a cream belly, small webbed leg fins, and the
signature huge crescent tail fin with radiating rays."""

CONFIG = {
    "name": "plesioth",
    "size": (56, 24),
    "compare_to": "../icons/mh3u/plesioth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (204, 124, 58, 255),    # orange scales
        "D": (158, 92, 44, 255),     # darker orange shade / spots
        "F": (72, 84, 108, 255),     # slate fins
        "C": (233, 213, 164, 255),   # cream belly / fin rays
        "Y": (230, 190, 72, 255),
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        1:  [(47, 49)],                          # tail top lobe tip
        2:  [(45, 50), (25, 26)],                # tail lobe, dorsal tip
        3:  [(3, 8), (24, 27), (43, 51)],
        4:  [(2, 9), (23, 28), (42, 52)],
        5:  [(1, 10), (22, 29), (41, 52)],
        6:  [(0, 11), (14, 30), (40, 51)],
        7:  [(0, 33), (39, 46)],
        8:  [(6, 36), (38, 43)],                 # mouth gap at cols 0-5
        9:  [(1, 5), (7, 38), (37, 41)],         # lower jaw + body
        10: [(1, 5), (8, 39), (36, 40)],
        11: [(10, 40), (36, 39)],
        12: [(11, 40), (36, 42)],
        13: [(12, 40), (37, 45)],
        14: [(13, 39), (38, 47)],
        15: [(14, 38), (39, 48)],
        16: [(15, 36), (40, 49)],
        17: [(16, 19), (25, 28), (41, 49)],
        18: [(16, 18), (26, 28), (43, 50)],
        19: [(16, 16), (18, 18), (26, 26), (28, 28), (45, 49)],
        20: [(46, 48)],
    },
    "fills": [
        # eye: brow over a yellow pupil
        ("put", 3, 6, "K"),
        ("put", 4, 6, "Y"),
        ("put", 4, 7, "K"),
        # nostril on the snout
        ("put", 5, 0, "K"),
        # open mouth: white fangs in the black gap
        ("put", 8, 1, "W"),
        ("put", 8, 4, "W"),
        # gill line behind the head
        ("runs", [(5, 10, 10), (6, 10, 10), (7, 10, 10)], "K"),
        # slate dorsal fin, slim spikes over the back line
        ("runs", [(2, 25, 26), (3, 24, 27), (4, 23, 28), (5, 22, 29),
                  (6, 22, 30)], "F"),
        ("runs", [(5, 25, 25), (6, 24, 24), (6, 28, 28)], "C", "F"),
        # dark spots along the back, like the icon
        ("runs", [(8, 24, 25), (9, 30, 31), (10, 20, 21), (11, 27, 28),
                  (12, 33, 34)], "D"),
        # cream belly along the bottom edge
        ("runs", [(13, 13, 30), (14, 14, 34), (15, 15, 36),
                  (16, 16, 33)], "C"),
        # dark pectoral fin fan behind the gill, over the belly seam
        ("runs", [(9, 10, 15), (10, 9, 17), (11, 10, 17), (12, 11, 16),
                  (13, 12, 15)], "F"),
        ("runs", [(10, 11, 11), (10, 15, 15), (11, 13, 13),
                  (12, 14, 14)], "C", "F"),
        # slate tail fin with cream rays
        ("runs", [(1, 47, 49), (2, 45, 50), (3, 43, 51), (4, 42, 52),
                  (5, 41, 52), (6, 40, 51), (7, 39, 46), (8, 38, 43),
                  (9, 37, 41), (10, 36, 40), (11, 36, 39), (12, 36, 42),
                  (13, 37, 45), (14, 38, 47), (15, 39, 48), (16, 40, 49),
                  (17, 41, 49), (18, 43, 50), (19, 45, 49),
                  (20, 46, 48)], "F"),
        ("runs", [(3, 47, 47), (4, 47, 47), (5, 46, 46), (6, 45, 45),
                  (13, 41, 41), (14, 42, 42), (15, 44, 44),
                  (16, 45, 45), (17, 46, 46)], "C", "F"),
        # tail root shade
        ("runs", [(11, 36, 39), (12, 36, 37)], "D", "O"),
        # webbed leg fins, rear pair darker
        ("runs", [(17, 16, 19)], "O"),
        ("runs", [(18, 16, 18)], "O"),
        ("runs", [(17, 25, 28), (18, 26, 28)], "D", "O"),
        ("put", 19, 16, "W"),
        ("put", 19, 18, "W"),
        ("put", 19, 26, "W"),
        ("put", 19, 28, "W"),
    ],
}
