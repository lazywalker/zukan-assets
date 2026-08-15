"""Red Khezu, khezu subspecies. Red-raw flesh over the blind wyvern frame."""
from khezu import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "red-khezu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (214, 122, 104, 255)  # red-raw flesh
CONFIG["palette"]["D"] = (176, 90, 76, 255)    # darker red
CONFIG["palette"]["R"] = (132, 44, 40, 255)    # deep red mouth
