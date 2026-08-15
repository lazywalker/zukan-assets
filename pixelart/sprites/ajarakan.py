"""Ajarakan, fanged beast. The ember-maned guardian: doshaguma's bulk in
burning orange fur with a crimson face and a rose-crystal crest."""
from doshaguma import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ajarakan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (222, 126, 58, 255)   # burning orange fur
CONFIG["palette"]["D"] = (180, 92, 44, 255)    # darker ember
CONFIG["palette"]["R"] = (206, 84, 96, 255)    # crimson face
CONFIG["palette"]["K2"] = (110, 44, 60, 255)   # dark rose eyes
CONFIG["palette"]["W"] = (244, 196, 216, 255)  # rose crystal claws
