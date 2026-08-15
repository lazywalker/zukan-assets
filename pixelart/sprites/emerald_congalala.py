"""Emerald Congalala, congalala subspecies. Emerald-green fur over the
pink baboon king frame, the face plate cooled to blue-slate."""
from congalala import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "emerald-congalala"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (118, 168, 96, 255)   # emerald fur
CONFIG["palette"]["D"] = (86, 130, 70, 255)    # darker green
CONFIG["palette"]["V"] = (56, 76, 88, 255)     # slate face plate
