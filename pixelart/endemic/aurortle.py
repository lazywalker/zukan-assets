"""Aurortle: a small turtle with a green shell dome, pale plastron, a
tiny head poking out, and stub legs."""
CONFIG = {
    "name": "aurortle",
    "size": (26, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (110, 160, 100, 255),  # shell
        "D": (78, 120, 72, 255),    # shell shade
        "C": (222, 226, 190, 255),  # skin / plastron
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        10: [(8, 19)],
        11: [(6, 21)],
        12: [(5, 22)],
        13: [(5, 22)],
        14: [(5, 22)],
        15: [(6, 21)],
        16: [(4, 20)],
        17: [(3, 19)],
        18: [(2, 8), (11, 11), (15, 15)],
        19: [(2, 2), (5, 5), (11, 11), (15, 15)],
    },
    "fills": [
        # head poking out at the left with an eye
        ("runs", [(16, 4, 7), (17, 3, 6)], "C"),
        ("put", 17, 5, "K"),
        # shell scute pattern
        ("runs", [(11, 10, 17), (12, 9, 18), (13, 9, 18), (14, 10, 17)],
         "D"),
        # pale plastron edge along the bottom
        ("runs", [(16, 8, 18), (17, 7, 16)], "C"),
    ],
}
