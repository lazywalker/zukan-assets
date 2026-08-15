"""Ash Kecha Wacha, kecha-wacha subspecies. Ash-grey fur over the acrobat
frame with pale blue ear rings."""
from kecha_wacha import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ash-kecha-wacha"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (138, 132, 126, 255)  # ash-grey fur
CONFIG["palette"]["D"] = (106, 100, 96, 255)   # darker ash
CONFIG["palette"]["E"] = (150, 176, 196, 255)  # pale blue ear rings
