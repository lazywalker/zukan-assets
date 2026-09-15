"""Hornetaur, neopteron. The shell beetle: dark carapace over the vespoid
frame with grey wing shells swept higher than the head."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hornetaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (74, 68, 62, 255)     # dark carapace
CONFIG["palette"]["Y"] = (196, 190, 176, 255)  # pale bands
CONFIG["palette"]["D"] = (52, 48, 44, 255)     # darker shade
CONFIG["palette"]["C"] = (206, 200, 186, 255)  # grey wing shells

# wing shells swept one row higher
CONFIG["spans"] = {
    **_base["spans"],
    1: [(4, 6), (9, 9), (16, 16), (19, 21)],
    2: [(3, 7), (8, 8), (10, 15), (17, 17), (18, 22)],
    3: [(2, 7), (9, 16), (18, 23)],
}
