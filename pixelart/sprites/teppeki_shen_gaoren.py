"""Teppeki Shen Gaoren, shen-gaoren variant. The iron wall: grey-steel
carapace over the skull-tower giant with plated sockets."""
from shen_gaoren import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "teppeki-shen-gaoren"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (128, 128, 128, 255)  # steel carapace
CONFIG["palette"]["D"] = (96, 96, 96, 255)     # darker steel
