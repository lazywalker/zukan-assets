"""Black Diablos: the charging female. Charcoal body and the twin horns
curved forward over the snout instead of sweeping straight up."""
from diablos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "black-diablos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (74, 64, 70, 255)
CONFIG["palette"]["o"] = (50, 44, 50, 255)
CONFIG["palette"]["W"] = (246, 242, 230, 255)  # bared fang

# forward-curved horns: both lean left over the snout, tips lower
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(3, 3), (32, 32)],
    2:  [(1, 3), (8, 8), (31, 33)],
    3:  [(1, 3), (7, 8), (31, 33)],
    4:  [(2, 4), (7, 8), (30, 34)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # white fang bared on the jaw
    ("put", 12, 3, "W"),
]
