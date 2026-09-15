"""Berserk Tetsucabra, tetsucabra deviant. The crimson crusher: blood-red
hide and the tusks grown into huge hooks."""
from tetsucabra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "berserk-tetsucabra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (188, 62, 50, 255)    # crimson hide
CONFIG["palette"]["D"] = (142, 42, 36, 255)    # darker crimson

# tusk hooks grown huge, tips hooking outward past the jaw
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(3, 5), (28, 30)],
    10: [(3, 5), (28, 30)],
    11: [(1, 1), (2, 29), (31, 31)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # hook bases rising through the upper jaw
    ("runs", [(8, 3, 5), (8, 28, 30)], "W", "O"),
    ("runs", [(9, 3, 5), (10, 3, 5), (9, 28, 30), (10, 28, 30)], "W"),
    # outward hook tips
    ("put", 11, 1, "W"),
    ("put", 11, 31, "W"),
]
