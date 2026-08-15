"""Swordmaster Shogun Ceanataur, shogun-ceanataur variant. The dual blade
master: the scissor claw grown into a longer katana edge with a red grip
band, over the shogun frame in darker steel."""
from shogun_ceanataur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "swordmaster-shogun-ceanataur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (72, 88, 118, 255)    # darker steel shell
CONFIG["palette"]["D"] = (48, 60, 88, 255)     # darker blade
CONFIG["palette"]["G"] = (150, 152, 146, 255)  # grey body
CONFIG["palette"]["R"] = (188, 62, 52, 255)    # red grip band

# katana blade: upper pincer extended one row higher
CONFIG["spans"] = {
    **_base["spans"],
    15: [(1, 11), (11, 31)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # red grip band on the blade
    ("runs", [(16, 3, 5)], "R"),
]
