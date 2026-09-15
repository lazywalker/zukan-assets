"""Swordmaster Shogun Ceanataur, shogun-ceanataur variant. The dual blade
master: darker steel shell, both blade pincers extended one row higher,
and a red grip band on each arm."""
from shogun_ceanataur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "swordmaster-shogun-ceanataur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (72, 88, 118, 255)    # darker steel shell
CONFIG["palette"]["D"] = (48, 60, 88, 255)     # darker slate dome
CONFIG["palette"]["Q"] = (12, 66, 156, 255)    # darker blade edge
CONFIG["palette"]["R"] = (188, 62, 52, 255)    # red grip band

# katana blades extended one row higher
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(5, 6), (33, 34)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # red grip bands on the arms
    ("runs", [(13, 6, 7), (13, 32, 33)], "R", "P"),
]
