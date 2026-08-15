"""Baggi, small bird wyvern. The navy sleeper: a tall dark crest fin like
the great-baggi's, over the small lunge frame in sleepy navy."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "baggi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (86, 96, 136, 255)    # navy scales
CONFIG["palette"]["F"] = (56, 64, 100, 255)    # dark crest fin
CONFIG["palette"]["C"] = (176, 186, 210, 255)  # pale belly
CONFIG["palette"]["S"] = (50, 56, 86, 255)     # dark spots

# tall crest fin
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(7, 11)],
    4:  [(6, 12)],
    5:  [(5, 12)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 7, 11), (4, 6, 12), (5, 5, 9)], "F"),
]
