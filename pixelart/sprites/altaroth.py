"""Altaroth, neopteron. The acid ant: green-brown body with a white stripe
band over the vespoid frame, mandibles forward."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "altaroth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (96, 110, 70, 255)    # green-brown body
CONFIG["palette"]["Y"] = (228, 226, 214, 255)  # white stripe band
CONFIG["palette"]["D"] = (68, 80, 50, 255)     # darker shade

# mandibles forward at the head
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(4, 14), (12, 17)],
    7:  [(3, 14), (11, 18)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(6, 4, 5), (7, 3, 4)], "D"),
]
