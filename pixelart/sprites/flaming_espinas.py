"""Flaming Espinas, espinas variant. The burning thorn: ember-red hide
with white-hot thorns over the thorn wyvern frame."""
from espinas import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "flaming-espinas"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (172, 78, 56, 255)    # ember hide
CONFIG["palette"]["D"] = (132, 54, 42, 255)    # darker ember
CONFIG["palette"]["R"] = (246, 196, 96, 255)   # white-hot thorns
CONFIG["palette"]["C"] = (232, 168, 120, 255)  # warm chest
