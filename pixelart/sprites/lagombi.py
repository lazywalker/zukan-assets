"""Lagombi, fanged beast. The snow rabbit: tall purple ears with pink
insides over a plump cream body, a blue carapace patch on the back, big
hind feet, sitting pose facing left."""

CONFIG = {
    "name": "lagombi",
    "size": (28, 24),
    "compare_to": "../icons/mhrise/lagombi.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (230, 222, 204, 255),   # cream fur
        "D": (190, 180, 160, 255),   # fur shade
        "P": (110, 85, 135, 255),    # purple ears / carapace
        "N": (225, 150, 170, 255),   # pink inner ear / nose
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        0:  [(8, 10), (13, 15)],               # ear tips
        1:  [(7, 11), (12, 16)],
        2:  [(7, 11), (12, 16)],
        3:  [(7, 11), (12, 16)],
        4:  [(6, 17)],
        5:  [(5, 18)],
        6:  [(4, 19)],
        7:  [(4, 20)],
        8:  [(4, 21)],
        9:  [(4, 21)],
        10: [(4, 22)],
        11: [(4, 22)],
        12: [(4, 22)],
        13: [(4, 22)],
        14: [(5, 21)],
        15: [(5, 21)],
        16: [(6, 20)],
        17: [(6, 20)],
        18: [(7, 19)],
        19: [(7, 11), (14, 19)],               # feet
        20: [(7, 11), (14, 19)],
        21: [(7, 7), (9, 9), (14, 14), (16, 16), (18, 18)],
    },
    "fills": [
        # purple ears with pink insides
        ("runs", [(0, 8, 10), (1, 7, 11), (2, 7, 11), (3, 7, 11)], "P"),
        ("runs", [(1, 8, 10), (2, 8, 10)], "N", "P"),
        ("runs", [(0, 13, 15), (1, 12, 16), (2, 12, 16), (3, 12, 16)],
         "P"),
        ("runs", [(1, 13, 15), (2, 13, 15)], "N", "P"),
        # eye on the face
        ("put", 7, 6, "K"),
        # pink nose at the snout tip
        ("put", 9, 4, "N"),
        # blue carapace patch on the back
        ("runs", [(9, 14, 21), (10, 14, 22), (11, 14, 22), (12, 14, 22)],
         "P"),
        # belly shade
        ("runs", [(13, 5, 11), (14, 6, 11), (15, 6, 11), (16, 7, 12)],
         "D"),
        # claws
        ("put", 21, 7, "W"),
        ("put", 21, 9, "W"),
        ("put", 21, 14, "W"),
        ("put", 21, 16, "W"),
        ("put", 21, 18, "W"),
    ],
}
