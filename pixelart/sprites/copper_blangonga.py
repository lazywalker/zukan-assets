"""Copper Blangonga, blangonga subspecies. Copper-bronze fur over the
whisker chieftain frame with a deeper red mustache."""
from blangonga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "copper-blangonga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (198, 152, 104, 255)  # copper fur
CONFIG["palette"]["D"] = (158, 118, 78, 255)   # darker copper
CONFIG["palette"]["V"] = (128, 78, 96, 255)    # plum face
CONFIG["palette"]["R"] = (238, 128, 48, 255)   # hot orange whiskers
