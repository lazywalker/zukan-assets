"""Zorah Magdaros, elder dragon. The scorching mountain: a colossal
volcanic shell of black rock cracked with glowing magma, a broad mountain
back, stubby towering legs, and lava pooling below."""

CONFIG = {
    "name": "zorah-magdaros",
    "size": (38, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "N": (58, 54, 56, 255),     # black rock shell
        "D": (40, 38, 40, 255),     # darker rock
        "M": (240, 122, 48, 255),   # magma glow
        "m": (184, 74, 40, 255),    # cooling magma
        "W": (246, 242, 230, 255),
    },
    "base": "N",
    "spans": {
        3:  [(8, 16), (22, 24)],              # mountain peaks
        4:  [(6, 20), (20, 26)],
        5:  [(4, 24), (18, 28)],
        6:  [(3, 27), (16, 30)],
        7:  [(2, 29), (14, 32)],
        8:  [(1, 31), (12, 33)],              # shell mass
        9:  [(1, 33), (10, 34)],
        10: [(0, 34), (9, 35)],
        11: [(0, 34), (8, 36)],
        12: [(0, 34), (7, 37)],
        13: [(0, 34), (6, 37)],
        14: [(0, 34), (6, 37)],
        15: [(0, 34), (6, 37)],
        16: [(0, 34), (6, 37)],
        17: [(1, 34), (6, 37)],
        18: [(1, 34), (6, 37)],
        19: [(2, 34), (7, 36)],
        20: [(3, 33), (8, 35)],
        21: [(5, 10), (15, 19), (25, 29), (33, 34)],  # towering legs
        22: [(5, 9), (16, 18), (26, 28), (33, 34)],
    },
    "fills": [
        # magma cracks splitting the shell
        ("runs", [(5, 14, 15), (6, 13, 14), (7, 12, 13), (8, 11, 12),
                  (9, 12, 13), (10, 15, 16), (11, 18, 19),
                  (12, 21, 22), (13, 20, 21), (14, 19, 20)], "M", "N"),
        # mountain peak glow
        ("runs", [(3, 11, 13), (4, 10, 12), (5, 9, 10)], "m", "N"),
        # broad magma glow along the base
        ("runs", [(19, 8, 33), (20, 9, 32)], "m", "N"),
        # shell shade
        ("runs", [(16, 2, 34), (17, 2, 34), (18, 2, 34)], "D"),
        # legs darker
        ("runs", [(21, 15, 19), (21, 25, 29), (22, 16, 18)], "D"),
    ],
}
