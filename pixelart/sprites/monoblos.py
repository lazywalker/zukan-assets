"""Monoblos, flying wyvern. The single-horn drill: diablos' frame with one
great horn instead of the twin sweep."""
from diablos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "monoblos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (188, 116, 60, 255)   # sandy red hide
CONFIG["palette"]["o"] = (146, 88, 44, 255)    # darker hide

# one horn: the far horn behind removed, the drill horn kept
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(2, 3), (31, 33)],
    3:  [(2, 4), (31, 33)],
    4:  [(2, 5), (30, 34)],
    5:  [(2, 5), (30, 34)],
}
