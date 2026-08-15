"""Tigerstripe Zamtrios, zamtrios subspecies. Purple hide with dark tiger
stripes over the shark-toad frame, the fin tipped dark."""
from zamtrios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "tigerstripe-zamtrios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (146, 110, 172, 255)  # purple hide
CONFIG["palette"]["D"] = (96, 62, 122, 255)    # dark purple stripes
CONFIG["palette"]["O"] = (216, 130, 176, 255)  # pink fin

CONFIG["fills"] = list(_base["fills"]) + [
    # tiger stripes down the flank
    ("runs", [(11, 15, 16), (12, 17, 18), (13, 16, 17),
              (14, 18, 19), (15, 19, 20)], "D", "B"),
]
