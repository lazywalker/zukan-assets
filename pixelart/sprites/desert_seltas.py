"""Desert Seltas, seltas subspecies. Sand-yellow armor over the horned
beetle frame, the wing shell turned to pale sandstone."""
from seltas import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "desert-seltas"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (196, 168, 96, 255)   # sand-yellow armor
CONFIG["palette"]["D"] = (156, 130, 70, 255)   # darker sand
CONFIG["palette"]["S"] = (216, 198, 152, 255)  # pale sandstone shell
