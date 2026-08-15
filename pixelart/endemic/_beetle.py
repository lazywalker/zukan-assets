"""Beetle archetype: side view facing left, dome elytra with a center
split line, darker head with mandibles, three visible legs. Horned
species (hercudrome) patch a horn onto the head."""

CONFIG = {
    "name": "_beetle",
    "size": (28, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (94, 110, 80, 255),    # elytra
        "D": (66, 80, 56, 255),     # darker: head, split
        "C": (200, 190, 150, 255),  # horn / legs
        "W": (246, 242, 230, 255),
    },
    "base": "B",
    "spans": {
        6:  [(9, 13)],
        7:  [(8, 15)],
        8:  [(7, 21)],
        9:  [(5, 22)],
        10: [(4, 23)],
        11: [(3, 24)],
        12: [(3, 24)],
        13: [(3, 24)],
        14: [(4, 23)],
        15: [(5, 22)],
        16: [(6, 20)],
        17: [(8, 10), (14, 16), (19, 21)],
        18: [(8, 8), (10, 10), (14, 14), (16, 16), (19, 19), (21, 21)],
    },
    "fills": [
        # head darker with a mandible notch
        ("runs", [(6, 9, 13), (7, 8, 11)], "D"),
        ("put", 7, 8, "K"),
        # elytra split line down the middle
        ("runs", [(8, 15, 15), (9, 15, 15), (10, 15, 15), (11, 15, 15),
                  (12, 15, 15), (13, 15, 15), (14, 15, 15), (15, 15, 15)],
         "D"),
        # elytra shine
        ("runs", [(9, 7, 9), (10, 6, 7), (11, 5, 6)], "W", "B"),
        # eye
        ("put", 7, 11, "W"),
    ],
}
