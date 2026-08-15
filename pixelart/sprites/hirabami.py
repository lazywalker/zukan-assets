"""Hirabami, leviathan. The ice ray: a pale blue serpentine body gliding
with big wing-fins whose trailing edges drip with icicles, red stripes
along the flanks, a slim arrow head."""

CONFIG = {
    "name": "hirabami",
    "size": (36, 24),
    "compare_to": "../icons/mhwilds/hirabami.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (156, 176, 206, 255),  # ice-blue body
        "D": (122, 144, 178, 255),  # darker ice
        "R": (198, 74, 62, 255),    # red stripes
        "W": (226, 236, 246, 255),  # icicle white
        "w": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        3:  [(4, 8)],                         # head crest
        4:  [(2, 10), (11, 13)],
        5:  [(1, 11), (10, 16)],              # head + wing top
        6:  [(1, 12), (9, 19)],
        7:  [(0, 12), (8, 21)],               # wing with drips
        8:  [(0, 12), (8, 22), (12, 12), (16, 16), (20, 20)],
        9:  [(0, 12), (7, 21), (11, 11), (15, 15), (19, 19)],
        10: [(0, 12), (7, 20)],
        11: [(1, 12), (7, 20)],
        12: [(1, 13), (8, 20)],               # body + wing bottom
        13: [(1, 14), (9, 19)],
        14: [(2, 14), (10, 18)],
        15: [(2, 15), (12, 18)],
        16: [(3, 15), (14, 17)],
        17: [(3, 15), (17, 17)],
        18: [(4, 15), (20, 22)],              # tail fins
        19: [(5, 15), (21, 24)],
        20: [(6, 15), (23, 24)],
    },
    "fills": [
        # slim arrow head with a dark eye
        ("runs", [(5, 1, 3), (6, 1, 3), (7, 0, 2)], "D"),
        ("put", 6, 4, "K"),
        # wing membrane with red stripes
        ("runs", [(4, 11, 13), (5, 10, 16), (6, 9, 19), (7, 8, 21),
                  (8, 8, 22), (9, 7, 21)], "W", "B"),
        ("runs", [(6, 13, 14), (7, 12, 13), (8, 12, 13), (9, 11, 12)],
         "R"),
        # body stripes
        ("runs", [(11, 13, 14), (12, 14, 15), (13, 15, 16),
                  (14, 15, 16)], "R"),
        # icicle drips under the wing
        ("runs", [(8, 12, 12), (8, 16, 16), (8, 20, 20), (9, 11, 11),
                  (9, 15, 15), (9, 19, 19)], "W"),
        # body shade along the bottom
        ("runs", [(13, 2, 13), (14, 3, 13), (15, 3, 14), (16, 4, 14)], "D"),
        # tail fins dark tips
        ("runs", [(18, 20, 22), (19, 22, 24)], "D"),
    ],
}
