"""Silverwind Nargacuga, nargacuga deviant. The silver storm: steel-blue
fur over the stealth panther frame, and a second silver blade line on the
tail."""
from nargacuga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "silverwind-nargacuga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (88, 96, 118, 255)    # steel-blue fur
CONFIG["palette"]["D"] = (64, 70, 90, 255)     # darker blue
CONFIG["palette"]["B"] = (108, 116, 142, 255)  # blue wing-blades
CONFIG["palette"]["S"] = (238, 240, 248, 255)  # bright silver edge

CONFIG["fills"] = list(_base["fills"]) + [
    # second silver line along the tail top
    ("runs", [(10, 29, 32), (11, 29, 31), (12, 29, 30)], "S"),
]
