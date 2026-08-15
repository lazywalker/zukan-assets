"""Akantor, flying wyvern. The black fang: an orange-black tank wyvern
with a spiky mane ridge, giant tusked jaws, and huge clawed forelimbs."""

CONFIG = {
    "name": "akantor",
    "size": (36, 24),
    "compare_to": "../icons/mh4u/akantor.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "O": (198, 122, 56, 255),   # orange-black hide
        "D": (150, 90, 40, 255),    # darker hide
        "N": (48, 42, 46, 255),     # near-black mane / claws
        "C": (226, 202, 156, 255),  # pale tusks
        "W": (246, 242, 230, 255),
    },
    "base": "O",
    "spans": {
        2:  [(5, 7), (10, 11)],               # mane spikes
        3:  [(3, 12), (9, 13)],
        4:  [(2, 13), (8, 15)],
        5:  [(1, 14), (8, 17)],
        6:  [(1, 15), (7, 19)],
        7:  [(0, 16), (7, 21)],
        8:  [(0, 16), (6, 22)],               # jaw zone
        9:  [(0, 16), (6, 23)],
        10: [(0, 16), (6, 24)],
        11: [(0, 16), (6, 24)],
        12: [(0, 16), (6, 24)],
        13: [(0, 16), (6, 24)],
        14: [(0, 16), (6, 24)],
        15: [(0, 16), (6, 24)],
        16: [(1, 16), (6, 24)],
        17: [(1, 16), (6, 24)],
        18: [(1, 16), (6, 24)],
        19: [(1, 16), (6, 24)],
        20: [(2, 16), (6, 24)],
        21: [(3, 9), (11, 14), (17, 20), (23, 24)],  # legs
        22: [(3, 8), (12, 13), (18, 19), (24, 24)],
        23: [(3, 3), (5, 5), (12, 12), (18, 18), (24, 24)],
    },
    "fills": [
        # near-black mane spikes over the head
        ("runs", [(2, 5, 7), (2, 10, 11), (3, 3, 6), (3, 9, 13),
                  (4, 8, 12), (5, 8, 10)], "N"),
        # pale eye
        ("put", 6, 4, "W"),
        # giant pale tusks from the lower jaw
        ("runs", [(8, 0, 2), (9, 0, 3), (10, 0, 3)], "C"),
        ("runs", [(8, 6, 8), (9, 6, 8), (10, 5, 7)], "C"),
        # dark mouth gap
        ("runs", [(8, 3, 5), (9, 4, 5)], "K"),
        # near-black claws
        ("runs", [(21, 3, 9), (21, 11, 14), (21, 17, 20),
                  (21, 23, 24)], "N"),
        # body shade along the bottom
        ("runs", [(18, 2, 16), (19, 2, 16), (20, 3, 16)], "D"),
    ],
}
