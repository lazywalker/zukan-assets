"""Drilltusk Tetsucabra, tetsucabra deviant. The ice borer: steel-blue
hide and the tusks fused into a pale drill spike on the jaw."""
from tetsucabra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "drilltusk-tetsucabra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (88, 108, 140, 255)   # steel-blue hide
CONFIG["palette"]["D"] = (62, 80, 108, 255)    # darker blue

# drill cones fused onto the tusk islands: one row taller, one column wider
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(4, 6), (25, 27)],
    10: [(4, 6), (25, 27)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # cone tip reaching up onto the face
    ("put", 8, 5, "W"),
    ("put", 8, 26, "W"),
    # dark ridge down the outer flank of each cone
    ("runs", [(9, 6, 6), (10, 6, 6), (9, 25, 25), (10, 25, 25)], "D"),
]
