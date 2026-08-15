"""Acidic Glavenus, glavenus subspecies. The toxic swordsman: teal body,
acid-green blade held higher with its edge dripping, and the jaw split
open in a hiss."""
from glavenus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "acidic-glavenus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (70, 130, 112, 255)   # teal body
CONFIG["palette"]["D"] = (48, 94, 82, 255)     # darker teal
CONFIG["palette"]["N"] = (40, 60, 84, 255)     # dark slate plates
CONFIG["palette"]["B"] = (152, 192, 92, 255)   # acid-green blade
CONFIG["palette"]["E"] = (98, 140, 60, 255)    # acid edge

# jaw split open in a hiss: the gap runs down the front of the face
CONFIG["spans"] = {
    **_base["spans"],
    11: [(1, 8), (10, 29)],
    12: [(1, 8), (10, 28)],
    13: [(2, 8), (10, 26)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # lower fangs in the hissing gap
    ("put", 11, 10, "W"),
    ("put", 12, 10, "W"),
    # acid drip on the blade edge
    ("put", 8, 28, "E"),
]
