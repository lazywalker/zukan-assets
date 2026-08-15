"""Giadrome, small bird wyvern. The frost leader: white-blue scales over
the lunge frame with icy crest spikes and a pale blue belly."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "giadrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (226, 232, 240, 255)  # white-blue scales
CONFIG["palette"]["F"] = (168, 196, 224, 255)  # icy crest
CONFIG["palette"]["C"] = (196, 216, 234, 255)  # pale blue belly
CONFIG["palette"]["S"] = (140, 168, 200, 255)  # icy spots

# icy crest spikes
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(7, 10)],
    4:  [(6, 11)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 7, 10), (4, 6, 11)], "F"),
    ("put", 3, 10, "W"),
]
