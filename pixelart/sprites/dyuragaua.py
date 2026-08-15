"""Dyuragaua, flying wyvern. The ice hammer: gigginox's cave stalker frame
in frost white with a hammer-shaped head club."""
from gigginox import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dyuragaua"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (204, 218, 234, 255)  # frost white body
CONFIG["palette"]["D"] = (150, 170, 194, 255)  # darker ice
CONFIG["palette"]["C"] = (232, 240, 248, 255)  # bright crest

# hammer head club widened, ice crest spikes on its crown
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(3, 4), (7, 8)],
    4:  [(2, 10)],
    5:  [(1, 12)],
    6:  [(1, 12), (11, 15)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the crest spikes glow bright
    ("runs", [(3, 3, 4), (3, 7, 8)], "C"),
]
