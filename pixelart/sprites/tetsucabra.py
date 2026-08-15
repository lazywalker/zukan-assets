"""Tetsucabra, amphibian. The tusked toad: a plump orange body crouched on
thick legs, a huge wide jaw with white tusks jutting up from the lower
jaw, and warty spikes over the brow. The toad archetype the deviants
derive from."""

CONFIG = {
    "name": "tetsucabra",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/tetsucabra.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (206, 118, 60, 255),   # orange hide
        "D": (158, 86, 44, 255),    # darker shade
        "C": (228, 190, 140, 255),  # pale jaw / belly
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        4:  [(6, 8), (11, 12)],               # brow spikes
        5:  [(4, 14)],
        6:  [(3, 16)],
        7:  [(2, 17)],
        8:  [(1, 18)],
        9:  [(1, 18), (19, 20)],              # jaw + back spikes
        10: [(0, 18), (18, 21)],
        11: [(0, 18), (17, 22)],
        12: [(0, 17), (17, 23)],
        13: [(1, 17), (16, 23)],
        14: [(1, 16), (16, 23)],
        15: [(2, 15), (17, 23)],
        16: [(3, 14), (18, 22)],
        17: [(5, 8), (11, 13), (19, 21)],     # legs
        18: [(5, 7), (10, 12), (19, 20)],
        19: [(5, 5), (7, 7), (10, 10), (12, 12), (19, 19), (21, 21)],
    },
    "fills": [
        # warty brow spikes
        ("runs", [(4, 6, 8), (4, 11, 12), (5, 12, 14)], "D"),
        # huge pale jaw band
        ("runs", [(9, 0, 18), (10, 0, 17)], "C"),
        # mouth line with white tusks jutting up
        ("runs", [(9, 2, 14)], "K"),
        ("put", 9, 3, "W"),
        ("put", 9, 6, "W"),
        ("put", 9, 9, "W"),
        ("put", 9, 12, "W"),
        # small eye under the brow
        ("put", 6, 5, "K"),
        # pale belly
        ("runs", [(13, 2, 15), (14, 2, 15), (15, 3, 14)], "C"),
        # back shade
        ("runs", [(8, 12, 18), (9, 19, 20), (10, 18, 21)], "D"),
        # claws
        ("put", 19, 5, "W"),
        ("put", 19, 7, "W"),
        ("put", 19, 10, "W"),
        ("put", 19, 12, "W"),
        ("put", 19, 19, "W"),
        ("put", 19, 21, "W"),
    ],
}
