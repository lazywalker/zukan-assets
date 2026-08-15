"""Tetranadon, amphibian. The sumo wrestler: a shaggy moss-green bulk with
a pale beaked face, a red eye, a huge round belly resting on thick legs,
and a shell plate on the back."""

CONFIG = {
    "name": "tetranadon",
    "size": (32, 24),
    "compare_to": "../icons/mhrise/tetranadon.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (110, 138, 82, 255),   # moss-green shaggy hide
        "D": (82, 108, 60, 255),    # darker green
        "C": (216, 200, 164, 255),  # pale belly / beak
        "R": (206, 68, 56, 255),    # red eye
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        3:  [(5, 8)],                         # head top
        4:  [(3, 10), (11, 12)],
        5:  [(2, 12), (11, 15)],
        6:  [(1, 13), (10, 17)],
        7:  [(1, 14), (9, 19)],
        8:  [(0, 15), (9, 21)],               # beak + back
        9:  [(0, 15), (8, 23)],
        10: [(0, 16), (8, 24)],
        11: [(0, 16), (8, 25)],
        12: [(0, 16), (8, 26)],               # belly mass
        13: [(0, 16), (8, 26)],
        14: [(1, 16), (8, 26)],
        15: [(1, 15), (9, 25)],
        16: [(2, 15), (10, 24)],
        17: [(3, 14), (12, 22)],
        18: [(4, 12), (14, 20)],              # legs
        19: [(4, 11), (15, 19)],
        20: [(4, 10), (16, 18)],
        21: [(4, 4), (6, 6), (10, 10), (16, 16), (18, 18)],
    },
    "fills": [
        # shaggy fur texture strokes
        ("runs", [(4, 4, 6), (5, 3, 5), (6, 3, 4), (7, 2, 4),
                  (8, 9, 14), (9, 10, 15)], "D"),
        # pale beak face
        ("runs", [(7, 1, 8), (8, 0, 8), (9, 0, 7)], "C"),
        # red eye
        ("put", 6, 5, "R"),
        # nostrils on the beak
        ("put", 8, 0, "K"),
        # shell plate on the back
        ("runs", [(10, 20, 24), (11, 19, 25), (12, 19, 26),
                  (13, 20, 26)], "D"),
        # huge pale belly
        ("runs", [(13, 2, 14), (14, 2, 14), (15, 2, 13), (16, 3, 12)],
         "C"),
        # claws
        ("put", 21, 4, "W"),
        ("put", 21, 6, "W"),
        ("put", 21, 10, "W"),
        ("put", 21, 16, "W"),
        ("put", 21, 18, "W"),
    ],
}
