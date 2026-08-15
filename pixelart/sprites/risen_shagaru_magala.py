"""Risen Shagaru Magala, shagaru-magala variant. The heaven ascended:
brighter gold scales over the angel dragon frame with radiant wing rays."""
from shagaru_magala import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "risen-shagaru-magala"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (236, 198, 92, 255)   # radiant gold scales
CONFIG["palette"]["D"] = (192, 152, 62, 255)   # darker gold
CONFIG["palette"]["V"] = (246, 226, 130, 255)  # radiant wing rays
CONFIG["palette"]["C"] = (248, 238, 190, 255)  # pale chest
