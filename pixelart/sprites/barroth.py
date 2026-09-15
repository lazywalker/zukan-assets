"""Barroth, brute wyvern. The mud-clay hammerhead, drawn head-on under
its crown: a huge flat clay crown ridge with dark groove seams, tiny
eyes sunk under the crown brim, a wide flat mouth gap with blunt teeth
in a pale rim, a stocky clay body and thick columnar forelegs."""

CONFIG = {
    "name": "barroth",
    "size": (36, 24),
    "compare_to": "../icons/mhrise/barroth.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (145, 120, 90, 255),    # grey clay crown
        "Y": (205, 165, 85, 255),    # yellow clay body
        "D": (150, 115, 60, 255),    # dark clay shade
        "E": (60, 35, 25, 255),      # dark mouth
        "C": (230, 210, 170, 255),   # pale rim
        "W": (246, 242, 230, 255),
    },
    "base": "Y",
    "spans": {
        2:  [(13, 22)],                          # crown top
        3:  [(11, 24)],
        4:  [(10, 25)],
        5:  [(9, 26)],
        6:  [(8, 27)],
        7:  [(8, 27)],
        8:  [(7, 28)],                           # crown brim
        9:  [(7, 28)],
        10: [(8, 27)],                           # face under the brim
        11: [(8, 27)],
        12: [(9, 26)],                           # mouth row
        13: [(9, 26)],
        14: [(10, 25)],                          # chin
        15: [(8, 27)],                           # shoulders
        16: [(7, 28)],
        17: [(7, 28)],
        18: [(8, 27)],
        19: [(8, 11), (13, 22), (24, 27)],       # legs
        20: [(8, 11), (13, 22), (24, 27)],
        21: [(8, 11), (13, 22), (24, 27)],
    },
    "fills": [
        # grey clay crown with dark groove seams
        ("runs", [(2, 13, 22), (3, 11, 24), (4, 10, 25), (5, 9, 26),
                  (6, 8, 27), (7, 8, 27), (8, 7, 28), (9, 7, 28)], "B"),
        ("runs", [(2, 16, 19), (3, 15, 16), (3, 19, 20), (4, 14, 15),
                  (4, 20, 21), (5, 13, 14), (5, 21, 22), (6, 12, 13),
                  (6, 22, 23), (7, 12, 13), (7, 22, 23), (8, 11, 12),
                  (8, 23, 24), (9, 11, 12), (9, 23, 24)], "D", "B"),
        # crown brim shading over the eyes
        ("runs", [(9, 9, 12), (9, 23, 26), (10, 9, 12), (10, 23, 26)],
         "D", "B"),
        # tiny sunk eyes under the brim
        ("put", 11, 12, "K"),
        ("put", 11, 23, "K"),
        # wide flat mouth gap with blunt teeth in a pale rim
        ("runs", [(12, 11, 24), (13, 11, 24)], "E"),
        ("runs", [(12, 12, 13), (12, 17, 18), (12, 22, 23), (13, 14, 15),
                  (13, 19, 21)], "W", "E"),
        ("runs", [(13, 10, 11), (13, 24, 25), (14, 11, 24)], "C", "Y"),
        # clay body shading
        ("runs", [(15, 8, 12), (15, 23, 27), (16, 7, 11), (16, 24, 28),
                  (17, 7, 11), (17, 24, 28), (18, 8, 12), (18, 23, 27)],
         "D", "Y"),
        ("runs", [(16, 14, 21), (17, 14, 21)], "C", "Y"),
        # thick dark legs with pale claws
        ("runs", [(19, 8, 11), (19, 24, 27), (20, 8, 11), (20, 24, 27),
                  (21, 8, 11), (21, 24, 27), (19, 13, 22), (20, 13, 22),
                  (21, 13, 22)], "D"),
        ("put", 21, 9, "W"),
        ("put", 21, 13, "W"),
        ("put", 21, 22, "W"),
        ("put", 21, 26, "W"),
    ],
}
