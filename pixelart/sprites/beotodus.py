"""Beotodus, piscine wyvern subspecies. The frosted mud fish: pale ice
coat over the jyuratodus frame, fins turned to ice-blue blades."""
from jyuratodus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "beotodus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (170, 186, 202, 255)  # ice coat
CONFIG["palette"]["D"] = (134, 152, 172, 255)  # darker ice
CONFIG["palette"]["R"] = (108, 170, 214, 255)  # ice-blue fins
CONFIG["palette"]["C"] = (214, 226, 238, 255)  # pale belly
