"""Comaqchi, neopteron. The red scout: vespoid's frame in a hot red-orange
coat with a big dark eye."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "comaqchi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (208, 88, 56, 255)    # hot red-orange body
CONFIG["palette"]["Y"] = (234, 160, 88, 255)   # warm bands
CONFIG["palette"]["D"] = (158, 60, 40, 255)    # darker shade

# big dark eye
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(7, 13), (12, 13)],
    5:  [(6, 14), (13, 15)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(5, 8, 9)], "K"),
    ("put", 5, 10, "K"),
]
