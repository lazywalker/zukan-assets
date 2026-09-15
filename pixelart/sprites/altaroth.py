"""Altaroth, neopteron. The acid ant: green-brown body over the vespoid
frame with a white stripe band across the thorax and a dark head cap."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "altaroth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (96, 110, 70, 255)    # green-brown body
CONFIG["palette"]["Y"] = (228, 226, 214, 255)  # white stripe band
CONFIG["palette"]["D"] = (68, 80, 50, 255)     # darker shade

CONFIG["fills"] = list(_base["fills"]) + [
    # white stripe band over the thorax
    ("runs", [(8, 8, 17), (9, 9, 16)], "Y", "R"),
    # dark head cap
    ("runs", [(2, 10, 15), (3, 9, 16)], "D", "R"),
]
