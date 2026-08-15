"""Drilltusk Tetsucabra, tetsucabra deviant. The ice borer: steel-blue
hide and the tusks fused into a pale drill spike on the jaw."""
from tetsucabra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "drilltusk-tetsucabra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (88, 108, 140, 255)   # steel-blue hide
CONFIG["palette"]["D"] = (62, 80, 108, 255)    # darker blue

# drill spike fused on the jaw tip
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(0, 18), (19, 20)],
    10: [(0, 18), (18, 21)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # pale drill cone at the jaw tip
    ("runs", [(9, 0, 3), (10, 0, 3), (11, 0, 2)], "W"),
]
