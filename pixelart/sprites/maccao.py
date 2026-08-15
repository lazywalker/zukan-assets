"""Maccao, small bird wyvern. The green kicker: a green lunge frame with a
feather crest on the skull, orange-red legs, and spots along the back."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "maccao"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (112, 152, 92, 255)   # green scales
CONFIG["palette"]["F"] = (86, 120, 70, 255)    # dark crest
CONFIG["palette"]["C"] = (200, 214, 176, 255)  # pale belly
CONFIG["palette"]["S"] = (76, 106, 60, 255)    # dark spots
CONFIG["palette"]["V"] = (214, 96, 60, 255)    # orange-red legs

# feather crest on the skull
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(7, 9)],
    4:  [(6, 9)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 7, 9), (4, 6, 9)], "F"),
    # orange-red legs
    ("runs", [(9, 1, 12), (10, 1, 12)], "V", "O"),
]
