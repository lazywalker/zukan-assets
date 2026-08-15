"""Apex Tidal Najarala, tidal-najarala apex. The frozen choir: darker ice
coils over the flute serpent frame with every flute lit pale blue."""
from tidal_najarala import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-tidal-najarala"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (88, 116, 156, 255)   # darker ice coils
CONFIG["palette"]["D"] = (64, 88, 124, 255)    # darkest blue
CONFIG["palette"]["F"] = (226, 240, 250, 255)  # lit pale flutes

# the frozen choir: flutes grow into two-row lit spires, no waist
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(12, 15), (19, 22), (27, 29), (39, 41)],
    5:  [(1, 8), (12, 15), (19, 22), (26, 29), (39, 41)],
    3:  [(13, 14), (20, 21), (28, 28), (40, 40)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the spires lit pale blue to the tip
    ("runs", [(4, 12, 15), (4, 19, 22), (4, 27, 29), (4, 39, 41)], "F"),
    ("runs", [(5, 15, 15), (5, 22, 22), (5, 29, 29), (5, 41, 41)], "F"),
    ("runs", [(3, 13, 14), (3, 20, 21), (3, 28, 28), (3, 40, 40)], "F"),
]
