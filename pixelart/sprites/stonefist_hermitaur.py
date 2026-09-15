"""Stonefist Hermitaur, daimyo-hermitaur deviant. The stone hammer: grey
stone shell over the crab daimyo frame, both claws swollen into boulder
fists with knobby stone studs."""
from daimyo_hermitaur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "stonefist-hermitaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (128, 124, 112, 255)  # stone shell
CONFIG["palette"]["D"] = (96, 92, 82, 255)     # darker stone

# boulder fists: claw heads swollen wider
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(2, 8), (29, 35)],
    3:  [(1, 9), (28, 36)],
    4:  [(1, 10), (27, 36)],
    5:  [(0, 10), (16, 21), (27, 37)],
    6:  [(1, 10), (14, 23), (27, 36)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # knobby stone studs on the fists
    ("runs", [(3, 2, 3), (3, 6, 7), (5, 1, 2), (5, 8, 9), (3, 34, 35),
              (3, 30, 31), (5, 36, 37), (5, 28, 29)], "D"),
]
