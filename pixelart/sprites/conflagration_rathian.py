"""Conflagration Rathian, rathian variant. The ember queen: hot red scales
over the rathian frame with a flame-yellow membrane."""
from rathian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "conflagration-rathian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (202, 84, 52, 255)    # hot red scales
CONFIG["palette"]["D"] = (156, 60, 40, 255)    # darker red
CONFIG["palette"]["C"] = (240, 188, 84, 255)   # flame-yellow membrane
