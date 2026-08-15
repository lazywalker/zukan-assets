"""Girros, small pack fanged wyvern. The great-girros' scout: grey-green
body, head lowered in a stalk, and a ridge of yellow neck spikes rising
over the back. Jagras derive with raised spikes and a stalker palette."""
from jagras import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "girros"
CONFIG["compare_to"] = "../icons/mhw/girros.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (105, 110, 95, 255)   # grey-green scales
CONFIG["palette"]["D"] = (75, 80, 68, 255)     # darker bands
CONFIG["palette"]["O"] = (170, 165, 130, 255)  # pale belly

# stalker pose + yellow spike ridge over the back
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(2, 5), (11, 11), (14, 14)],
    6:  [(1, 7), (10, 10), (13, 13), (16, 16)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # yellow spikes
    ("runs", [(5, 11, 11), (5, 14, 14), (6, 10, 10), (6, 13, 13),
              (6, 16, 16)], "Y"),
]
