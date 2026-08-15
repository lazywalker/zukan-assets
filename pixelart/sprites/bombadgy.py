"""Bombadgy, fanged beast. The bomb raccoon: a round grey-white ball with
a dark raccoon mask face, yellow flank patches, tiny legs, and a small
brush tail."""

CONFIG = {
    "name": "bombadgy",
    "size": (26, 24),
    "compare_to": "../icons/mhrise/bombadgy.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "F": (210, 204, 192, 255),  # grey-white fur
        "D": (170, 162, 148, 255),  # fur shade
        "N": (74, 66, 58, 255),     # dark mask / tail
        "Y": (222, 178, 76, 255),   # yellow flank patches
        "W": (246, 242, 230, 255),
    },
    "base": "F",
    "spans": {
        4:  [(8, 9), (14, 15)],               # ear tips
        5:  [(6, 16)],
        6:  [(5, 17)],
        7:  [(4, 18)],
        8:  [(3, 19)],                        # round body
        9:  [(2, 20)],
        10: [(2, 20), (21, 22)],              # tail
        11: [(2, 20), (21, 23)],
        12: [(2, 20), (21, 23)],
        13: [(2, 20)],
        14: [(3, 20)],
        15: [(4, 19)],
        16: [(5, 18)],
        17: [(7, 10), (13, 16)],              # legs
        18: [(7, 9), (14, 15)],
    },
    "fills": [
        # dark raccoon mask with pale eyes
        ("runs", [(6, 6, 10), (6, 12, 16), (7, 5, 16), (8, 4, 16),
                  (9, 4, 16)], "N"),
        ("put", 8, 7, "W"),
        ("put", 8, 12, "W"),
        # pale muzzle + dark nose
        ("runs", [(10, 8, 14), (11, 9, 13)], "W"),
        ("put", 10, 11, "K"),
        # yellow flank patches
        ("runs", [(10, 17, 19), (11, 17, 19), (12, 17, 19)], "Y"),
        ("runs", [(13, 17, 18)], "Y"),
        # fur shade
        ("runs", [(14, 4, 19), (15, 5, 18), (16, 6, 17)], "D"),
        # dark tail
        ("runs", [(10, 21, 22), (11, 21, 23), (12, 21, 23)], "N"),
        # legs
        ("put", 18, 7, "N"),
        ("put", 18, 9, "N"),
        ("put", 18, 14, "N"),
    ],
}
