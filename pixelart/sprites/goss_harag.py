"""Goss Harag, fanged beast. The frost yeti: a hulking white-furred
gorilla crouched on huge arms, a dark blue face with yellow eyes, blue
band markings, and ice claws."""

CONFIG = {
    "name": "goss-harag",
    "size": (30, 24),
    "compare_to": "../icons/mhrise/goss-harag.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (228, 226, 218, 255),  # white fur
        "D": (184, 182, 174, 255),  # fur shade
        "N": (64, 72, 100, 255),    # dark blue face / markings
        "I": (176, 214, 232, 255),  # ice claws
        "Y": (232, 190, 70, 255),   # yellow eyes
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        3:  [(5, 8), (11, 13)],               # crest tufts
        4:  [(4, 14)],
        5:  [(3, 15)],
        6:  [(2, 16)],
        7:  [(2, 17)],                        # hunched shoulders
        8:  [(1, 18)],
        9:  [(1, 19)],
        10: [(1, 19), (20, 21)],              # body + fist start
        11: [(1, 19), (19, 22)],
        12: [(1, 19), (19, 23)],              # knuckles
        13: [(1, 19), (19, 23)],
        14: [(2, 19), (19, 23)],
        15: [(2, 19), (19, 22)],
        16: [(3, 19), (19, 22)],
        17: [(4, 19)],
        18: [(5, 18)],
        19: [(6, 11), (14, 17)],              # legs
        20: [(6, 10), (15, 16)],
        21: [(6, 6), (8, 8), (15, 15), (17, 17)],
    },
    "fills": [
        # dark blue face with yellow eyes
        ("runs", [(4, 6, 13), (5, 5, 14), (6, 5, 14), (7, 4, 12)], "N"),
        ("put", 5, 7, "Y"),
        ("put", 5, 12, "Y"),
        # pale fangs under the face
        ("runs", [(8, 5, 7), (8, 10, 12)], "W"),
        # blue band markings on the arms
        ("runs", [(10, 20, 21), (11, 19, 22), (12, 19, 23)], "N", "F"),
        ("runs", [(14, 19, 23), (15, 19, 22)], "N", "F"),
        # ice claws on the knuckles
        ("runs", [(12, 19, 23), (13, 20, 23)], "I", "N"),
        # fur shade along the belly
        ("runs", [(15, 3, 18), (16, 4, 18), (17, 5, 18), (18, 6, 17)], "D"),
        # crest tufts dark
        ("runs", [(3, 5, 8), (3, 11, 13)], "D"),
        # claws
        ("put", 21, 6, "I"),
        ("put", 21, 8, "I"),
        ("put", 21, 15, "I"),
        ("put", 21, 17, "I"),
    ],
}
