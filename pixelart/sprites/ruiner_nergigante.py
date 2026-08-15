"""Ruiner Nergigante, nergigante variant. The settled hunter: darker
black-brown spikes over the elder dragon frame, thorn arms heavier."""
from nergigante import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ruiner-nergigante"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (58, 48, 46, 255)     # darker black-brown bulk
CONFIG["palette"]["D"] = (42, 34, 34, 255)     # darkest shade
CONFIG["palette"]["S"] = (188, 128, 84, 255)   # dried-bone spikes
