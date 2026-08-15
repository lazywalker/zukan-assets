"""Lunastra, elder dragon. Teostra's mate: blue-purple body with the mane
flared into extra pale spikes around the ring and the horns sweeping one
row taller than the king's."""
from teostra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lunastra"
CONFIG["compare_to"] = "../icons/mhfu/lunastra.png"
CONFIG["palette"] = {
    ".": (0, 0, 0, 0),
    "K": (24, 20, 22, 255),
    "R": (110, 90, 180, 255),   # blue-purple body
    "D": (80, 62, 140, 255),    # dark purple wings
    "M": (205, 200, 230, 255),  # pale blue mane / tail tuft
    "H": (90, 70, 130, 255),    # dark horns
    "E": (150, 180, 240, 255),  # blue ember dots
    "W": (246, 242, 230, 255),
}

# taller horns + mane flaring into spikes at the ring's edge
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(8, 9), (14, 15)],
    3:  [(8, 10), (14, 16), (6, 6), (12, 12), (17, 17)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # dark horn tips, one row up
    ("runs", [(2, 8, 9), (2, 14, 15)], "H"),
    # pale mane spikes flaring out
    ("runs", [(3, 6, 6), (3, 12, 12), (3, 17, 17)], "M"),
]
