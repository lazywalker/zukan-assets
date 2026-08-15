"""Hornetaur, neopteron. The shell beetle: dark carapace over the vespoid
frame with pale wing shells and no yellow bands."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hornetaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (74, 68, 62, 255)     # dark carapace
CONFIG["palette"]["Y"] = (196, 190, 176, 255)  # pale wing shells
CONFIG["palette"]["D"] = (52, 48, 44, 255)     # darker shade

# wing shells swept higher
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(7, 12), (12, 16)],
    5:  [(6, 13), (12, 17)],
}
