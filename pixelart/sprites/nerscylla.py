"""Nerscylla, temnoceran. The hooded spider: a pale body with a purple
crest hood swept over the head, red fangs, four spiky legs per side, and
a round abdomen with a pale diamond mark. The spider archetype the
variants derive from."""

CONFIG = {
    "name": "nerscylla",
    "size": (30, 24),
    "compare_to": "../icons/mh4u/nerscylla.png",
    "palette": {
        ".": (0, 0, 0, 0),
        "K": (24, 20, 22, 255),
        "C": (208, 196, 172, 255),  # pale body
        "D": (166, 152, 128, 255),  # pale shade
        "V": (108, 84, 138, 255),   # purple crest hood
        "R": (198, 62, 52, 255),    # red fangs
        "W": (246, 242, 230, 255),
    },
    "base": "C",
    "spans": {
        3:  [(6, 10)],                        # hood crest
        4:  [(4, 12), (13, 14)],              # hood + front leg tip
        5:  [(3, 13), (13, 15)],
        6:  [(2, 14), (12, 16)],              # hood + back leg tip
        7:  [(2, 14), (11, 17)],
        8:  [(1, 15), (10, 18)],              # head + abdomen
        9:  [(1, 15), (10, 19)],
        10: [(1, 15), (10, 19)],
        11: [(1, 15), (10, 18)],
        12: [(1, 14), (10, 18)],
        13: [(2, 14), (11, 17)],
        14: [(2, 13), (12, 16)],
        15: [(3, 12), (13, 15)],
        16: [(4, 11), (14, 14)],
        17: [(4, 5), (7, 8), (10, 12)],       # legs
        18: [(4, 4), (6, 6), (9, 9), (11, 12)],
    },
    "fills": [
        # purple hood swept over the head
        ("runs", [(3, 6, 10), (4, 4, 12), (5, 3, 12), (6, 2, 9),
                  (7, 2, 7)], "V"),
        # red fangs under the hood
        ("runs", [(8, 1, 3), (9, 1, 3)], "R"),
        # eyes
        ("put", 7, 3, "W"),
        # pale diamond on the abdomen
        ("runs", [(10, 13, 16), (11, 12, 17), (12, 12, 17)], "W", "C"),
        ("runs", [(11, 14, 15)], "V", "W"),
        # leg shade
        ("runs", [(4, 13, 14), (5, 13, 15), (6, 12, 16)], "D", "C"),
        # abdomen shade
        ("runs", [(12, 10, 18), (13, 11, 17), (14, 12, 16)], "D"),
        # legs
        ("runs", [(17, 4, 5), (17, 7, 8), (17, 10, 12)], "D"),
        ("put", 18, 4, "D"),
        ("put", 18, 6, "D"),
        ("put", 18, 9, "D"),
        ("put", 18, 11, "D"),
        ("put", 18, 12, "D"),
    ],
}
