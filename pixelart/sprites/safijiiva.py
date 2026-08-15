"""Safi'jiiva, elder dragon. The red emperor: xenojiiva grown; a deep
crimson dragon with golden organ lines glowing along the body, curved
horns, and wide wing-arms."""

CONFIG = {
    "name": "safijiiva",
    "size": (34, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "R": (172, 62, 52, 255),    # deep crimson scales
        "D": (132, 44, 40, 255),    # darker crimson
        "Y": (236, 178, 68, 255),   # golden organ lines
        "C": (222, 130, 100, 255),  # pale red chest
        "W": (246, 242, 230, 255),
    },
    "base": "R",
    "spans": {
        2:  [(4, 5), (9, 10)],                # horn tips
        3:  [(3, 6), (8, 11)],
        4:  [(2, 7), (7, 13)],
        5:  [(1, 8), (6, 15)],
        6:  [(1, 9), (5, 17)],                # head + wing arm
        7:  [(0, 10), (5, 19)],
        8:  [(0, 11), (4, 21)],
        9:  [(0, 12), (4, 22)],
        10: [(0, 12), (4, 23)],
        11: [(0, 12), (4, 23)],
        12: [(0, 12), (4, 23)],
        13: [(0, 12), (4, 23)],
        14: [(0, 12), (4, 23)],
        15: [(0, 12), (4, 23)],
        16: [(1, 12), (4, 23)],
        17: [(1, 12), (4, 23)],
        18: [(1, 12), (4, 23)],
        19: [(2, 12), (5, 22)],
        20: [(3, 12), (6, 21)],
        21: [(4, 7), (10, 13), (15, 18)],     # legs + tail
    },
    "fills": [
        # curved horns
        ("runs", [(2, 4, 5), (2, 9, 10), (3, 3, 6), (3, 8, 11)], "D"),
        # golden organ lines glowing along the body
        ("runs", [(8, 5, 10), (9, 5, 10), (10, 5, 10), (11, 5, 10),
                  (12, 5, 10), (13, 5, 10), (14, 5, 10), (15, 5, 10)], "Y"),
        ("runs", [(10, 15, 22), (11, 15, 23), (12, 15, 23)], "Y", "R"),
        # pale eyes
        ("put", 6, 4, "W"),
        # pale red chest
        ("runs", [(8, 1, 4), (9, 1, 4), (10, 1, 4), (11, 1, 4)], "C"),
        # body shade
        ("runs", [(16, 1, 12), (17, 2, 12), (18, 2, 12)], "D"),
        # tail tip golden
        ("runs", [(20, 17, 21), (21, 15, 18)], "Y", "R"),
    ],
}
