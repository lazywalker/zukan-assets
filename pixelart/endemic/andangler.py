"""Andangler: a dark anglerfish with a glowing lure stalk hanging over its
fang-filled mouth."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "andangler"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (70, 76, 92, 255)     # dark body
CONFIG["palette"]["D"] = (48, 54, 68, 255)     # darker fins
CONFIG["palette"]["C"] = (120, 126, 140, 255)  # pale belly
CONFIG["palette"]["G"] = (240, 220, 120, 255)  # lure glow

CONFIG["spans"] = {
    **_base["spans"],
    4: [(7, 8)],
    5: [(6, 9), (8, 8)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # lure stalk with a glowing bulb
    ("runs", [(4, 7, 8), (5, 6, 8)], "D"),
    ("put", 4, 7, "G"),
    # jagged fangs under the mouth
    ("put", 11, 4, "W"),
    ("put", 12, 4, "W"),
    ("put", 12, 6, "W"),
]
