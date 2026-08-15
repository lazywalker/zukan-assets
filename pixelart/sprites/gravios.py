"""Gravios, flying wyvern. The stone tank: a tall shell dome with the
folded wing-arm shelf behind, a blunt wedge face low at the front with a
beam-breath mouth notch opening through the silhouette edge, thick column
legs, pale face and chest. The gravios archetype its variants derive from."""

CONFIG = {
    "name": "gravios",
    "size": (32, 24),
    "compare_to": "../icons/mh4u/gravios.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (146, 140, 128, 255),  # grey stone hide
        "D": (112, 106, 96, 255),   # darker stone
        "C": (196, 186, 168, 255),  # pale face / chest
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(11, 16)],                   # dome top
        4:  [(9, 18), (21, 22)],          # dome + wing-arm tip
        5:  [(8, 20), (20, 24)],          # dome + wing arm
        6:  [(7, 25)],
        7:  [(6, 26)],
        8:  [(5, 27)],
        9:  [(4, 27)],
        10: [(0, 27)],
        11: [(0, 27)],
        12: [(0, 27)],
        13: [(3, 27)],                    # mouth notch open at the left
        14: [(3, 27)],
        15: [(0, 26)],                    # chin under the notch
        16: [(1, 25)],
        17: [(3, 24)],
        18: [(5, 24)],
        19: [(8, 12), (16, 20)],          # legs
        20: [(8, 11), (16, 19)],
        21: [(8, 8), (10, 10), (16, 16), (18, 18)],
    },
    "fills": [
        # shell plates on the dome
        ("runs", [(4, 10, 15), (5, 9, 14), (6, 8, 13), (7, 7, 12)],
         "D", "G"),
        # wing-arm shelf darker where it folds behind the dome
        ("runs", [(4, 21, 22), (5, 21, 24), (6, 22, 25)], "D"),
        # pale face panel on the head front
        ("runs", [(10, 0, 4), (11, 0, 4), (12, 0, 4), (15, 0, 4)], "C"),
        # brow + eye
        ("put", 9, 5, "D"),
        ("put", 10, 5, "K"),
        # teeth on the jaw faces around the mouth notch
        ("put", 12, 0, "W"),
        ("put", 12, 2, "W"),
        ("put", 15, 0, "W"),
        ("put", 15, 2, "W"),
        # pale chest along the lower front
        ("runs", [(16, 2, 10), (17, 4, 11)], "C"),
        # boulder shade on the underside
        ("runs", [(16, 18, 24), (17, 17, 23), (18, 15, 23)], "D"),
        # claws
        ("put", 21, 8, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 16, "W"),
        ("put", 21, 18, "W"),
    ],
}
