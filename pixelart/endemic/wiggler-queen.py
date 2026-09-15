"""Wiggler queen: the big wiggler with a flower crown on her head."""
from wiggler import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wiggler-queen"
CONFIG["size"] = (34, 24)
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (226, 130, 160, 255)  # flower petals

CONFIG["spans"] = {
    **_base["spans"],
    8: [(3, 4), (7, 8)],
    9: [(2, 9)],
    10: [(2, 10)],
    11: [(2, 15)],
    12: [(2, 20)],
    13: [(2, 25)],
    14: [(2, 30)],
    15: [(2, 31)],
    16: [(3, 31)],
    17: [(4, 31)],
    18: [(6, 30)],
    19: [(8, 28)],
    20: [(10, 26)],
}

CONFIG["fills"] = [
    op for op in _base["fills"] if not (op[0] == "runs" and op[1][0] == (10, 2, 6))
] + [
    # the flower crown
    ("runs", [(8, 3, 4), (8, 7, 8), (9, 2, 9)], "F"),
    ("put", 9, 5, "Y"),
    ("put", 9, 6, "Y"),
    # head stays red beneath the crown
    ("runs", [(10, 2, 9), (11, 2, 9)], "R"),
    ("put", 11, 5, "W"),
    ("put", 11, 6, "K"),
]
