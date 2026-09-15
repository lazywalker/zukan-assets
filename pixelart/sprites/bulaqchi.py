"""Bulaqchi, neopteron. The pale hopper: vespoid's frame in a sandy grey
coat with shorter, lower-set wings."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bulaqchi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (172, 160, 140, 255)  # sandy coat
CONFIG["palette"]["Y"] = (206, 194, 172, 255)  # pale bands
CONFIG["palette"]["D"] = (136, 124, 106, 255)  # darker shade

# shorter wings starting one row lower
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(8, 8), (10, 15), (17, 17)],
    3:  [(4, 5), (9, 16), (20, 21)],
    4:  [(3, 6), (8, 17), (19, 22)],
    5:  [(3, 6), (8, 17), (19, 22)],
    6:  [(3, 6), (8, 17), (19, 22)],
    7:  [(2, 5), (8, 17), (20, 23)],
    8:  [(2, 5), (8, 17), (20, 23)],
    9:  [(3, 5), (9, 16), (20, 22)],
    10: [(4, 4), (10, 15), (21, 21)],
}
