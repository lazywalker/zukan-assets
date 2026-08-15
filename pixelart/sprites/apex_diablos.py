"""Apex Diablos, diablos apex. The blackened tyrant: charcoal hide and the
twin horns grown wider, over the diablos frame."""
from diablos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-diablos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (74, 66, 62, 255)     # charcoal hide
CONFIG["palette"]["o"] = (52, 46, 44, 255)     # darker charcoal

# twin horns grown wider and taller
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(2, 4), (32, 32)],
    2:  [(1, 4), (7, 9), (31, 33)],
    3:  [(1, 5), (7, 9), (31, 33)],
    4:  [(2, 5), (7, 9), (30, 34)],
    5:  [(2, 5), (7, 8), (30, 34)],
}
