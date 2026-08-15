"""Dreadqueen Rathian, rathian deviant. The poison empress: deep purple
scales over the rathian frame with a toxic pink membrane."""
from rathian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dreadqueen-rathian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (110, 66, 122, 255)   # deep purple scales
CONFIG["palette"]["D"] = (80, 46, 92, 255)     # darker purple
CONFIG["palette"]["C"] = (236, 138, 172, 255)  # toxic pink membrane
