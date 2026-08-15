"""Elderfrost Gammoth, gammoth deviant. A silver-white mammoth with steel
blue trim and an ice-crusted trunk, over the gammoth frame."""
from gammoth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "elderfrost-gammoth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (238, 240, 246, 255)  # silver-white fur
CONFIG["palette"]["D"] = (196, 202, 214, 255)  # darker silver
CONFIG["palette"]["V"] = (118, 138, 172, 255)  # steel-blue face
CONFIG["palette"]["Y"] = (158, 190, 218, 255)  # ice-blue trim
