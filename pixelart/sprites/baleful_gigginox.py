"""Baleful Gigginox, gigginox subspecies. Night-purple body with a
green-pale crest over the cave stalker frame."""
from gigginox import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "baleful-gigginox"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (86, 62, 104, 255)    # night-purple body
CONFIG["palette"]["D"] = (62, 42, 78, 255)     # darker purple
CONFIG["palette"]["C"] = (186, 208, 168, 255)  # pale green crest
