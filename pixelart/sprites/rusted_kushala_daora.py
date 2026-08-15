"""Rusted Kushala Daora, kushala-daora subspecies. The corroded storm:
rust-brown plating over the storm dragon frame, the sheen gone."""
from kushala_daora import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rusted-kushala-daora"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (122, 96, 78, 255)    # rust-brown plating
CONFIG["palette"]["D"] = (92, 70, 58, 255)     # darker rust
CONFIG["palette"]["N"] = (58, 46, 40, 255)     # dark corroded horns
