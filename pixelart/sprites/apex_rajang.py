"""Apex Rajang, rajang apex. The golden tyrant: deeper gold fur over the
rajang frame with both fists raised and a bigger mane."""
from rajang import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-rajang"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (226, 190, 66, 255)   # deeper gold fur
CONFIG["palette"]["g"] = (178, 144, 48, 255)   # darker gold

# bigger mane + raised fists
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(4, 6), (8, 12)],
    3:  [(3, 8), (8, 14)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(2, 4, 6), (2, 8, 12)], "D"),
]
