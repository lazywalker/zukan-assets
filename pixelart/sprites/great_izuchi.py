"""Great Izuchi, bird wyvern leader. Sickle-crest variant: gray-green
scales, a large bone-colored scythe blade rising from the head, blade
spikes along the tail. The oversized head blade is the signature."""

CONFIG = {
    "name": "great-izuchi",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/great-izuchi.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (150, 160, 140, 255),  # gray-green scales
        "C": (190, 200, 180, 255),  # pale underbelly
        "H": (210, 205, 185, 255),  # bone: sickle crest
        "D": (110, 120, 100, 255),  # darker: spots, shade
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        1:  [(9, 13)],
        2:  [(8, 14)],
        3:  [(7, 14)],
        4:  [(6, 13)],
        5:  [(5, 12)],
        6:  [(1, 12), (31, 32)],
        7:  [(1, 12), (30, 33)],
        8:  [(2, 11), (29, 33)],
        9:  [(3, 12), (13, 25), (29, 32)],
        10: [(5, 13), (14, 26), (28, 31)],
        11: [(6, 14), (15, 27), (30, 30)],
        12: [(6, 14), (16, 28)],
        13: [(7, 14), (17, 29)],
        14: [(7, 29)],
        15: [(8, 28)],
        16: [(9, 25)],
        17: [(10, 13), (14, 17), (18, 24)],
        18: [(10, 13), (18, 24)],
        19: [(10, 13), (18, 23)],
        20: [(10, 13), (18, 22)],
        21: [(10, 10), (12, 12), (18, 18), (20, 20)],
    },
    "fills": [
        # oversized sickle crest, bone colored
        ("runs", [(1, 9, 13), (2, 8, 14), (3, 7, 14), (4, 6, 13)], "H"),
        ("runs", [(3, 12, 13), (4, 11, 12)], "D"),
        # beak
        ("runs", [(6, 1, 3), (7, 1, 3)], "C"),
        ("runs", [(8, 2, 3)], "D"),
        ("put", 7, 5, "W"),
        # dark spots
        ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22)], "D"),
        # cream underbelly
        ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)], "C"),
        # tail blade spikes
        ("runs", [(9, 24, 25), (10, 26, 27), (11, 27, 28)], "H"),
        ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
         "D"),
        ("put", 21, 10, "W"),
        ("put", 21, 12, "W"),
        ("put", 21, 18, "W"),
        ("put", 21, 20, "W"),
    ],
}
