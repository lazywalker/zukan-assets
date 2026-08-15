"""Seltas, neopteron. The horned beetle: a green armored body with a big
orange-tipped horn jutting forward, a blue-grey wing shell over the back,
and spiky legs. The beetle archetype the queens derive from."""

CONFIG = {
    "name": "seltas",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/seltas.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (108, 148, 92, 255),   # green armor
        "D": (78, 112, 66, 255),    # darker green
        "O": (222, 146, 62, 255),   # orange horn
        "S": (150, 162, 178, 255),  # blue-grey wing shell
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(3, 7)],                         # horn tip
        4:  [(2, 9), (14, 16)],               # horn + wing shell tip
        5:  [(1, 11), (13, 18)],
        6:  [(1, 12), (12, 20)],
        7:  [(1, 13), (11, 22)],
        8:  [(1, 14), (10, 23)],
        9:  [(2, 15), (10, 24)],
        10: [(2, 16), (10, 24)],
        11: [(3, 16), (11, 23)],
        12: [(3, 15), (12, 22)],
        13: [(4, 14), (13, 21)],
        14: [(5, 13), (15, 20)],
        15: [(6, 12), (17, 18)],
        16: [(6, 9), (11, 14), (16, 18)],     # legs
        17: [(6, 8), (10, 10), (13, 13), (17, 17)],
    },
    "fills": [
        # big orange horn with a dark tip
        ("runs", [(3, 3, 7), (4, 2, 9), (5, 1, 8), (6, 1, 6)], "O"),
        ("runs", [(3, 3, 4)], "D", "O"),
        # eye on the head
        ("put", 7, 3, "W"),
        ("put", 7, 4, "K"),
        # blue-grey wing shell over the back
        ("runs", [(4, 14, 16), (5, 13, 18), (6, 12, 20), (7, 11, 21),
                  (8, 10, 21)], "S"),
        # shell ridge lines
        ("runs", [(6, 16, 16), (7, 16, 16), (8, 15, 15)], "D", "S"),
        # dark underside
        ("runs", [(13, 6, 13), (14, 7, 12), (15, 8, 11)], "D"),
        # spiky legs
        ("runs", [(16, 6, 9), (16, 11, 14), (16, 16, 18)], "D"),
        # claws
        ("put", 17, 6, "W"),
        ("put", 17, 8, "W"),
        ("put", 17, 10, "W"),
        ("put", 17, 13, "W"),
        ("put", 17, 17, "W"),
    ],
}
