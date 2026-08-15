"""Boggi, small bird wyvern. The purple scavenger: jaggi's frame in a
bruised purple coat with a darker frill and pale spots."""
from jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "boggi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (122, 96, 140, 255)   # bruised purple scales
CONFIG["palette"]["F"] = (94, 72, 112, 255)    # dark purple frill
CONFIG["palette"]["C"] = (198, 186, 206, 255)  # pale belly
CONFIG["palette"]["S"] = (80, 60, 96, 255)     # dark spots

CONFIG["fills"] = list(_base["fills"]) + [
    # pale spots on the flank
    ("runs", [(10, 14, 15), (11, 16, 17)], "C"),
]
