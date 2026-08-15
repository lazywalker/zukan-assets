"""Guren Shen Gaoren, shen-gaoren variant. The crimson siege: red-hot
carapace over the skull-tower giant with glowing socket eyes."""
from shen_gaoren import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "guren-shen-gaoren"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (196, 78, 52, 255)    # red-hot carapace
CONFIG["palette"]["D"] = (148, 54, 38, 255)    # darker red
CONFIG["palette"]["C"] = (236, 214, 190, 255)  # brighter skulls
