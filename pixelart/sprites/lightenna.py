"""Lightenna, neopteron. The mirror beetle: vespoid's frame in polished
silver plating with a bright horn wedge on the forehead."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lightenna"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (196, 200, 208, 255)  # polished silver body
CONFIG["palette"]["Y"] = (232, 236, 242, 255)  # bright band sheen
CONFIG["palette"]["D"] = (150, 154, 164, 255)  # darker silver

# horn tip rising between the antennae
CONFIG["spans"] = {
    **_base["spans"],
    1: [(9, 9), (12, 13), (16, 16)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(1, 12, 13), (2, 11, 14)], "Y"),
]
