"""Lao-Shan Lung, elder dragon. The walking mountain: a colossal slab of
a body at near-constant height with a gold ridge hugging the top edge, a
small dark head at the front with TWO pale horns arcing back over the
shell, a rounded rear with a stub tail, columnar legs. The horn arc and
the slab silhouette are the signature."""

CONFIG = {
    "name": "lao-shan-lung",
    "size": (40, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (152, 112, 78, 255),   # brown carapace
        "D": (116, 82, 56, 255),    # darker shell
        "C": (214, 198, 166, 255),  # pale horns / jaw / under-plate
        "Y": (222, 178, 84, 255),   # gold ridge
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(8, 11)],                    # near horn tip
        4:  [(6, 11), (15, 18)],          # near horn + far horn tip
        5:  [(5, 11), (14, 19)],          # horns arcing back
        6:  [(4, 12), (13, 20)],          # horn roots + shell top
        7:  [(3, 23)],                    # shell top edge
        8:  [(2, 9), (7, 26)],            # head at the front + shell
        9:  [(2, 30)],
        10: [(2, 34)],
        11: [(1, 36)],
        12: [(1, 37), (38, 39)],          # tail stub
        13: [(1, 37), (38, 39)],
        14: [(1, 37)],
        15: [(1, 37)],
        16: [(1, 37)],
        17: [(1, 37)],
        18: [(2, 36)],
        19: [(3, 36)],
        20: [(4, 35)],
        21: [(7, 11), (17, 21), (27, 31), (34, 37)],   # columnar legs
        22: [(7, 10), (18, 20), (28, 30), (35, 36)],
    },
    "fills": [
        # gold ridge hugging the top edge of the shell
        ("runs", [(7, 12, 23), (8, 11, 26), (9, 11, 30), (10, 11, 34)],
         "Y"),
        # the two pale horns arcing back over the ridge
        ("runs", [(3, 8, 11), (4, 6, 11), (5, 5, 10), (6, 4, 10)], "C"),
        ("runs", [(4, 15, 18), (5, 14, 19), (6, 13, 18)], "C"),
        # dark head at the front under the horn arc
        ("runs", [(8, 2, 7), (9, 2, 6), (10, 2, 6)], "D"),
        ("put", 9, 4, "W"),
        ("runs", [(10, 2, 6), (11, 2, 5)], "C"),
        # shell plate seams
        ("runs", [(13, 16, 17), (15, 24, 25), (17, 30, 31)], "D", "B"),
        # pale under-plate along the bottom edge
        ("runs", [(18, 3, 36), (19, 4, 35), (20, 5, 34)], "C"),
        # legs darker
        ("runs", [(21, 17, 21), (21, 27, 31), (22, 18, 20),
                  (22, 28, 30)], "D"),
        # claws
        ("put", 22, 7, "W"),
        ("put", 22, 28, "W"),
    ],
}
