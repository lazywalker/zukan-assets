"""Redhelm Arzuros, arzuros deviant. The crimson helm: a red shell plate
capping the head and shoulders over the honey bear frame."""
from arzuros import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "redhelm-arzuros"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (188, 76, 54, 255)    # red helm shell
CONFIG["palette"]["p"] = (146, 52, 40, 255)    # darker red rim

# red helm capping the head and shoulders
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(4, 17)],
    6:  [(3, 20)],
    7:  [(3, 20)],
    8:  [(3, 21)],
}

CONFIG["fills"] = [
    # red helm shell with a darker rim
    ("runs", [(5, 4, 17), (6, 3, 20), (7, 3, 20), (8, 3, 15)], "P"),
    ("runs", [(8, 16, 21), (9, 16, 22)], "p"),
    # the bear's face below the helm
    ("runs", [(9, 5, 10), (10, 4, 11)], "F"),
    ("put", 10, 6, "K"),
    # blue carapace patch on the back kept from the base
    ("runs", [(11, 14, 21), (12, 14, 22), (13, 14, 22), (14, 14, 22)],
     "P"),
    # belly shade
    ("runs", [(14, 5, 11), (15, 6, 11), (16, 7, 12)], "p"),
    # claws
    ("put", 21, 6, "W"),
    ("put", 21, 8, "W"),
    ("put", 21, 13, "W"),
    ("put", 21, 15, "W"),
    ("put", 21, 20, "W"),
    ("put", 21, 22, "W"),
]
