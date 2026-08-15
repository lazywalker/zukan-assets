"""Rajang, golden ape. Hunched knuckle-walking biped. Series-standard look:
gold fur with a big shoulder hump, dark face buried in a black mane, red
eyes, massive forearms reaching the ground, short legs, tiny tail.
"""

CONFIG = {
    "name": "rajang",
    "size": (30, 24),
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "G": (205, 170, 60, 255),   # gold fur
        "g": (160, 130, 45, 255),   # dark gold shade
        "D": (60, 45, 38, 255),     # dark brown: face, mane, fists
        "R": (215, 50, 45, 255),    # red eyes
        "W": (245, 242, 230, 255),  # knuckle light / fangs
    },
    "base": "G",
    "spans": {
        # head rows 3-9 with swept-back crown fur
        3:  [(4, 6), (8, 12)],
        4:  [(3, 8), (8, 14)],
        5:  [(2, 9), (9, 15)],
        6:  [(2, 10), (10, 16)],
        7:  [(2, 11), (11, 17)],
        8:  [(3, 12), (12, 18)],
        9:  [(4, 13), (13, 19)],
        10: [(5, 14), (14, 20)],
        11: [(5, 15), (15, 20)],
        12: [(5, 15), (15, 20)],
        13: [(5, 15), (15, 20)],
        14: [(5, 14), (15, 20)],
        15: [(6, 13), (16, 19)],
        16: [(6, 12), (16, 19)],
        17: [(6, 11), (17, 19)],
        18: [(6, 10), (17, 19)],
        19: [(5, 10), (18, 19)],              # fist + hind foot
        20: [(5, 10), (18, 19)],
        21: [(5, 5), (8, 8), (18, 18)],       # knuckle lights + claw
    },
    "fills": [
        # dark face buried in the mane
        ("runs", [(6, 4, 8), (7, 4, 9), (8, 5, 9)], "D"),
        # mane strips around the face
        ("runs", [(5, 2, 4), (6, 2, 3), (7, 2, 3), (8, 3, 4), (9, 4, 4)], "D"),
        # red eyes + fang
        ("put", 6, 5, "R"),
        ("put", 6, 7, "R"),
        ("put", 7, 8, "W"),
        # shoulder hump shade
        ("runs", [(8, 13, 18), (9, 14, 19), (10, 15, 20)], "g"),
        # belly shade
        ("runs", [(13, 12, 14), (14, 12, 14), (15, 12, 13)], "g"),
        # separation line between the forearm and the body
        ("runs", [(10, 11, 11), (11, 11, 11), (12, 11, 11), (13, 11, 11),
                  (14, 11, 11), (15, 11, 11), (16, 11, 11)], "K"),
        # dark fist at the bottom of the forearm
        ("runs", [(17, 6, 11), (18, 6, 10), (19, 5, 10), (20, 5, 10)], "D"),
        # hind leg shade + dark foot
        ("runs", [(18, 17, 19), (19, 18, 19), (20, 18, 19)], "g"),
        ("runs", [(20, 18, 19)], "D"),
        # knuckle lights
        ("put", 21, 5, "W"),
        ("put", 21, 8, "W"),
        ("put", 21, 18, "W"),
    ],
}
