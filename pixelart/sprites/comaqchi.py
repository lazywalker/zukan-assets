"""Comaqchi, neopteron. The red scout: vespoid's frame in a hot red-orange
coat with one big dark eye across the face."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "comaqchi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (208, 88, 56, 255)    # hot red-orange body
CONFIG["palette"]["Y"] = (234, 160, 88, 255)   # warm bands
CONFIG["palette"]["D"] = (158, 60, 40, 255)    # darker shade

CONFIG["fills"] = list(_base["fills"]) + [
    # one big dark eye swallowing the face, warm glint
    ("runs", [(4, 11, 14), (5, 11, 14)], "K", "R"),
    ("runs", [(4, 9, 10), (4, 15, 16), (5, 9, 10), (5, 15, 16)], "K", "P"),
    ("put", 4, 12, "Y"),
]
