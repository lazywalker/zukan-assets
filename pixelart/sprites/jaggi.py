"""Jaggi, small bird wyvern. The orange pack hunter: velocidrome's lunge
in hot orange with a small frill restored behind the jaw."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "jaggi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (208, 120, 60, 255)   # hot orange scales
CONFIG["palette"]["F"] = (232, 172, 84, 255)   # frill
CONFIG["palette"]["C"] = (230, 200, 160, 255)  # pale belly
CONFIG["palette"]["S"] = (156, 88, 44, 255)    # dark spots

# small frill restored behind the jaw
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(7, 10)],
    4:  [(6, 11)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 7, 10), (4, 6, 11)], "F"),
]
