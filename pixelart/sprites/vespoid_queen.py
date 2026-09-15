"""Vespoid Queen, neopteron. The queen wasp: a big vespoid with a three
point crown, a longer abdomen, and brighter bands."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "vespoid-queen"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (188, 92, 66, 255)    # richer red body
CONFIG["palette"]["Y"] = (240, 196, 84, 255)   # brighter bands

# three point crown, longer abdomen
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(8, 9), (12, 13), (16, 17)],
    17: [(11, 14)],
    18: [(11, 14)],
    19: [(12, 13)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(1, 12, 13)], "D"),
    ("runs", [(19, 12, 13)], "Y"),
]
