"""Uroktor, leviathan. The lava pup: epioth's little frame in a red-hot
coat with dark lava-rock spikes."""
from epioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "uroktor"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (190, 88, 58, 255)    # red-hot scales
CONFIG["palette"]["D"] = (148, 62, 42, 255)    # darker red
CONFIG["palette"]["C"] = (232, 170, 120, 255)  # warm belly

# lava-rock spikes along the back
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(0, 12), (14, 14), (18, 18)],
    9:  [(0, 18), (13, 13), (17, 17)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(8, 14, 14), (8, 18, 18), (9, 13, 13), (9, 17, 17)], "D"),
]
