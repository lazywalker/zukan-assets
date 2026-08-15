"""Leshen, elder dragon. The rooted fear: a pale deer-skull head under
branching wood antlers, a dark log body with glowing rune marks, a clawed
branch arm, and root legs. The skull face is the identity anchor."""

CONFIG = {
    "name": "leshen",
    "size": (28, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (66, 54, 48, 255),     # dark log body
        "D": (48, 40, 36, 255),     # darker bark
        "T": (150, 118, 76, 255),   # wood antlers
        "C": (226, 218, 200, 255),  # pale skull face
        "G": (140, 190, 100, 255),  # glowing rune marks
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        1:  [(4, 4), (9, 9)],                 # antler tine tips
        2:  [(3, 5), (8, 10)],
        3:  [(2, 5), (8, 11)],                # antler beams + tine
        4:  [(2, 6), (8, 12)],
        5:  [(3, 7), (9, 12)],                # antler roots / skull top
        6:  [(4, 11)],                        # skull
        7:  [(4, 11)],
        8:  [(4, 11)],
        9:  [(4, 11)],
        10: [(2, 12), (13, 17)],              # trunk + branch arm
        11: [(2, 12), (14, 18)],
        12: [(2, 12), (15, 18)],
        13: [(2, 12), (16, 19)],
        14: [(2, 12), (17, 19)],
        15: [(3, 12), (18, 20)],              # arm claw tips
        16: [(3, 12)],
        17: [(4, 11)],                        # root legs
        18: [(4, 4), (6, 6), (8, 8), (10, 10)],
    },
    "fills": [
        # wood antlers with pale tips, dark far beam
        ("runs", [(1, 4, 4), (2, 3, 5), (3, 2, 5), (4, 2, 6)], "T"),
        ("runs", [(1, 9, 9), (2, 8, 10), (3, 8, 11), (4, 8, 12)], "D"),
        ("put", 3, 8, "T"),
        ("put", 1, 4, "W"),
        ("put", 1, 9, "W"),
        # pale skull face with dark eye sockets
        ("runs", [(6, 4, 11), (7, 4, 11), (8, 4, 11), (9, 4, 10)], "C"),
        ("put", 7, 6, "K"),
        ("put", 7, 9, "K"),
        ("put", 8, 7, "K"),
        ("put", 9, 6, "D"),
        ("put", 9, 9, "D"),
        # glowing rune marks down the trunk
        ("runs", [(11, 6, 7), (13, 8, 9), (15, 6, 7)], "G"),
        # branch arm bark with claw tips
        ("runs", [(10, 13, 17), (11, 14, 18), (12, 15, 18),
                  (13, 16, 19), (14, 17, 19)], "D"),
        ("put", 15, 18, "T"),
        ("put", 15, 20, "T"),
        # bark shade at the trunk base
        ("runs", [(15, 3, 12), (16, 4, 12), (17, 4, 11)], "D"),
        # root claws
        ("put", 18, 4, "D"),
        ("put", 18, 6, "D"),
        ("put", 18, 8, "D"),
        ("put", 18, 10, "D"),
    ],
}
