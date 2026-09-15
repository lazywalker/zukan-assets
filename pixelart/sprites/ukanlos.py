"""Ukanlos, flying wyvern. The shovel jaw, drawn head-on like its icon: a
pale grey-white tank with a huge spade jaw spanning the full width, its
corners upturned, a dark mouth gap with white teeth, small sunk eyes
high on the skull under a blue-grey back dome, and a chin spike."""

CONFIG = {
    "name": "ukanlos",
    "size": (36, 24),
    "compare_to": "../icons/mh4u/ukanlos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "W": (238, 242, 244, 255),   # pale grey-white hide
        "B": (135, 170, 205, 255),   # blue-grey back dome
        "D": (90, 115, 150, 255),    # dark blue-grey shade
        "E": (50, 40, 44, 255),      # dark mouth
        "O": (230, 140, 50, 255),    # eye orange
        "C": (190, 210, 228, 255),   # pale shade
    },
    "base": "W",
    "spans": {
        2:  [(13, 22)],                          # back dome
        3:  [(11, 24)],
        4:  [(9, 26)],
        5:  [(7, 28)],
        6:  [(6, 29)],                           # skull
        7:  [(5, 30)],
        8:  [(5, 30)],
        9:  [(4, 31)],
        10: [(2, 33)],                           # jaw corners rising
        11: [(1, 34)],
        12: [(1, 34)],                           # spade jaw full width
        13: [(0, 35)],
        14: [(0, 35)],
        15: [(1, 34)],                           # jaw bottom
        16: [(2, 33)],
        17: [(3, 32)],                           # chin
        18: [(4, 31)],
        19: [(6, 29)],
        20: [(16, 19)],                          # chin spike
    },
    "fills": [
        # blue-grey back dome with dark shade
        ("runs", [(2, 13, 22), (3, 11, 24), (4, 9, 26), (5, 7, 28),
                  (6, 6, 29), (7, 5, 30)], "B"),
        ("runs", [(4, 9, 12), (5, 7, 10), (6, 6, 9), (7, 5, 8),
                  (4, 23, 26), (5, 25, 28), (6, 26, 29), (7, 27, 30)],
         "D", "B"),
        # small sunk orange eyes high on the skull
        ("runs", [(7, 13, 14), (7, 21, 22)], "O", "B"),
        ("put", 7, 14, "K"),
        ("put", 7, 21, "K"),
        # pale shading down the skull sides
        ("runs", [(8, 5, 8), (9, 4, 7), (8, 27, 30), (9, 28, 31)],
         "C", "W"),
        # dark mouth gap with white teeth rows
        ("runs", [(11, 6, 29), (12, 6, 29), (13, 7, 28), (14, 7, 28)],
         "E"),
        ("runs", [(11, 8, 9), (11, 13, 14), (11, 18, 19), (11, 23, 24),
                  (11, 26, 27), (13, 9, 10),
                  (13, 15, 16), (13, 21, 22), (13, 26, 27)], "W", "E"),
        # jaw under-shading and chin spike
        ("runs", [(15, 3, 10), (15, 25, 32), (16, 4, 12), (16, 23, 31),
                  (17, 5, 12), (17, 23, 30), (18, 6, 13), (18, 22, 29)],
         "C", "W"),
        ("runs", [(19, 8, 27), (20, 16, 19)], "D", "W"),
    ],
}
