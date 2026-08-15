"""Bloodbath Diablos, diablos deviant. The bloodied brawler: crimson-black
hide, horns cracked and bent, and pale scars over the diablos frame."""
from diablos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bloodbath-diablos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (122, 40, 40, 255)    # crimson-black hide
CONFIG["palette"]["o"] = (88, 26, 30, 255)     # darker crimson

# horns cracked: the main horn breaks mid-shaft, tip bent forward
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(2, 2), (32, 32)],
    2:  [(2, 2), (4, 4), (8, 8), (31, 33)],
    3:  [(2, 4), (7, 8), (31, 33)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # pale scar slashes on the shell
    ("runs", [(11, 16, 17), (12, 20, 21), (13, 18, 19)], "M", "O"),
]
