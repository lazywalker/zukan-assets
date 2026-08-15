"""Raphinos, wingdrake. The jungle snapper: mernos' glide frame in grey
plumage with a green wing sheen and a longer beak."""
from mernos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "raphinos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (150, 152, 146, 255)  # grey plumage
CONFIG["palette"]["D"] = (116, 118, 112, 255)  # darker grey
CONFIG["palette"]["B"] = (110, 140, 120, 255)  # green wing

# longer beak
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(1, 9), (7, 16)],
    6:  [(1, 10), (6, 18)],
}
