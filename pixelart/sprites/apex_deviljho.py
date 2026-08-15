"""Apex Deviljho, deviljho apex. The world eater enraged: darker emerald
over the pickle frame with the jaw even wider and scarred hide."""
from savage_deviljho import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-deviljho"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (48, 120, 66, 255)    # darker emerald
CONFIG["palette"]["D"] = (32, 84, 46, 255)     # darkest green

CONFIG["fills"] = list(_base["fills"]) + [
    # scar slashes across the jaw
    ("runs", [(7, 10, 11), (8, 12, 13)], "L", "G"),
]
