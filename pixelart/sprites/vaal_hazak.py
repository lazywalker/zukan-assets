"""Vaal Hazak, elder dragon. Miasma dragon: distinct huge flat-jawed head
rising at the left, lower horizontal body with pale spine fins, red
effluvium glow lines along the flank, long drooping tail, stubby legs."""

CONFIG = {
    "name": "vaal-hazak",
    "size": (36, 24),
    "compare_to": "../icons/mhw/vaal-hazak.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (188, 190, 182, 255),  # pale gray body
        "D": (138, 140, 136, 255),  # darker gray: fins, shade
        "R": (205, 60, 50, 255),    # red effluvium glow
        "W": (240, 240, 232, 255),  # tiny pale eyes
    },
    "base": "P",
    "spans": {
        4:  [(1, 9), (14, 15), (20, 21)],
        5:  [(1, 11), (13, 17), (19, 22)],
        6:  [(1, 12), (12, 14), (16, 18)],
        7:  [(1, 13), (11, 13), (15, 18)],
        8:  [(1, 13), (11, 12), (16, 19)],
        9:  [(1, 13), (12, 26)],
        10: [(2, 14), (12, 28)],
        11: [(2, 14), (12, 30)],
        12: [(3, 14), (12, 32)],
        13: [(3, 14), (12, 33)],
        14: [(4, 14), (13, 34)],
        15: [(5, 14), (14, 34)],
        16: [(6, 15), (15, 33)],
        17: [(7, 15), (16, 32)],
        18: [(7, 15), (17, 31)],
        19: [(8, 15), (18, 30)],
        20: [(9, 15), (19, 29)],
        21: [(11, 11), (14, 14), (20, 20), (23, 23)],
    },
    "fills": [
        # huge flat head: darker jaw, tiny pale eyes
        ("runs", [(6, 1, 6), (7, 1, 6), (8, 1, 6)], "D"),
        ("put", 5, 2, "W"),
        ("put", 5, 5, "W"),
        # neck dip between head and body
        ("runs", [(8, 10, 11)], "D"),
        # spine fins, darker gray
        ("runs", [(4, 14, 15), (5, 13, 17), (6, 12, 14), (6, 16, 18),
                  (7, 11, 13), (7, 15, 18), (8, 16, 19)], "D"),
        # red effluvium glow lines on the flank
        ("runs", [(10, 13, 14), (11, 13, 14), (12, 14, 15), (13, 14, 15),
                  (14, 14, 15), (15, 15, 16), (16, 15, 16), (17, 15, 16),
                  (18, 16, 17), (19, 17, 18), (20, 18, 19)], "R"),
        # tail underside shade
        ("runs", [(13, 24, 30), (14, 24, 32), (15, 24, 32), (16, 24, 31),
                  (17, 24, 30), (18, 24, 29), (19, 24, 28), (20, 24, 27)],
         "D"),
        # claws
        ("put", 21, 11, "W"),
        ("put", 21, 14, "W"),
        ("put", 21, 20, "W"),
        ("put", 21, 23, "W"),
    ],
}
