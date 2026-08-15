"""Astalos, flying wyvern. The thunder mantis: big-headed runner skeleton
with astalos identity; a tall head crowned by the yellow-tipped crest
horn, a beak jaw, big yellow-edged wing blades over the back, green body
with an orange chest band, a long tail ending in a yellow blade tip."""

CONFIG = {
    "name": "astalos",
    "size": (36, 24),
    "compare_to": "../icons/mhgu/astalos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "G": (118, 156, 92, 255),   # green plating
        "D": (88, 120, 68, 255),    # darker green
        "Y": (236, 202, 72, 255),   # electric yellow
        "O": (222, 122, 52, 255),   # orange chest band
        "W": (246, 242, 230, 255),
    },
    "base": "G",
    "spans": {
        2:  [(6, 9), (30, 30)],               # crest tip + tail tip
        3:  [(5, 11), (29, 31)],
        4:  [(4, 12), (28, 31)],
        5:  [(3, 13), (27, 31)],
        6:  [(2, 13), (26, 31)],              # brow + tail
        7:  [(1, 13), (13, 24), (25, 30)],    # snout + body + tail
        8:  [(5, 13), (13, 25), (25, 28)],    # mouth gap c1-4
        9:  [(2, 12), (12, 25)],
        10: [(2, 11), (12, 25)],
        11: [(3, 11), (12, 25)],
        12: [(12, 25)],
        13: [(12, 24)],
        14: [(13, 23)],
        15: [(13, 22)],
        16: [(14, 18), (22, 26)],
        17: [(14, 18), (22, 26)],
        18: [(14, 17), (22, 25)],
        19: [(14, 17), (22, 25)],
        20: [(13, 17), (22, 25)],
        21: [(13, 13), (15, 15), (22, 22), (24, 24)],
    },
    "fills": [
        # crest horn dark with a yellow tip
        ("runs", [(2, 6, 9), (3, 5, 11), (4, 4, 11)], "D"),
        ("runs", [(2, 7, 8), (3, 7, 9)], "Y"),
        # eye + fangs
        ("put", 6, 4, "K"),
        ("put", 7, 2, "W"),
        ("put", 7, 4, "W"),
        ("put", 8, 3, "W"),
        # wing blades over the back with yellow edges
        ("runs", [(7, 14, 18), (8, 14, 20), (9, 14, 20)], "D"),
        ("runs", [(7, 17, 18), (8, 19, 20), (9, 19, 20)], "Y", "D"),
        # orange chest band
        ("runs", [(9, 2, 11), (10, 2, 10), (11, 3, 10)], "O"),
        # pale chest under the orange band
        ("runs", [(12, 12, 19), (13, 12, 19), (14, 13, 18),
                  (15, 13, 18)], "D"),
        # tail blade with yellow edge
        ("runs", [(2, 30, 30), (3, 30, 31), (4, 29, 31), (5, 29, 31)],
         "Y", "G"),
        ("runs", [(6, 28, 30), (7, 27, 29)], "Y", "G"),
        # body shade
        ("runs", [(12, 20, 24), (13, 20, 23), (14, 19, 22)], "D"),
        # leg bands
        ("runs", [(17, 15, 17), (17, 23, 25)], "D"),
        # claws
        ("put", 21, 13, "W"),
        ("put", 21, 15, "W"),
        ("put", 21, 22, "W"),
        ("put", 21, 24, "W"),
    ],
}
