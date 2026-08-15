"""Risen Kushala Daora, kushala-daora variant. The wind ascended: brighter
steel over the storm dragon frame with a glowing white wind ruff."""
from kushala_daora import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "risen-kushala-daora"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (188, 190, 196, 255)  # brighter steel
CONFIG["palette"]["D"] = (148, 150, 158, 255)  # darker steel
CONFIG["palette"]["N"] = (98, 100, 112, 255)   # lighter horns
CONFIG["palette"]["B"] = (190, 216, 240, 255)  # glowing white wind
