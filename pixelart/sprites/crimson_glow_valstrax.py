"""Crimson Glow Valstrax, valstrax variant. The burning comet: deeper
silver over the jet dragon frame with white-hot wing exhaust."""
from valstrax import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "crimson-glow-valstrax"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (204, 202, 210, 255)  # deeper silver
CONFIG["palette"]["D"] = (158, 156, 166, 255)  # darker silver
CONFIG["palette"]["R"] = (222, 78, 66, 255)    # burning crimson wings
CONFIG["palette"]["r"] = (250, 180, 120, 255)  # white-hot exhaust
CONFIG["palette"]["B"] = (216, 92, 88, 255)    # red-hot eyes
