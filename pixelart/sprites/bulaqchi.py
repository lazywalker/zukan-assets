"""Bulaqchi, neopteron. The pale hopper: vespoid's frame in a sandy grey
coat with shorter wings."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bulaqchi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (172, 160, 140, 255)  # sandy coat
CONFIG["palette"]["Y"] = (206, 194, 172, 255)  # pale bands
CONFIG["palette"]["D"] = (136, 124, 106, 255)  # darker shade

# shorter wings
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(6, 13), (13, 14)],
    6:  [(5, 14), (12, 16)],
    7:  [(4, 14), (11, 17)],
    8:  [(4, 14), (10, 18)],
}
