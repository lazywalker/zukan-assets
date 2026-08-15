"""Crimson Qurupeco, qurupeco subspecies. Red plumage over the songbird
frame, a taller crest, and a deeper purple tail."""
from qurupeco import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "crimson-qurupeco"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (196, 68, 58, 255)    # red plumage
CONFIG["palette"]["D"] = (152, 48, 42, 255)    # darker red
CONFIG["palette"]["P"] = (86, 56, 110, 255)    # deep purple tail

# taller crest
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(4, 6)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(2, 4, 6)], "R"),
]
