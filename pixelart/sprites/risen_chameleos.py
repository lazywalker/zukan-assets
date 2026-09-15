"""Risen Chameleos, chameleos variant. The haze ascended: brighter pink
skin over the trickster frame with a glowing white frill."""
from chameleos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "risen-chameleos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (228, 174, 196, 255)  # brighter pink skin
CONFIG["palette"]["D"] = (188, 134, 160, 255)  # darker pink
CONFIG["palette"]["V"] = (158, 108, 182, 255)  # brighter frills
