"""Tetranadon, amphibian. The sumo wrestler, drawn in the belly-front of
its icon: a shaggy moss-green shell dome with a seaweed strand, a pale
beaked face with red eyes, a huge pale belly resting on thick legs."""

CONFIG = {
    "name": "tetranadon",
    "size": (32, 24),
    "compare_to": "../icons/mhrise/tetranadon.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (110, 140, 70, 255),    # moss green shell
        "M": (80, 110, 50, 255),     # dark moss shade
        "D": (60, 85, 40, 255),      # darkest green
        "C": (220, 200, 160, 255),   # pale belly / beak
        "E": (60, 40, 30, 255),      # dark beak line
        "R": (200, 60, 50, 255),     # red eyes
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        1:  [(15, 16)],                          # seaweed strand
        2:  [(14, 17)],
        3:  [(12, 19)],                          # shell top
        4:  [(10, 21)],
        5:  [(9, 22)],
        6:  [(8, 23)],
        7:  [(7, 24)],
        8:  [(7, 24), (11, 20)],                 # shell + face top
        9:  [(6, 25), (11, 20)],
        10: [(6, 25), (11, 20)],
        11: [(6, 25), (11, 20)],
        12: [(6, 25)],                           # face base
        13: [(6, 25)],
        14: [(7, 24)],                           # belly
        15: [(7, 24)],
        16: [(8, 23)],
        17: [(8, 23)],
        18: [(9, 22)],
        19: [(9, 13), (15, 16), (18, 22)],       # legs
        20: [(9, 13), (15, 16), (18, 22)],
        21: [(9, 12), (15, 16), (19, 22)],
    },
    "fills": [
        # seaweed strand on the shell top
        ("runs", [(1, 15, 16), (2, 14, 17)], "M", "G"),
        # shaggy moss dome with dark patches
        ("runs", [(3, 12, 19), (4, 10, 21), (5, 9, 22), (6, 8, 23),
                  (7, 7, 24)], "G"),
        ("runs", [(4, 12, 14), (5, 10, 12), (6, 9, 10), (4, 17, 19),
                  (5, 19, 21), (6, 21, 23), (7, 8, 10), (7, 21, 23)],
         "M", "G"),
        # pale beaked face with red eyes
        ("runs", [(8, 12, 19), (9, 12, 19), (10, 12, 19), (11, 12, 19)],
         "C"),
        ("runs", [(9, 12, 13), (9, 18, 19), (10, 12, 13), (10, 18, 19)],
         "R", "C"),
        ("put", 9, 13, "K"),
        ("put", 9, 18, "K"),
        # dark beak line
        ("runs", [(11, 14, 17)], "E", "C"),
        ("put", 11, 13, "E"),
        ("put", 11, 18, "E"),
        # huge pale belly
        ("runs", [(13, 9, 22), (14, 9, 22), (15, 9, 22), (16, 10, 21),
                  (17, 10, 21), (18, 11, 20)], "C"),
        ("runs", [(15, 13, 14), (15, 17, 18), (16, 13, 14), (16, 17, 18)],
         "E", "C"),
        # thick dark legs with pale claws
        ("runs", [(19, 9, 13), (19, 18, 22), (20, 9, 13), (20, 18, 22),
                  (21, 9, 12), (21, 19, 22), (19, 15, 16), (20, 15, 16)],
         "D"),
        ("put", 21, 10, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 21, "W"),
    ],
}
