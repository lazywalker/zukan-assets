"""Vespoid, neopteron. The wasp, drawn in the front pose of its icon:
magenta eyes and white mandibles on the head, four pale wing lobes
spread in a fan with pink veins, a banded abdomen hanging to a dark
sting, and thin legs. The wasp archetype the other small neopterons
derive from."""

CONFIG = {
    "name": "vespoid",
    "size": (26, 24),
    "compare_to": "../icons/mhwilds/vespoid.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (232, 140, 40, 255),    # orange body
        "D": (180, 100, 32, 255),    # darker shade / bands
        "Y": (240, 220, 70, 255),    # yellow bands
        "P": (214, 50, 140, 255),    # magenta eyes / wing veins
        "C": (246, 236, 180, 255),   # pale wing cells
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        1:  [(9, 9), (16, 16)],                        # antennae
        2:  [(4, 5), (8, 8), (10, 15), (17, 17), (20, 21)],   # wing + head
        3:  [(3, 5), (9, 16), (20, 22)],
        4:  [(2, 6), (8, 17), (19, 23)],
        5:  [(2, 6), (8, 17), (19, 23)],
        6:  [(2, 6), (8, 17), (19, 23)],
        7:  [(1, 5), (8, 17), (20, 24)],               # thorax
        8:  [(1, 5), (8, 17), (20, 24)],
        9:  [(2, 5), (9, 16), (20, 23)],
        10: [(3, 4), (10, 15), (21, 22)],              # abdomen top
        11: [(10, 15)],
        12: [(6, 6), (8, 8), (10, 15), (17, 17), (19, 19)],   # legs
        13: [(6, 6), (8, 8), (10, 15), (17, 17), (19, 19)],
        14: [(6, 6), (8, 8), (10, 15), (17, 17), (19, 19)],
        15: [(11, 14)],
        16: [(11, 14)],
        17: [(12, 13)],
        18: [(12, 13)],                                # sting
    },
    "fills": [
        # pale wing lobes with pink tips and outer veins
        ("runs", [(2, 4, 5), (3, 3, 5), (4, 2, 6), (5, 2, 6), (6, 2, 6),
                  (7, 1, 5), (8, 1, 5), (9, 2, 5), (10, 3, 4), (2, 20, 21),
                  (3, 20, 22), (4, 19, 23), (5, 19, 23), (6, 19, 23),
                  (7, 20, 24), (8, 20, 24), (9, 20, 23), (10, 21, 22)],
         "C"),
        ("runs", [(2, 4, 5), (10, 3, 4), (2, 20, 21), (10, 21, 22)],
         "P", "C"),
        ("runs", [(4, 2, 2), (5, 2, 2), (6, 2, 2), (7, 1, 1), (8, 1, 1),
                  (4, 23, 23), (5, 23, 23), (6, 23, 23), (7, 24, 24),
                  (8, 24, 24)], "P", "C"),
        # magenta eyes with dark pupils
        ("runs", [(4, 9, 10), (4, 15, 16), (5, 9, 10), (5, 15, 16)], "P"),
        ("put", 5, 10, "K"),
        ("put", 5, 15, "K"),
        # white mandibles around a dark mouth gap
        ("runs", [(6, 12, 13), (7, 12, 13)], "D"),
        ("put", 6, 11, "W"),
        ("put", 6, 14, "W"),
        ("put", 7, 11, "W"),
        ("put", 7, 14, "W"),
        # dark thorax sides
        ("runs", [(7, 8, 8), (8, 8, 8), (9, 9, 9), (10, 10, 10),
                  (11, 10, 10), (7, 17, 17), (8, 17, 17), (9, 16, 16),
                  (10, 15, 15), (11, 15, 15)], "D"),
        # yellow and dark bands down the abdomen
        ("runs", [(13, 10, 15), (14, 10, 15)], "Y"),
        ("runs", [(15, 11, 14), (16, 11, 14)], "D"),
        # dark sting
        ("runs", [(17, 12, 13), (18, 12, 13)], "K"),
        # dark legs with pale feet
        ("runs", [(1, 9, 9), (1, 16, 16), (2, 8, 8), (2, 17, 17)], "D"),
        ("runs", [(12, 6, 6), (12, 8, 8), (13, 6, 6), (13, 8, 8),
                  (14, 6, 6), (14, 8, 8)], "D"),
        ("put", 14, 6, "W"),
        ("put", 14, 8, "W"),
        ("put", 14, 17, "W"),
        ("put", 14, 19, "W"),
    ],
}
