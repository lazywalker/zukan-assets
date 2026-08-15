"""Apex Tigrex, tigrex apex. The roar tyrant: darker orange hide with
black widening stripes over the tigrex frame."""
from tigrex import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-tigrex"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (198, 118, 40, 255)   # darker orange hide
CONFIG["palette"]["N"] = (40, 38, 44, 255)     # wider black stripes

# stripes widened: extra band runs painted over the body
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(7, 17, 18), (8, 17, 18), (9, 16, 17), (10, 19, 20),
              (11, 18, 19), (12, 21, 22)], "N"),
]
