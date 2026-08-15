"""Stonefist Hermitaur, daimyo-hermitaur deviant. The stone hammer: grey
stone shell over the crab daimyo frame, the near claw swollen into a
boulder fist."""
from daimyo_hermitaur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "stonefist-hermitaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (128, 124, 112, 255)  # stone shell
CONFIG["palette"]["D"] = (96, 92, 82, 255)     # darker stone

# boulder fist: claw mass swollen
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(1, 8), (12, 13), (20, 21)],
    3:  [(0, 9), (11, 14), (19, 22)],
    4:  [(0, 10), (11, 15), (18, 23)],
    5:  [(0, 10), (11, 15), (17, 24)],
}
