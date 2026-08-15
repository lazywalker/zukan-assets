"""Shattered Monoblos, monoblos variant. The broken drill: monoblos' frame
with the horn snapped mid-shaft and scarred hide."""
from monoblos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shattered-monoblos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (98, 74, 62, 255)     # broken darker hide
CONFIG["palette"]["o"] = (72, 52, 44, 255)     # darker hide

# horn snapped: tip removed, stump squared off
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(32, 32)],
    2:  [(2, 2), (31, 33)],
    3:  [(2, 3), (31, 33)],
    4:  [(2, 4), (30, 34)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # scar slashes
    ("runs", [(11, 16, 17), (12, 20, 21)], "M", "O"),
]
