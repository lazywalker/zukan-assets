"""Furious Rajang, rajang deviation. The super ape: white fur blazing over
the rajang frame, lightning-blue eyes, and both fists crackling."""
from rajang import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "furious-rajang"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (238, 236, 228, 255)  # blazing white fur
CONFIG["palette"]["g"] = (198, 196, 188, 255)  # fur shade
CONFIG["palette"]["D"] = (48, 40, 36, 255)     # darker face / mane
CONFIG["palette"]["R"] = (96, 170, 236, 255)   # lightning-blue eyes

# crackling fists raised
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(6, 7), (10, 11)],
    3:  [(4, 6), (8, 12), (14, 15)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # lightning sparks off the crown and fists
    ("runs", [(2, 6, 7), (2, 10, 11), (3, 14, 15)], "R"),
    ("runs", [(19, 5, 10), (20, 5, 10)], "R", "D"),
    ("put", 21, 5, "R"),
    ("put", 21, 8, "R"),
]
