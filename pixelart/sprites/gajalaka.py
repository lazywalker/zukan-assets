"""Gajalaka, lynian. The vexed totem: a grey-furred cat behind a red
totem mask with a jagged grin, hefting a big machete."""
from shakalaka import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gajalaka"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (148, 148, 140, 255)  # grey fur
CONFIG["palette"]["D"] = (114, 114, 106, 255)  # darker fur
CONFIG["palette"]["N"] = (178, 54, 48, 255)    # red totem mask
CONFIG["palette"]["T"] = (96, 104, 118, 255)   # machete steel
CONFIG["palette"]["Y"] = (226, 190, 90, 255)   # yellow mask trim

# machete hefted bigger
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(3, 16), (16, 19)],
    10: [(3, 16), (15, 20)],
    11: [(3, 16), (14, 21)],
    12: [(4, 15), (13, 22)],
    13: [(5, 14), (12, 23)],
    14: [(6, 13), (12, 23)],
}

CONFIG["fills"] = [
    # red totem mask with a jagged yellow grin
    ("runs", [(2, 5, 13), (3, 5, 13), (4, 4, 14), (5, 4, 14),
              (6, 4, 15), (7, 4, 15), (8, 4, 15)], "N"),
    ("runs", [(3, 5, 6), (3, 12, 13)], "Y"),
    ("runs", [(6, 6, 13), (7, 6, 13)], "W"),
    ("runs", [(7, 7, 7), (7, 9, 9), (7, 11, 11)], "N", "W"),
    ("put", 5, 7, "K"),
    ("put", 5, 12, "K"),
    # machete blade
    ("runs", [(10, 16, 20), (11, 15, 21), (12, 14, 22), (13, 13, 23),
              (14, 12, 23)], "T"),
    ("runs", [(13, 20, 23), (14, 20, 23)], "Y", "T"),
]
