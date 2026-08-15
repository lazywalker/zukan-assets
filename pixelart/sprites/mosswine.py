"""Mosswine, herbivore. The moss-backed pig: low brown body, a big pale
plate over the forehead, a snout with a white tusk, and a patch of moss
growing along the back."""

CONFIG = {
    "name": "mosswine",
    "size": (26, 24),
    "compare_to": "../icons/mhfu/mosswine.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (152, 102, 66, 255),   # brown hide
        "D": (116, 74, 48, 255),    # darker shade
        "P": (222, 206, 180, 255),  # pale forehead plate
        "M": (104, 142, 72, 255),   # moss patch
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        5:  [(6, 12)],                        # forehead plate top
        6:  [(4, 14)],
        7:  [(3, 15), (15, 16)],
        8:  [(2, 16), (14, 19)],              # head + back
        9:  [(0, 17), (13, 21)],              # snout extends left
        10: [(0, 18), (13, 22)],              # tusk bump col 0
        11: [(1, 18), (14, 23)],
        12: [(2, 18), (15, 24)],
        13: [(2, 17), (16, 24)],
        14: [(3, 16), (18, 24)],
        15: [(4, 15), (20, 24)],
        16: [(5, 11), (15, 18), (21, 23)],    # legs
        17: [(5, 10), (16, 17), (22, 22)],
        18: [(5, 5), (7, 7), (16, 16), (18, 18), (22, 22)],
    },
    "fills": [
        # pale forehead plate
        ("runs", [(5, 6, 12), (6, 4, 13), (7, 3, 9)], "P"),
        # plate speckles
        ("runs", [(6, 7, 7), (6, 10, 10)], "D", "P"),
        # snout + tusk
        ("runs", [(9, 0, 2)], "D"),
        ("put", 10, 0, "W"),
        # small dark eye
        ("put", 7, 5, "K"),
        # moss patch along the back
        ("runs", [(8, 14, 18), (9, 14, 18), (10, 14, 17), (11, 15, 17)],
         "M"),
        # belly shade
        ("runs", [(13, 3, 14), (14, 4, 13), (15, 5, 12)], "D"),
        # claws
        ("put", 18, 5, "W"),
        ("put", 18, 7, "W"),
        ("put", 18, 16, "W"),
        ("put", 18, 18, "W"),
        ("put", 18, 22, "W"),
    ],
}
