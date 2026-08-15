"""Cortos, wingdrake. The frost glider: mernos' glide frame in ice-white
with a cold blue wing."""
from mernos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "cortos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (214, 220, 228, 255)  # ice-white body
CONFIG["palette"]["D"] = (176, 186, 200, 255)  # darker ice
CONFIG["palette"]["B"] = (150, 176, 208, 255)  # cold blue wing
CONFIG["palette"]["R"] = (196, 214, 232, 255)  # pale crest
