"""Estrellian, elder dragon. The star steed: a long dark-indigo body with
a pair of red crescent horns sweeping back over the head, a small wing
fan on the shoulder, gold star sparkles scattered along the flank, and a
tapering tail. The estrellian archetype its variants derive from."""

CONFIG = {
    "name": "estrellian",
    "size": (36, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (66, 58, 92, 255),     # dark indigo hide
        "D": (48, 42, 70, 255),     # darker indigo
        "R": (196, 60, 48, 255),    # red crescent horns
        "r": (150, 40, 40, 255),    # darker red far horn
        "Y": (232, 196, 80, 255),   # gold star sparkles
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        2:  [(4, 5)],                     # near horn tip
        3:  [(3, 5), (8, 9)],             # horn + far horn tip
        4:  [(2, 5), (7, 10)],            # horn base + far horn
        5:  [(1, 6), (7, 11)],            # head crown + horn base / wing
        6:  [(0, 7), (8, 13)],            # snout + wing
        7:  [(0, 15)],                    # neck + wing merged
        8:  [(0, 30)],                    # body + tail root
        9:  [(0, 32)],
        10: [(0, 33)],
        11: [(0, 34)],
        12: [(0, 34)],
        13: [(1, 33)],
        14: [(2, 32)],
        15: [(4, 31)],
        16: [(7, 10), (15, 18), (23, 26)],    # legs
        17: [(7, 10), (15, 18), (23, 26)],
        18: [(7, 9), (15, 17), (23, 25)],
        19: [(6, 9), (14, 17), (22, 25)],
        20: [(6, 6), (8, 8), (14, 14), (16, 16), (22, 22), (24, 24)],
    },
    "fills": [
        # red crescent horns, far one darker
        ("runs", [(2, 4, 5), (3, 3, 5), (4, 2, 5), (5, 1, 4)], "R"),
        ("runs", [(3, 8, 9), (4, 7, 10), (5, 7, 9)], "r"),
        # eye
        ("put", 6, 2, "WK"),
        # wing membrane darker with a gold spark
        ("runs", [(6, 8, 13), (7, 8, 12)], "D"),
        ("put", 6, 10, "Y"),
        # gold star sparkles scattered along the flank
        ("runs", [(9, 17, 18), (10, 20, 21), (11, 23, 24), (12, 26, 27),
                  (13, 29, 30)], "Y", "N"),
        ("put", 8, 13, "Y"),
        # belly shade along the bottom edge
        ("runs", [(13, 4, 20), (14, 5, 18), (15, 6, 16)], "D"),
        # far legs darker
        ("runs", [(16, 15, 18), (17, 15, 18), (18, 15, 17), (19, 14, 17),
                  (16, 23, 26), (17, 23, 26), (18, 23, 25), (19, 22, 25)],
         "D"),
        # claws
        ("runs", [(20, 6, 6), (20, 8, 8), (20, 14, 14), (20, 16, 16),
                  (20, 22, 22), (20, 24, 24)], "W"),
    ],
}
