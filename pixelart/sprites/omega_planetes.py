"""Omega Planetes, elder dragon. The other-world machine: a pale armored
humanoid-frame dragon with gold circuit lines and twin blade arms."""

CONFIG = {
    "name": "omega-planetes",
    "size": (32, 24),
    "compare_to": "",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (204, 202, 196, 255),  # pale machine plating
        "D": (162, 160, 154, 255),  # darker plating
        "Y": (236, 182, 84, 255),   # gold circuit lines
        "N": (62, 60, 66, 255),     # dark joints
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(5, 6), (10, 11)],               # blade arm tips
        3:  [(4, 7), (9, 12)],
        4:  [(3, 8), (8, 14)],                # arms + head
        5:  [(2, 9), (7, 16)],
        6:  [(1, 10), (6, 18)],               # head + body
        7:  [(1, 11), (5, 20)],
        8:  [(1, 12), (5, 21)],               # torso
        9:  [(1, 12), (5, 21)],
        10: [(1, 12), (5, 21)],
        11: [(1, 12), (5, 21)],
        12: [(2, 12), (6, 21)],
        13: [(3, 12), (8, 20)],
        14: [(4, 12), (10, 19)],
        15: [(5, 11), (12, 17)],              # legs
        16: [(5, 10), (13, 16)],
        17: [(5, 5), (7, 7), (13, 13), (15, 15)],
    },
    "fills": [
        # gold circuit lines across the chest and arms
        ("runs", [(6, 8, 9), (7, 8, 9), (8, 8, 9), (9, 8, 9),
                  (10, 8, 9), (11, 8, 9), (12, 8, 9)], "Y"),
        ("runs", [(4, 9, 11), (5, 10, 13), (6, 11, 15)], "Y", "G"),
        # dark joint bands
        ("runs", [(5, 8, 8), (8, 12, 13), (10, 12, 13)], "N"),
        # plating shade
        ("runs", [(14, 4, 12), (15, 5, 11), (16, 5, 10)], "D"),
        # feet
        ("put", 17, 5, "N"),
        ("put", 17, 7, "N"),
        ("put", 17, 13, "N"),
        ("put", 17, 15, "N"),
    ],
}
