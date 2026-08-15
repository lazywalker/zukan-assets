"""Azure Rathalos: steel-blue rathalos in the downstroke phase of the
wingbeat. The whole fan wing sits one row lower than the base sprite,
plus the blue body palette."""
from rathalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "azure-rathalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (62, 92, 142, 255)   # steel blue body
CONFIG["palette"]["D"] = (38, 58, 98, 255)    # dark blue shade

# downstroke: wing block shifted one row down, tip run at row 1 dropped
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(3, 3)],
    2:  [(2, 3), (19, 21)],
    3:  [(2, 4), (17, 23)],
    4:  [(2, 5), (15, 21)],
    5:  [(2, 6), (14, 25)],
    6:  [(1, 6), (7, 8), (13, 26)],
    7:  [(1, 7), (7, 8), (12, 23)],
    8:  [(1, 6), (7, 9), (11, 27)],
    9:  [(1, 5), (7, 9), (10, 27)],
    10: [(3, 6), (7, 9), (10, 23)],
    11: [(1, 4), (5, 10), (11, 22)],
}

CONFIG["fills"] = [
    # wing membrane: cream right of the leading-edge arm, one row down
    ("runs", [(3, 19, 23), (4, 17, 21), (5, 16, 25), (6, 15, 26),
              (7, 14, 23), (8, 13, 27), (9, 12, 27), (10, 12, 23),
              (11, 13, 22)], "C"),
    # three red finger bones radiating from the wrist to the tips
    ("runs", [(3, 21, 23), (4, 20, 21), (5, 19, 21), (6, 17, 18),
              (7, 15, 16)], "R"),
    ("runs", [(5, 24, 25), (6, 22, 26), (7, 19, 23), (8, 17, 20),
              (9, 15, 17)], "R"),
    ("runs", [(8, 24, 27), (9, 23, 27), (10, 19, 23), (11, 18, 22)],
     "R"),
    # scale dashes in the membrane panels
    ("runs", [(4, 17, 18), (5, 16, 17), (6, 19, 20), (8, 14, 15),
              (9, 13, 13), (9, 20, 21), (10, 16, 18), (11, 15, 16)],
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
