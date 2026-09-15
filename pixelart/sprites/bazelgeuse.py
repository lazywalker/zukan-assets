"""Bazelgeuse, flying wyvern. The bomber, drawn in the horned front of
its icon: two dark wings curled up like horns, a grey head with a
red-brown scale cap and glaring yellow eyes, orange pinecone scale
clusters studding the wings, a pale jaw with a dark mouth gap, and
stout legs below."""

CONFIG = {
    "name": "bazelgeuse",
    "size": (36, 24),
    "compare_to": "../icons/mhw/bazelgeuse.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "B": (148, 148, 138, 255),   # grey body
        "D": (70, 72, 70, 255),      # dark charcoal wings
        "R": (172, 74, 48, 255),     # red-brown scale cap
        "O": (222, 130, 60, 255),    # orange scale glow
        "T": (104, 184, 168, 255),   # teal wing accents
        "Y": (240, 210, 70, 255),    # eye yellow
        "C": (230, 225, 210, 255),   # pale jaw
    },
    "base": "B",
    "spans": {
        1:  [(6, 7), (28, 29)],                  # wing horn tips
        2:  [(5, 8), (27, 30)],
        3:  [(4, 9), (26, 31)],
        4:  [(3, 10), (25, 32)],
        5:  [(3, 11), (24, 32)],
        6:  [(2, 11), (14, 21), (24, 33)],       # wings + scale cap
        7:  [(2, 12), (13, 22), (23, 33)],
        8:  [(2, 12), (12, 23), (23, 33)],
        9:  [(3, 12), (12, 23), (23, 32)],
        10: [(3, 11), (11, 24), (24, 32)],
        11: [(4, 11), (11, 24), (24, 31)],       # jaw row
        12: [(4, 10), (11, 24), (25, 31)],
        13: [(5, 10), (11, 24), (25, 30)],       # wings end + body
        14: [(6, 29)],
        15: [(6, 29)],
        16: [(7, 28)],
        17: [(7, 28)],
        18: [(8, 12), (14, 21), (23, 27)],       # legs
        19: [(8, 12), (14, 21), (23, 27)],
        20: [(9, 12), (15, 20), (23, 26)],
        21: [(9, 9), (12, 12), (15, 15), (20, 20), (23, 23), (26, 26)],
    },
    "fills": [
        # dark wings with teal membrane accents
        ("runs", [(1, 6, 7), (2, 5, 8), (3, 4, 9), (4, 3, 10), (5, 3, 11),
                  (6, 2, 11), (7, 2, 12), (8, 2, 12), (9, 3, 12),
                  (10, 3, 11), (11, 4, 11), (12, 4, 10), (13, 5, 10),
                  (1, 28, 29), (2, 27, 30), (3, 26, 31), (4, 25, 32),
                  (5, 24, 32), (6, 24, 33), (7, 23, 33), (8, 23, 33),
                  (9, 23, 32), (10, 24, 32), (11, 24, 31), (12, 25, 31),
                  (13, 25, 30)], "D"),
        ("runs", [(4, 6, 8), (5, 6, 8), (6, 5, 7), (4, 27, 29),
                  (5, 27, 29), (6, 28, 30)], "T", "D"),
        # orange pinecone scale clusters on the wings
        ("runs", [(6, 8, 10), (7, 7, 9), (6, 25, 27), (7, 26, 28),
                  (9, 8, 9), (9, 26, 27)], "O", "D"),
        # red-brown scale cap over the head
        ("runs", [(6, 14, 21), (7, 13, 22), (8, 12, 23)], "R"),
        ("runs", [(7, 15, 16), (7, 19, 20), (8, 14, 14), (8, 21, 21),
                  (8, 15, 16), (8, 19, 20)], "O", "R"),
        # angry brows over glaring yellow eyes
        ("runs", [(9, 13, 14), (9, 21, 22)], "D", "R"),
        ("runs", [(9, 15, 16), (9, 19, 20)], "Y", "B"),
        ("put", 9, 16, "K"),
        ("put", 9, 19, "K"),
        # dark mouth gap over the pale jaw
        ("runs", [(11, 14, 21)], "K", "B"),
        ("runs", [(12, 12, 23)], "C", "B"),
        ("runs", [(13, 13, 22)], "C", "B"),
        # grey body with dark shading
        ("runs", [(14, 6, 10), (14, 25, 29), (15, 6, 9), (15, 26, 29),
                  (16, 7, 10), (16, 25, 28), (17, 7, 10), (17, 25, 28)],
         "D", "B"),
        # stout dark legs with pale claws
        ("runs", [(18, 8, 12), (18, 23, 27), (19, 8, 12), (19, 23, 27),
                  (20, 9, 12), (20, 23, 26), (21, 9, 9), (21, 23, 23),
                  (21, 26, 26)], "D"),
        ("put", 21, 15, "C"),
        ("put", 21, 20, "C"),
    ],
}
