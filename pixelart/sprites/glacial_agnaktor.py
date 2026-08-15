"""Glacial Agnaktor, agnaktor subspecies. Frozen armor: dark blue body,
ice-gray ash plates, and extra white-cyan spikes bristling along the
back ridge on top of the agnaktor beaked frame."""
from agnaktor import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "glacial-agnaktor"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (52, 68, 100, 255)    # dark blue body
CONFIG["palette"]["D"] = (38, 50, 76, 255)     # darker blue shade
CONFIG["palette"]["G"] = (168, 180, 190, 255)  # ice-gray ash plates
CONFIG["palette"]["Y"] = (225, 240, 245, 255)  # white frozen plates
CONFIG["palette"]["O"] = (120, 190, 215, 255)  # cyan eye / glow

# ice spikes bristling above the back ridge
CONFIG["spans"] = {
    **_base["spans"],
    6: [(1, 12), (14, 14), (17, 17), (24, 24), (28, 28)],
    7: [(1, 15), (17, 17), (20, 20), (24, 24), (28, 28)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # white tips on the ice spikes
    ("runs", [(6, 17, 17), (6, 24, 24), (6, 28, 28)], "W"),
]
