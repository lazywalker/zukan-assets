"""Pariapuria, flying wyvern. The mud gulper: jyuratodus' mud fish frame in
a bloated purple-brown with a wider maw."""
from jyuratodus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pariapuria"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (146, 118, 126, 255)  # purple-brown hide
CONFIG["palette"]["D"] = (112, 88, 96, 255)    # darker purple
CONFIG["palette"]["R"] = (188, 148, 130, 255)  # pale pink fins
CONFIG["palette"]["C"] = (222, 196, 178, 255)  # pale belly

# wider maw
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(0, 19), (13, 24)],
    9:  [(0, 18), (12, 26)],
    10: [(0, 17), (11, 28)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 8, 1, "W"),
    ("put", 8, 10, "W"),
]
