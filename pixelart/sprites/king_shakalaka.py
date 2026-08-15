"""King Shakalaka, lynian. The mask king: shakalaka's masked frame grown
bigger with a golden crown and a heavier club."""
from shakalaka import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "king-shakalaka"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (188, 132, 96, 255)   # deeper tan fur
CONFIG["palette"]["N"] = (172, 70, 40, 255)    # deep red mask
CONFIG["palette"]["T"] = (208, 168, 74, 255)   # golden club
CONFIG["palette"]["R"] = (238, 200, 90, 255)   # crown gold

# golden crown spikes
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(5, 6), (8, 9), (11, 12)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(0, 5, 6), (0, 8, 9), (0, 11, 12)], "R"),
]
