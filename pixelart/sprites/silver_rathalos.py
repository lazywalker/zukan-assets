"""Silver Rathalos: the sky king, wings flapped to the top of the stroke.
The whole fan wing sits one row higher than the base sprite, plus the
silver body palette."""
from rathalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "silver-rathalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (192, 192, 198, 255)
CONFIG["palette"]["D"] = (140, 140, 150, 255)

# upstroke: wing block shifted one row up
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(19, 21)],
    1:  [(3, 3), (17, 23)],
    2:  [(2, 3), (15, 21)],
    3:  [(2, 4), (14, 25)],
    4:  [(2, 5), (13, 26)],
    5:  [(2, 6), (12, 23)],
    6:  [(1, 6), (7, 8), (11, 27)],
    7:  [(1, 7), (7, 8), (10, 27)],
    8:  [(1, 6), (7, 9), (10, 23)],
    9:  [(1, 5), (7, 9), (11, 22)],
    10: [(3, 6), (7, 9)],
}

CONFIG["fills"] = [
    # wing membrane: cream right of the leading-edge arm, one row up
    ("runs", [(1, 19, 23), (2, 17, 21), (3, 16, 25), (4, 15, 26),
              (5, 14, 23), (6, 13, 27), (7, 12, 27), (8, 12, 23),
              (9, 13, 22)], "C"),
    # three red finger bones radiating from the wrist to the tips
    ("runs", [(1, 21, 23), (2, 20, 21), (3, 19, 21), (4, 17, 18),
              (5, 15, 16)], "R"),
    ("runs", [(3, 24, 25), (4, 22, 26), (5, 19, 23), (6, 17, 20),
              (7, 15, 17)], "R"),
    ("runs", [(6, 24, 27), (7, 23, 27), (8, 19, 23), (9, 18, 22)],
     "R"),
    # scale dashes in the membrane panels
    ("runs", [(2, 17, 18), (3, 16, 17), (4, 19, 20), (6, 14, 15),
              (7, 13, 13), (7, 20, 21), (8, 16, 18), (9, 15, 16)],
     "S", "C"),
    # horn + lower jaw
    ("runs", [(1, 3, 3), (2, 2, 3), (3, 2, 4), (4, 2, 4), (10, 3, 5)],
     "C"),
    # far leg + belly + tail underside
    ("runs", [(17, 15, 18), (18, 15, 18), (19, 15, 18), (20, 15, 18)],
     "D"),
    ("put", 14, 10, "DDDD"),
    ("put", 15, 10, "DDDD"),
    ("put", 16, 11, "DDD"),
    ("put", 15, 19, "DD"),
    ("put", 16, 18, "DDD"),
    # brow, eye, fang
    ("put", 4, 2, "KK"),
    ("put", 5, 2, "WK"),
    ("put", 10, 1, "W"),
]
