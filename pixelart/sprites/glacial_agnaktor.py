"""Glacial Agnaktor, agnaktor subspecies. Frozen armor: the plated frame
in dark blue with cyan glow seams, ice-grey beak and belly, white frozen
eye plates, and ice spikes bristling above the head plates."""
from agnaktor import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "glacial-agnaktor"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (52, 68, 100, 255)    # dark blue plate
CONFIG["palette"]["D"] = (38, 50, 76, 255)     # darker blue shade
CONFIG["palette"]["O"] = (120, 190, 215, 255)  # cyan glow seams
CONFIG["palette"]["C"] = (168, 180, 190, 255)  # ice-grey beak / belly
CONFIG["palette"]["E"] = (120, 132, 142, 255)  # darker ice shade
CONFIG["palette"]["Y"] = (225, 240, 245, 255)  # white frozen eye plates

# ice spikes bristling above the head plates
CONFIG["spans"] = {
    **_base["spans"],
    1: [(12, 12), (15, 15), (20, 20), (23, 23)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(1, 12, 12), (1, 15, 15), (1, 20, 20), (1, 23, 23)], "W"),
]
