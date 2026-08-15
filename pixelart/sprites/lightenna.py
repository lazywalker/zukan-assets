"""Lightenna, neopteron. The mirror beetle: vespoid's frame in polished
silver plating with a sharp horn."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lightenna"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (196, 200, 208, 255)  # polished silver body
CONFIG["palette"]["Y"] = (232, 236, 242, 255)  # bright band sheen
CONFIG["palette"]["D"] = (150, 154, 164, 255)  # darker silver

# sharp horn on the head
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(6, 7)],
    5:  [(5, 7), (8, 11)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 6, 7), (5, 5, 6)], "Y"),
]
