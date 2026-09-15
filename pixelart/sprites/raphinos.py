"""Raphinos, wingdrake. The jungle snapper: mernos' glide frame in grey
plumage with a green wing sheen and a long dark beak."""
from mernos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "raphinos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (150, 152, 146, 255)  # grey plumage
CONFIG["palette"]["D"] = (116, 118, 112, 255)  # darker grey
CONFIG["palette"]["B"] = (110, 140, 120, 255)  # green wing

CONFIG["fills"] = list(_base["fills"]) + [
    # long dark beak running down from the head
    ("runs", [(8, 13, 14), (9, 13, 14), (10, 13, 14), (11, 13, 14),
              (12, 13, 14)], "E", "C"),
]
