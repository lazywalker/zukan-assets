"""The yellow spiritbird: bright golden plumage."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "yellow-spiritbird"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (236, 210, 90, 255)
CONFIG["palette"]["D"] = (184, 158, 54, 255)
CONFIG["palette"]["C"] = (250, 238, 170, 255)
