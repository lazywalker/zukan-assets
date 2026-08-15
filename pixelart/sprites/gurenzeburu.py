"""Gurenzeburu, flying wyvern. The crystal boar: bulldrome's charging frame
in deep purple with amber crystal spikes on the back."""
from bulldrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gurenzeburu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (116, 76, 130, 255)   # deep purple hide
CONFIG["palette"]["D"] = (86, 54, 100, 255)    # darker purple
CONFIG["palette"]["M"] = (60, 44, 56, 255)     # dark mane
CONFIG["palette"]["C"] = (238, 190, 96, 255)   # amber crystal spikes

# amber crystal spikes on the back
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(4, 5), (8, 9), (12, 12)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 4, 5), (4, 8, 9), (4, 12, 12)], "C"),
]
