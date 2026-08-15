"""Infernal Tartaronis, leviathan. The vine serpent: balahara's sand flower
frame in deep green with a thorned petal fan."""
from balahara import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "infernal-tartaronis"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (96, 128, 84, 255)    # deep green coils
CONFIG["palette"]["D"] = (70, 98, 62, 255)     # darker green
CONFIG["palette"]["S"] = (188, 210, 140, 255)  # pale thorned petals
CONFIG["palette"]["T"] = (140, 160, 100, 255)  # green chin
