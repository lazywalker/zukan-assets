"""Scorned Magnamalo, magnamalo deviation. Blue hellfire: deeper purple
armor, horn tips breaking one row higher, and blue flame spikes bursting
from the back ridge."""
from magnamalo import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "scorned-magnamalo"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (82, 48, 100, 255)    # deeper purple
CONFIG["palette"]["D"] = (56, 30, 72, 255)     # darker shade
CONFIG["palette"]["F"] = (110, 150, 230, 255)  # blue hellfire

# horn tips higher + blue flame spikes over the back ridge
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(3, 4), (7, 8)],
    2:  [(2, 5), (6, 9), (14, 15), (18, 19), (28, 29)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # blue flame on the new spikes and horn tips
    ("runs", [(0, 3, 4), (0, 7, 8), (2, 14, 15), (2, 18, 19)], "F"),
]
