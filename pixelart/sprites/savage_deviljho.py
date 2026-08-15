"""Savage Deviljho, deviljho deviation. The emerald berserker: brighter
green body over the pickle frame, the massive jaw grown past the snout
tip, and scarred pale patches across the face."""
from deviljho import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "savage-deviljho"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (66, 158, 88, 255)    # emerald body
CONFIG["palette"]["D"] = (44, 112, 62, 255)    # darker emerald
CONFIG["palette"]["L"] = (130, 200, 130, 255)  # pale belly

# jaw grown past the snout, head bulked
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(1, 9), (20, 21)],
    8:  [(0, 13), (14, 26), (25, 33)],
    9:  [(0, 13), (12, 34)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # pale scars across the jaw
    ("runs", [(6, 9, 10), (7, 10, 11), (8, 11, 12)], "L"),
]
