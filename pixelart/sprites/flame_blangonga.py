"""Flame Blangonga, blangonga variant. The fire whiskers: orange-tan fur
over the whisker chieftain frame with the mustache turned flame."""
from blangonga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "flame-blangonga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (216, 152, 92, 255)   # orange-tan fur
CONFIG["palette"]["D"] = (174, 116, 66, 255)   # darker tan
CONFIG["palette"]["R"] = (244, 116, 48, 255)   # flame whiskers
