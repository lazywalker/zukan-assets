"""Dung beetle: a dark beetle rolling a big ball of dung in front of it;
the ball is the identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dung-beetle"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (86, 70, 54, 255)     # dark brown shell
CONFIG["palette"]["D"] = (58, 46, 36, 255)     # darker
CONFIG["palette"]["C"] = (150, 116, 82, 255)   # dung ball

CONFIG["spans"] = {
    **_base["spans"],
    12: [(0, 2), (3, 24)],
    13: [(0, 3), (3, 24)],
    14: [(0, 3), (4, 23)],
    15: [(0, 3), (5, 22)],
    16: [(0, 2), (6, 20)],
    17: [(1, 1), (8, 10), (14, 16), (19, 21)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the dung ball with speckles
    ("runs", [(12, 0, 2), (13, 0, 3), (14, 0, 3), (15, 0, 3), (16, 0, 2)],
     "C"),
    ("put", 13, 1, "D"),
    ("put", 15, 1, "D"),
]
