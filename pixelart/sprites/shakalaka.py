"""Shakalaka, lynian. The masked dancer: a felyne-sized biped behind a big
orange grin mask with a spike crest, brandishing a weapon."""
from felyne import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shakalaka"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (222, 178, 128, 255)  # tan fur
CONFIG["palette"]["D"] = (182, 140, 96, 255)   # darker fur
CONFIG["palette"]["N"] = (206, 92, 50, 255)    # orange mask
CONFIG["palette"]["W"] = (246, 242, 230, 255)
CONFIG["palette"]["T"] = (146, 146, 158, 255)  # weapon steel

# spike crest + weapon arm up-right
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(6, 7), (10, 11)],
    2:  [(5, 13)],
    10: [(3, 16), (16, 18)],
    11: [(3, 16), (15, 19)],
    12: [(4, 15), (14, 20)],
    13: [(5, 14), (13, 21)],
    14: [(6, 13), (13, 22)],
}

CONFIG["fills"] = [
    # orange grin mask with white teeth
    ("runs", [(2, 5, 13), (3, 5, 13), (4, 4, 14), (5, 4, 14),
              (6, 4, 15), (7, 4, 15), (8, 4, 15)], "N"),
    ("runs", [(6, 6, 13), (7, 6, 13)], "W"),
    ("runs", [(7, 7, 7), (7, 9, 9), (7, 11, 11)], "N", "W"),
    ("put", 5, 7, "K"),
    ("put", 5, 12, "K"),
    # weapon diagonal up-right
    ("runs", [(11, 16, 19), (12, 15, 20), (13, 14, 21), (14, 13, 22)],
     "T"),
]
