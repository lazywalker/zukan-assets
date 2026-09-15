"""Seltas Queen, neopteron. The armored tank, drawn in the head-on front
of its icon: a massive green dome with red spots, two dark mandible
horns curving up and out, orange eyes on the lower dome, a tan jaw rim
with pale mandibles, and a small striped body below."""

CONFIG = {
    "name": "seltas-queen",
    "size": (34, 24),
    "compare_to": "../icons/mh4u/seltas-queen.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (46, 96, 26, 255),      # green shell
        "D": (30, 66, 18, 255),      # dark green horns / shade
        "R": (160, 32, 28, 255),     # red spots
        "C": (190, 180, 110, 255),   # tan jaw rim
        "O": (240, 150, 50, 255),    # orange eyes
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        1:  [(10, 10), (23, 23)],                # horn tips
        2:  [(9, 11), (22, 24)],
        3:  [(8, 12), (21, 25)],
        4:  [(8, 12), (13, 20), (21, 25)],       # horns + dome top
        5:  [(7, 12), (12, 21), (21, 26)],
        6:  [(11, 22)],                          # dome
        7:  [(10, 23)],
        8:  [(10, 23)],
        9:  [(10, 23)],
        10: [(10, 23)],
        11: [(11, 22)],                          # eyes row
        12: [(12, 21)],                          # tan jaw rim
        13: [(14, 19)],                          # body
        14: [(14, 19)],
        15: [(13, 20)],                          # skirt
        16: [(12, 13), (15, 18), (20, 21)],      # legs
        17: [(12, 12), (16, 17), (21, 21)],      # tips
    },
    "fills": [
        # dark horns with pale inner edge
        ("runs", [(1, 10, 10), (2, 9, 11), (3, 8, 12), (4, 8, 12),
                  (5, 7, 12), (1, 23, 23), (2, 22, 24), (3, 21, 25),
                  (4, 21, 25), (5, 21, 26)], "D"),
        ("runs", [(2, 10, 11), (3, 10, 12), (4, 11, 12), (2, 22, 23),
                  (3, 21, 23), (4, 21, 22)], "G", "D"),
        # red spots across the dome
        ("runs", [(5, 15, 16), (5, 19, 20), (7, 12, 13), (7, 20, 21),
                  (9, 16, 17), (6, 18, 18)], "R"),
        # dome shading
        ("runs", [(6, 11, 11), (7, 10, 10), (8, 10, 10), (9, 10, 10),
                  (10, 10, 11), (6, 22, 22), (7, 23, 23), (8, 23, 23),
                  (9, 23, 23), (10, 22, 23), (11, 11, 11), (11, 22, 22)],
         "D"),
        # orange eyes with dark pupils
        ("runs", [(10, 12, 13), (10, 20, 21), (11, 12, 13), (11, 20, 21)],
         "O"),
        ("put", 10, 13, "K"),
        ("put", 10, 20, "K"),
        # tan jaw rim with pale mandibles
        ("runs", [(12, 12, 21)], "C"),
        ("put", 12, 15, "W"),
        ("put", 12, 18, "W"),
        # body stripes
        ("runs", [(13, 14, 19), (14, 14, 19)], "D"),
        ("runs", [(14, 15, 18)], "G", "D"),
        # dark legs with pale tips
        ("runs", [(16, 12, 13), (16, 20, 21), (17, 12, 12), (17, 21, 21)],
         "D"),
        ("put", 17, 12, "W"),
        ("put", 17, 21, "W"),
    ],
}
