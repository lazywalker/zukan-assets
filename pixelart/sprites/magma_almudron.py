"""Magma Almudron, almudron subspecies. The magma swimmer: dark basalt
body over the mud-swimmer frame, the frill turned lava-orange, magma
veins glowing along the flanks."""
from almudron import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "magma-almudron"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (72, 64, 66, 255)     # basalt body
CONFIG["palette"]["D"] = (52, 46, 48, 255)     # darker basalt
CONFIG["palette"]["R"] = (244, 126, 48, 255)   # lava frill
CONFIG["palette"]["M"] = (240, 150, 60, 255)   # magma veins
CONFIG["palette"]["C"] = (188, 122, 70, 255)   # warm belly

CONFIG["fills"] = list(_base["fills"]) + [
    # magma veins glowing along the flanks
    ("runs", [(10, 25, 27), (11, 27, 29), (12, 24, 26)], "M", "D"),
]
