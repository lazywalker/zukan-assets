"""Berserk Tetsucabra, tetsucabra deviant. The crimson crusher: blood-red
hide and the tusks grown into huge hooks."""
from tetsucabra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "berserk-tetsucabra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (188, 62, 50, 255)    # crimson hide
CONFIG["palette"]["D"] = (142, 42, 36, 255)    # darker crimson

# tusk hooks grown bigger
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(1, 18), (1, 1), (4, 4), (7, 7), (10, 10), (13, 13)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(8, 1, 1), (8, 4, 4), (8, 7, 7), (8, 10, 10),
              (8, 13, 13)], "W"),
]
