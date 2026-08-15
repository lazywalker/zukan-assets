"""Namielle, elder dragon. The water dragon: big gentle head with pale
eyes at the left, wide manta cloak spreading right with a pale rim, thin
tail, tiny legs, cyan droplets dripping from the cloak edge."""

CONFIG = {
    "name": "namielle",
    "size": (36, 24),
    "compare_to": "../icons/mhwi/namielle.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (100, 110, 195, 255),  # deep blue body
        "L": (170, 180, 230, 255),  # pale belly / cloak edge
        "D": (70, 80, 150, 255),    # darker edge
        "C": (150, 220, 230, 255),  # cyan droplets
        "W": (240, 240, 245, 255),  # eye
    },
    "base": "B",
    "spans": {
        5:  [(1, 7), (12, 14)],
        6:  [(1, 9), (11, 17)],
        7:  [(1, 10), (10, 19)],
        8:  [(1, 11), (10, 21)],
        9:  [(1, 11), (10, 24)],
        10: [(1, 12), (10, 27)],
        11: [(1, 12), (10, 30)],
        12: [(1, 12), (10, 32)],
        13: [(2, 12), (10, 33)],
        14: [(2, 12), (10, 34)],
        15: [(3, 12), (11, 34)],
        16: [(4, 12), (13, 33)],
        17: [(5, 12), (15, 32)],
        18: [(6, 12), (18, 30)],
        19: [(7, 11), (21, 28)],
        20: [(8, 10), (23, 26)],
        21: [(9, 9), (13, 13), (22, 23)],
        22: [(9, 9), (22, 22)],
    },
    "fills": [
        # big pale eyes on the head
        ("put", 7, 2, "W"),
        ("put", 7, 4, "W"),
        # tiny beak
        ("runs", [(8, 1, 1)], "D"),
        # cloak rim: pale along the bottom edge
        ("runs", [(15, 12, 33), (16, 13, 32), (17, 14, 31), (18, 16, 29),
                  (19, 18, 28), (20, 21, 26)], "L"),
        # darker rim above it
        ("runs", [(13, 11, 32), (14, 11, 33)], "D"),
        # cyan droplets dripping
        ("runs", [(16, 5, 5), (17, 3, 3), (18, 1, 1), (19, 24, 24),
                  (20, 27, 27), (16, 30, 30), (17, 32, 32)], "C"),
        # thin tail + tiny legs
        ("runs", [(21, 22, 23), (22, 9, 9)], "L"),
    ],
}
