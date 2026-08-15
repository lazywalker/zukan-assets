"""Dreadking Rathalos, rathalos deviant. The sky tyrant: black-silver
scales over the rathalos frame with a hot orange membrane."""
from rathalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dreadking-rathalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (66, 60, 66, 255)     # black-silver scales
CONFIG["palette"]["D"] = (46, 42, 48, 255)     # darker black
CONFIG["palette"]["C"] = (238, 138, 58, 255)   # hot orange membrane
