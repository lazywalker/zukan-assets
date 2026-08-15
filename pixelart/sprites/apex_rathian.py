"""Apex Rathian, rathian apex. The blackened queen: charcoal-green scales
over the rathian frame with a burning rose membrane."""
from rathian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-rathian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (64, 74, 64, 255)     # charcoal-green scales
CONFIG["palette"]["D"] = (44, 52, 44, 255)     # darker charcoal
CONFIG["palette"]["C"] = (216, 106, 130, 255)  # burning rose membrane
