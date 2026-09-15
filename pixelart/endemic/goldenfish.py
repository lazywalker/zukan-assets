"""Goldenfish: bright gold with orange fins, the classic shiny pond fish."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "goldenfish"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (232, 180, 60, 255)   # gold body
CONFIG["palette"]["D"] = (196, 130, 34, 255)   # orange fins
CONFIG["palette"]["C"] = (248, 224, 140, 255)  # pale belly
