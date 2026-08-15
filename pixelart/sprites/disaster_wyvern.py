"""Disaster Wyvern, flying wyvern. The ember thorn: espinas' thorn frame
in scorched red-black with charred thorn tips."""
from espinas import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "disaster-wyvern"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (88, 62, 58, 255)     # scorched hide
CONFIG["palette"]["D"] = (64, 44, 42, 255)     # darker scorched
CONFIG["palette"]["R"] = (236, 120, 56, 255)   # ember thorn tips
