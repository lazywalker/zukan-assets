"""Fulgur Anjanath: the storm variant. Steel-blue body and the sail grown
into lightning rods: two gold spikes breaking above the sail's top edge."""
from anjanath import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "fulgur-anjanath"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (98, 118, 158, 255)
CONFIG["palette"]["p"] = (142, 162, 198, 255)
CONFIG["palette"]["G"] = (232, 198, 84, 255)
CONFIG["palette"]["O"] = (240, 150, 40, 255)

# sail spikes breaking above the top edge
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(14, 15), (19, 20)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # gold on the new spikes
    ("runs", [(0, 14, 15), (0, 19, 20)], "G"),
]
