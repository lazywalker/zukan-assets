"""Zinogre, thunder-wolf fanged wyvern. Second archetype: hunched quadruped,
no wings. Reference pose from icons/mhrise/zinogre.png: crown shell plate,
open jaw with fangs, arched back with gold spikes, huge gold foreleg plates,
white chest fur, bushy tail sweeping up, green claws.
"""

CONFIG = {
    "name": "zinogre",
    "size": (34, 24),
    "compare_to": "../icons/mhrise/zinogre.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),     # near-black outline
        "T": (74, 178, 158, 255),   # teal fur body
        "t": (46, 126, 110, 255),   # dark teal: belly, hind shade
        "G": (240, 194, 62, 255),   # gold shell plates
        "g": (182, 138, 38, 255),   # dark gold: plate shadow
        "V": (64, 86, 26, 255),     # claw green
        "W": (242, 240, 228, 255),  # chest fur / eye / fangs
    },
    "base": "T",
    "spans": {
        # head: crown plate rows 2-5, skull 4-8, jaw 8-10
        2:  [(4, 6), (28, 29)],               # crown tip + tail tip spike
        3:  [(3, 8), (15, 16), (19, 20), (27, 29)],
        4:  [(2, 8), (14, 14), (17, 17), (20, 21), (26, 29)],
        5:  [(1, 9), (13, 22), (25, 30)],
        6:  [(1, 10), (12, 23), (24, 30)],
        7:  [(2, 10), (12, 30)],              # snout + back + tail, one span
        8:  [(4, 8), (10, 26)],               # mouth gap c1-3
        9:  [(2, 26)],                        # lower jaw + chest + body
        10: [(9, 25)],
        11: [(9, 25)],
        12: [(10, 25)],
        13: [(10, 25)],
        14: [(10, 24)],
        15: [(10, 22)],
        16: [(11, 20)],
        17: [(12, 15), (19, 22)],             # foreleg + hind leg
        18: [(12, 15), (19, 22)],
        19: [(12, 14), (19, 21)],
        20: [(12, 14), (19, 21)],
        21: [(11, 13), (19, 21)],             # paws
        22: [(11, 11), (13, 13), (19, 19), (21, 21)],  # claws
    },
    "fills": [
        # crown + ear crest gold
        ("runs", [(2, 4, 6), (3, 3, 8), (4, 2, 8), (5, 1, 7),
                  (5, 8, 9), (6, 9, 10)], "G"),
        # back spikes + back ridge band
        ("runs", [(3, 15, 16), (3, 19, 20), (4, 14, 14), (4, 17, 17),
                  (4, 20, 21), (5, 13, 22)], "G"),
        # shoulder + foreleg shell, running down the leg's outer side
        ("runs", [(9, 14, 18), (10, 12, 17), (11, 12, 17), (12, 12, 17),
                  (13, 12, 16), (14, 12, 15), (15, 12, 15)], "G"),
        ("runs", [(16, 12, 15)], "g"),
        # hip plate flowing into the hind leg top
        ("runs", [(9, 21, 25), (10, 21, 25), (11, 21, 25)], "G"),
        ("runs", [(12, 22, 25)], "g"),
        # tail outer edge gold
        ("runs", [(2, 28, 29), (3, 27, 29), (4, 26, 28), (5, 25, 28),
                  (6, 28, 30), (7, 27, 30)], "G"),
        # belly + under-tail shade
        ("runs", [(14, 10, 11), (15, 10, 13), (16, 11, 14)], "t"),
        ("runs", [(14, 22, 24), (15, 20, 23)], "t"),
        # chest fur
        ("runs", [(10, 9, 13), (11, 9, 12), (12, 9, 12), (13, 10, 12)], "W"),
        # eye + fang
        ("put", 6, 2, "WK"),
        ("put", 8, 2, "W"),
        # claws
        ("put", 22, 11, "V"),
        ("put", 22, 13, "V"),
        ("put", 22, 19, "V"),
        ("put", 22, 21, "V"),
    ],
}
