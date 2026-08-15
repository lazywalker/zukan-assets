"""Apceros, herbivore. The shelled grazer: a domed brown shell with pale
spikes over a cream body, a frilled little head at the left, and a spiked
tail club dragging behind. The armored-herbivore archetype rhenoplos
derives from."""

CONFIG = {
    "name": "apceros",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/apceros.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (152, 92, 58, 255),    # brown shell
        "D": (116, 66, 42, 255),    # darker shell
        "C": (208, 182, 150, 255),  # cream body
        "S": (228, 210, 178, 255),  # pale spikes
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        3:  [(8, 10), (15, 16)],              # shell spike tips
        4:  [(6, 12), (14, 18)],
        5:  [(5, 19)],
        6:  [(4, 21), (22, 23)],              # shell + tail spike
        7:  [(3, 23), (22, 25)],
        8:  [(2, 24), (21, 26)],
        9:  [(1, 25), (20, 27)],
        10: [(1, 26), (19, 28)],
        11: [(2, 27), (18, 28)],
        12: [(2, 27), (17, 29)],
        13: [(3, 26), (17, 29)],
        14: [(4, 25), (18, 29)],
        15: [(5, 24), (19, 29)],
        16: [(6, 23), (20, 29)],              # tail club
        17: [(7, 11), (14, 17), (21, 28)],
        18: [(7, 10), (15, 16), (22, 27)],
        19: [(7, 7), (9, 9), (15, 15), (24, 24), (26, 26)],
    },
    "fills": [
        # pale shell spikes
        ("runs", [(3, 8, 10), (3, 15, 16), (4, 6, 7), (4, 11, 12),
                  (4, 17, 18), (6, 22, 23), (7, 22, 23)], "S"),
        # shell scute lines
        ("runs", [(6, 8, 9), (7, 11, 12), (8, 10, 11), (9, 13, 14),
                  (10, 12, 13), (11, 15, 16), (12, 14, 15)], "D", "R"),
        # cream head under the shell front
        ("runs", [(9, 1, 6), (10, 1, 7), (11, 2, 7)], "C"),
        # eye + beak
        ("put", 10, 3, "K"),
        ("put", 9, 1, "D"),
        # cream legs
        ("runs", [(17, 7, 11), (17, 14, 17)], "C"),
        # tail club spikes
        ("runs", [(15, 27, 29), (16, 26, 29), (17, 27, 28)], "S"),
        # claws
        ("put", 19, 7, "W"),
        ("put", 19, 9, "W"),
        ("put", 19, 15, "W"),
    ],
}
