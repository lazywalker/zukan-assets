"""Cactuar: the cactus person; a green column body with spines, two stub
arms held forward, a face, and running legs."""
CONFIG = {
    "name": "cactuar",
    "size": (26, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (120, 170, 90, 255),   # cactus green
        "D": (86, 130, 62, 255),    # darker green
        "W": (240, 236, 220, 255),  # spine tips
        "B": (60, 60, 56, 255),     # face dots
    },
    "base": "G",
    "spans": {
        4:  [(10, 15)],
        5:  [(9, 16)],
        6:  [(9, 16)],
        7:  [(8, 17)],
        8:  [(8, 17)],
        9:  [(8, 17)],
        10: [(8, 17)],
        11: [(8, 17)],
        12: [(8, 17)],
        13: [(8, 17)],
        14: [(8, 17)],
        15: [(8, 17)],
        16: [(9, 16)],
        17: [(10, 12), (14, 16)],
        18: [(10, 10), (12, 12), (14, 14), (16, 16)],
    },
    "fills": [
        # face: two dot eyes + a mouth line
        ("put", 7, 11, "B"),
        ("put", 7, 15, "B"),
        ("runs", [(9, 11, 14)], "B"),
        # spines sticking out of the arms and sides
        ("runs", [(9, 8, 8), (11, 8, 8), (13, 8, 8), (9, 17, 17),
                  (11, 17, 17), (13, 17, 17)], "W"),
        # darker side shading
        ("runs", [(7, 15, 17), (9, 15, 17), (11, 15, 17), (13, 15, 17)], "D"),
    ],
}
