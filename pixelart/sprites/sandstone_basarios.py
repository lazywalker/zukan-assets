"""Sandstone Basarios, basarios variant. Tan sandstone rock over the
sleeping boulder frame."""
from basarios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "sandstone-basarios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (196, 168, 118, 255)  # sandstone rock
CONFIG["palette"]["D"] = (156, 130, 86, 255)   # darker sandstone
CONFIG["palette"]["C"] = (228, 208, 164, 255)  # pale sand face
