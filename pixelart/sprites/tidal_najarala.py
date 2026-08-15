"""Tidal Najarala, najarala subspecies. Ice-blue coils over the flute
serpent frame, the flutes turned to pale ice blades."""
from najarala import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "tidal-najarala"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (108, 138, 176, 255)  # ice-blue coils
CONFIG["palette"]["D"] = (80, 106, 142, 255)   # darker blue
CONFIG["palette"]["F"] = (196, 220, 238, 255)  # ice flutes
CONFIG["palette"]["R"] = (150, 190, 224, 255)  # blue flute tips
CONFIG["palette"]["C"] = (208, 222, 238, 255)  # pale belly

# ice blades: flutes grow into straight pale towers, no waist
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(12, 15), (19, 22), (27, 29), (39, 41)],
    5:  [(1, 8), (12, 15), (19, 22), (26, 29), (39, 41)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the towers are pale ice with a blue tip
    ("runs", [(4, 12, 15), (4, 19, 22), (4, 27, 29), (4, 39, 41)], "F"),
    ("runs", [(4, 15, 15), (4, 22, 22), (4, 29, 29), (4, 41, 41)], "R",
     "F"),
    ("runs", [(5, 15, 15), (5, 22, 22), (5, 29, 29), (5, 41, 41)], "F"),
]
