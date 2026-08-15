"""Shamos, small pack fanged wyvern. The blind cave stalker: pale grey
body, orange head, no eyes, and an underbite jaw with raised lower fangs.
Jagras derive with an underbite silhouette."""
from jagras import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shamos"
CONFIG["compare_to"] = "../icons/mhw/shamos.png"

CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (172, 175, 168, 255)  # pale grey scales
CONFIG["palette"]["D"] = (135, 138, 132, 255)  # darker bands
CONFIG["palette"]["Y"] = (215, 120, 70, 255)   # orange head / spikes
CONFIG["palette"]["O"] = (150, 152, 146, 255)  # grey belly

# underbite: lower jaw bumps up into the mouth gap
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(0, 3), (6, 18)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # orange head, no eyes
    ("runs", [(5, 2, 5), (6, 1, 7), (7, 0, 9)], "Y"),
    # underbite fangs
    ("put", 8, 0, "W"),
    ("put", 8, 2, "W"),
]
