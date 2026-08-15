"""Molten Tigrex, tigrex deviant. The magma brute: blackened hide with
lava-orange stripes that glow over the tigrex frame."""
from tigrex import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "molten-tigrex"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (58, 52, 54, 255)     # blackened hide
CONFIG["palette"]["N"] = (244, 122, 46, 255)   # lava-orange stripes
CONFIG["palette"]["M"] = (232, 176, 110, 255)  # hot pale jaw
CONFIG["palette"]["C"] = (250, 210, 90, 255)   # molten eye
