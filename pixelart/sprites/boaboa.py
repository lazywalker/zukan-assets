"""Boaboa, lynian. The tall tribal: a taller, robed cat with a leaf cloak
and a staff held upright, on the felyne frame stretched taller."""
from felyne import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "boaboa"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (150, 132, 110, 255)  # tan fur
CONFIG["palette"]["D"] = (114, 100, 82, 255)   # darker fur
CONFIG["palette"]["N"] = (60, 70, 46, 255)     # dark ear tips
CONFIG["palette"]["R"] = (88, 122, 70, 255)    # leaf robe
CONFIG["palette"]["T"] = (146, 116, 78, 255)   # staff wood

# taller frame with a robe hem and staff
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(6, 7), (11, 12)],
    9:  [(2, 18), (18, 19)],
    10: [(2, 16), (17, 19)],
    11: [(2, 16), (17, 19)],
    12: [(3, 16), (17, 19)],
    13: [(4, 16), (17, 19)],
    14: [(5, 15), (17, 19)],
    15: [(6, 14), (17, 19)],
    16: [(7, 13), (17, 19)],
    17: [(7, 12), (17, 19)],
    18: [(7, 11), (17, 19)],
    19: [(7, 10), (17, 19)],
}

CONFIG["fills"] = [
    ("runs", [(2, 6, 7), (2, 11, 12)], "N"),
    ("put", 5, 7, "K"),
    ("put", 5, 12, "K"),
    ("put", 7, 9, "R"),
    # leaf robe down the body
    ("runs", [(10, 3, 15), (11, 2, 15), (12, 3, 15), (13, 4, 15),
              (14, 5, 14), (15, 6, 13), (16, 7, 12), (17, 7, 11),
              (18, 7, 10), (19, 7, 9)], "R"),
    ("runs", [(11, 8, 8), (12, 9, 9), (13, 10, 10), (14, 10, 10)], "D", "R"),
    # staff pole
    ("runs", [(10, 18, 19), (11, 18, 19), (12, 18, 19), (13, 18, 19),
              (14, 18, 19), (15, 18, 19), (16, 18, 19), (17, 18, 19),
              (18, 18, 19), (19, 18, 19)], "T"),
]
