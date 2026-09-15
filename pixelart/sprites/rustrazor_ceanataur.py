"""Rustrazor Ceanataur, ceanataur deviant. The rust saw: rust-red shell
over the shogun frame, the blade cutting edges lined with pale saw
teeth."""
from shogun_ceanataur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rustrazor-ceanataur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 84, 54, 255)    # rust-red shell
CONFIG["palette"]["D"] = (112, 60, 38, 255)    # darker rust

# saw teeth islands on each blade cutting edge
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(2, 10), (11, 11), (28, 28), (29, 37)],
    9:  [(4, 10), (11, 11), (17, 22), (28, 28), (29, 35)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("put", 6, 11, "W"),
    ("put", 9, 11, "W"),
    ("put", 6, 28, "W"),
    ("put", 9, 28, "W"),
]
