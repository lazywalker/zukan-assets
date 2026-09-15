"""Ahtal-Ka, neopteron elder. The golden pharaoh mantis, drawn in the
throne-spread front of its icon: a huge ornate gold wing fan with blue
trim and purple silk strands, a small gold face with green eyes between
red mandible hooks, folded forearms and splayed rear legs."""

CONFIG = {
    "name": "ahtal-ka",
    "size": (34, 24),
    "compare_to": "../icons/mhgu/ahtal-ka.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (236, 180, 44, 255),    # gold
        "E": (186, 132, 30, 255),    # dark gold pattern
        "B": (64, 90, 220, 255),     # blue trim
        "P": (178, 60, 200, 255),    # purple silk
        "C": (120, 200, 110, 255),   # green eyes
        "R": (196, 56, 40, 255),     # red mandibles
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        1:  [(14, 19)],                          # fan top
        2:  [(12, 21)],
        3:  [(10, 23)],
        4:  [(8, 25)],
        5:  [(7, 26)],
        6:  [(6, 27)],
        7:  [(5, 28)],
        8:  [(4, 29)],                           # fan widest
        9:  [(4, 29)],
        10: [(5, 28)],
        11: [(6, 9), (12, 21), (24, 27)],        # fan rim + head
        12: [(7, 8), (12, 21), (25, 26)],        # rim tips + head
        13: [(12, 21)],                          # head
        14: [(13, 20)],                          # mandibles row
        15: [(14, 19)],                          # body
        16: [(9, 11), (14, 19), (22, 24)],       # forearms + body
        17: [(8, 10), (15, 18), (23, 25)],
        18: [(8, 8), (10, 10), (15, 18), (23, 23), (25, 25)],  # legs
        19: [(15, 18)],                          # body tip
    },
    "fills": [
        # dark seam splitting the fan into two wings
        ("runs", [(2, 16, 17), (3, 16, 17), (4, 16, 17), (5, 16, 17),
                  (6, 16, 17), (7, 16, 17), (8, 16, 17), (9, 16, 17),
                  (10, 16, 17), (11, 16, 17)], "E"),
        # dark gold chevron bands fanning down the wings
        ("runs", [(3, 14, 19), (4, 12, 21), (5, 11, 22)], "E"),
        ("runs", [(6, 9, 12), (6, 21, 24), (7, 8, 11), (7, 22, 25),
                  (8, 7, 10), (8, 23, 26), (9, 6, 9), (9, 24, 27),
                  (10, 6, 9), (10, 24, 27)], "E"),
        # blue trim along the fan outer rim
        ("runs", [(8, 4, 5), (9, 4, 5), (10, 5, 6), (11, 6, 9),
                  (12, 7, 8), (8, 28, 29), (9, 28, 29), (10, 27, 28),
                  (11, 24, 27), (12, 25, 26), (5, 7, 7), (6, 6, 6),
                  (7, 5, 5), (5, 26, 26), (6, 27, 27), (7, 28, 28)],
         "B", "G"),
        # purple silk strands hanging from the rim
        ("runs", [(13, 6, 6), (13, 27, 27), (14, 6, 6), (14, 27, 27),
                  (15, 6, 6), (15, 27, 27)], "P"),
        # gold face with green eyes
        ("runs", [(12, 14, 19)], "G"),
        ("runs", [(12, 15, 16), (12, 17, 18)], "C", "G"),
        ("put", 12, 15, "K"),
        ("put", 12, 18, "K"),
        # red mandible hooks on the jaw row
        ("runs", [(14, 14, 15), (14, 18, 19)], "R"),
        ("put", 14, 16, "E"),
        ("put", 14, 17, "E"),
        # dark forearms with pale claw tips
        ("runs", [(16, 9, 11), (16, 22, 24), (17, 8, 10), (17, 23, 25)],
         "E"),
        ("put", 18, 8, "W"),
        ("put", 18, 25, "W"),
        # body shading
        ("runs", [(15, 18, 19), (16, 18, 19), (19, 17, 18)], "E"),
    ],
}
