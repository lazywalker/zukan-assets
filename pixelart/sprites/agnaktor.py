"""Agnaktor, flying wyvern. The lava armor lance, drawn in the plated
front of its icon: a wide armored head of dark red plates split by
glowing lava seams, a pale beak over a dark mouth line, yellow eyes set
in the plates, a lava-banded chest, and heavy columnar legs."""

CONFIG = {
    "name": "agnaktor",
    "size": (36, 24),
    "compare_to": "../icons/mh3u/agnaktor.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (200, 40, 30, 255),     # dark red plate
        "D": (130, 30, 26, 255),     # darker plate shade
        "O": (248, 140, 40, 255),    # glowing lava seams
        "C": (235, 195, 130, 255),   # sand beak / belly
        "E": (180, 140, 90, 255),    # dark sand shade
        "Y": (240, 200, 70, 255),    # eye yellow
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        2:  [(12, 23)],                          # crest plates
        3:  [(10, 25)],
        4:  [(9, 26)],
        5:  [(8, 27)],                           # head
        6:  [(8, 27)],
        7:  [(7, 28)],
        8:  [(7, 28)],
        9:  [(7, 28)],                           # beak row
        10: [(8, 27)],                           # jaw
        11: [(9, 26)],                           # chin
        12: [(8, 27)],                           # chest
        13: [(8, 27)],
        14: [(9, 26)],
        15: [(9, 26)],
        16: [(10, 25)],
        17: [(10, 25)],
        18: [(11, 13), (16, 19), (22, 24)],      # legs
        19: [(11, 13), (16, 19), (22, 24)],
        20: [(11, 13), (16, 19), (22, 24)],
        21: [(11, 11), (14, 14), (17, 18), (21, 21), (24, 24)],  # claws
    },
    "fills": [
        # glowing lava seams between the head plates
        ("runs", [(2, 16, 19), (3, 15, 16), (3, 19, 20), (4, 14, 15),
                  (4, 20, 21), (5, 13, 14), (5, 21, 22), (6, 13, 14),
                  (6, 21, 22), (7, 12, 13), (7, 22, 23), (8, 12, 13),
                  (8, 22, 23), (9, 12, 12), (9, 23, 23)], "O", "R"),
        # plate shading on the cheeks
        ("runs", [(5, 8, 10), (6, 8, 10), (7, 7, 9), (8, 7, 9),
                  (5, 25, 27), (6, 25, 27), (7, 26, 28), (8, 26, 28)],
         "D", "R"),
        # sand beak over the dark mouth line
        ("runs", [(9, 10, 25)], "C", "R"),
        ("runs", [(9, 13, 15), (9, 20, 22)], "E", "C"),
        ("runs", [(10, 11, 24)], "K", "R"),
        # yellow eyes set in the plates
        ("runs", [(7, 14, 16), (7, 19, 21)], "Y", "R"),
        ("put", 7, 15, "K"),
        ("put", 7, 20, "K"),
        # sand chest bands with lava between
        ("runs", [(12, 10, 25), (13, 10, 25)], "C", "R"),
        ("runs", [(12, 14, 15), (12, 20, 21), (13, 12, 13), (13, 22, 23)],
         "O", "C"),
        ("runs", [(14, 11, 24), (15, 11, 24)], "D", "R"),
        ("runs", [(15, 14, 21)], "O", "D"),
        # dark legs with pale claws
        ("runs", [(18, 11, 13), (18, 22, 24), (19, 11, 13), (19, 22, 24),
                  (20, 11, 13), (20, 22, 24), (18, 16, 19), (19, 16, 19),
                  (20, 16, 19)], "D"),
        ("runs", [(21, 11, 11), (21, 14, 14), (21, 21, 21), (21, 24, 24)],
         "C", "R"),
        ("runs", [(21, 17, 18)], "C", "R"),
    ],
}
