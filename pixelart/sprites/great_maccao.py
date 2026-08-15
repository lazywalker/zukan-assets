"""Great Maccao, bird wyvern leader. The kick-boxing variant of the
great-jaggi family: brown scales, a tall orange mohawk crest instead of
a frill, and the tail raised into an upturned club with a pale tip.
Differs from jaggi by the mohawk and the club tail."""
from great_jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-maccao"
CONFIG["compare_to"] = "../icons/mhgu/great-maccao.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (165, 125, 85, 255)   # brown scales
CONFIG["palette"]["F"] = (130, 95, 65, 255)    # dark brown crest
CONFIG["palette"]["C"] = (205, 175, 140, 255)  # pale belly
CONFIG["palette"]["S"] = (115, 85, 58, 255)    # spots / shade
CONFIG["palette"]["M"] = (205, 120, 55, 255)   # orange mohawk

# mohawk crest over the head, tail raised into an upturned club
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(8, 10)],
    2:  [(7, 11)],
    3:  [(7, 11), (31, 32)],
    4:  [(6, 12), (30, 33)],
    5:  [(5, 12), (30, 33)],
    6:  [(1, 12), (29, 33)],
    7:  [(1, 12), (29, 33)],
    8:  [(2, 11), (28, 33)],
    9:  [(3, 12), (13, 25), (28, 32)],
    10: [(5, 13), (14, 26), (27, 31)],
    11: [(6, 14), (15, 27), (28, 30)],
}

CONFIG["fills"] = [
    # orange mohawk with a dark base
    ("runs", [(1, 8, 10), (2, 7, 11), (3, 7, 11), (4, 6, 9)], "M"),
    ("runs", [(4, 10, 12), (5, 10, 12)], "F"),
    # beak: cream, dark mouth line
    ("runs", [(6, 1, 3), (7, 1, 3)], "C"),
    ("runs", [(8, 2, 3)], "S"),
    # eye
    ("put", 7, 5, "W"),
    # dark spots on the body
    ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22), (14, 12, 13),
              (14, 23, 24)], "S"),
    # cream underbelly
    ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)],
     "C"),
    # club tail: dark top edge, pale spike tip
    ("runs", [(4, 31, 32), (5, 30, 32), (6, 30, 31), (7, 31, 32),
              (8, 31, 32)], "F"),
    ("put", 3, 31, "W"),
    # tail underside shade
    ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
     "S"),
    # claws
    ("put", 21, 10, "W"),
    ("put", 21, 12, "W"),
    ("put", 21, 18, "W"),
    ("put", 21, 20, "W"),
]
