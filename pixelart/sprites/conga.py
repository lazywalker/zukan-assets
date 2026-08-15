"""Conga, fanged beast. The small pack baboon: congalala's hunched frame
shrunk to a compact body with a smaller face plate."""
from congalala import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "conga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (158, 110, 92, 255)   # brown-pink fur
CONFIG["palette"]["D"] = (122, 80, 66, 255)    # darker brown

# compact body: sides pulled in
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(4, 17)],
    6:  [(3, 18)],
    7:  [(3, 19)],
    8:  [(2, 20)],
    9:  [(2, 20)],
    10: [(2, 21)],
    11: [(1, 21)],
    12: [(1, 21)],
    13: [(1, 21)],
    14: [(2, 21)],
    15: [(2, 20)],
    16: [(3, 19)],
    17: [(4, 18)],
    18: [(5, 16), (17, 20)],
    19: [(7, 14), (17, 20)],
    20: [(7, 13), (16, 19)],
    21: [(7, 7), (9, 9), (11, 11), (13, 13), (16, 16), (18, 18)],
}
