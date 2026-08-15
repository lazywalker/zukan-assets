"""Poikilos Lightenna, lightenna variant. The golden mirror: gold plating
over the silver beetle frame."""
from lightenna import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "poikilos-lightenna"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (214, 176, 88, 255)   # gold plating
CONFIG["palette"]["Y"] = (244, 214, 130, 255)  # bright gold sheen
CONFIG["palette"]["D"] = (170, 134, 62, 255)   # darker gold
