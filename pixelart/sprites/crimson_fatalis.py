"""Crimson Fatalis, fatalis subspecies. The red wyvern: burning crimson
scales over the black dragon frame with a hotter chest glow."""
from fatalis import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "crimson-fatalis"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (168, 56, 48, 255)    # crimson scales
CONFIG["palette"]["D"] = (126, 40, 38, 255)    # darker crimson
CONFIG["palette"]["C"] = (216, 120, 78, 255)   # hotter chest glow
