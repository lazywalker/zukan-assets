"""Chameleos, elder dragon. The invisible trickster: a pink-purple chameleon
body with a curled tail sweeping up-right, a single nose horn, big pale
eyes, a coiled tongue, and wavy skin frills."""

CONFIG = {
    "name": "chameleos",
    "size": (32, 24),
    "compare_to": "../icons/mh4u/chameleos.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "P": (206, 152, 178, 255),  # pink-purple skin
        "D": (168, 118, 146, 255),  # darker skin
        "V": (142, 96, 164, 255),   # deep purple frills
        "C": (232, 214, 220, 255),  # pale belly / eyes
        "Y": (232, 196, 80, 255),   # tongue tip
        "W": (246, 242, 230, 255),
    },
    "base": "P",
    "spans": {
        3:  [(4, 6)],                         # nose horn
        4:  [(2, 8), (9, 10)],
        5:  [(1, 9), (8, 11)],                # head + frill
        6:  [(1, 10), (7, 13)],
        7:  [(0, 10), (6, 15)],               # snout + body
        8:  [(0, 11), (5, 17)],
        9:  [(0, 11), (5, 19)],
        10: [(0, 11), (5, 21)],               # body + tail start
        11: [(0, 11), (5, 23)],
        12: [(1, 11), (6, 25)],
        13: [(1, 11), (8, 27)],
        14: [(2, 11), (10, 29)],
        15: [(2, 11), (13, 31)],              # tail curl up
        16: [(3, 11), (17, 31)],
        17: [(3, 11), (21, 31)],
        18: [(4, 11), (25, 31)],
        19: [(4, 10), (28, 31)],
        20: [(5, 10), (30, 31)],
        21: [(5, 10), (30, 30)],
    },
    "fills": [
        # nose horn pale
        ("runs", [(3, 4, 6), (4, 3, 5)], "C"),
        # big pale eyes
        ("runs", [(5, 2, 4), (6, 2, 4)], "C"),
        ("put", 5, 3, "K"),
        # curled tongue with a yellow tip
        ("runs", [(8, 0, 0), (9, 0, 0)], "Y"),
        # deep purple frills along the back
        ("runs", [(9, 8, 11), (10, 8, 12), (11, 7, 11)], "V"),
        # wavy skin bands
        ("runs", [(12, 6, 10), (14, 6, 10), (16, 6, 10)], "D"),
        # tail curl shade
        ("runs", [(14, 10, 29), (15, 14, 30), (16, 18, 31),
                  (17, 22, 31)], "D"),
        # tail tip dark
        ("runs", [(20, 30, 31), (21, 30, 30)], "V"),
    ],
}
