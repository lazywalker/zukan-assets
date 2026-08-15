"""Abyssal Lagiacrus, lagiacrus subspecies. The black abyss serpent:
charcoal-black scales over the lagiacrus frame, spikes one row taller,
and the belly turned deep red."""
from lagiacrus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "abyssal-lagiacrus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (58, 56, 66, 255)     # charcoal-black scales
CONFIG["palette"]["D"] = (40, 38, 48, 255)     # darker black
CONFIG["palette"]["C"] = (188, 92, 72, 255)    # deep red belly
CONFIG["palette"]["O"] = (228, 108, 60, 255)   # ember dorsal ridge

# spikes one row taller
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(0, 11), (10, 10)],
    5:  [(0, 11), (11, 11), (12, 12)],
    6:  [(0, 11), (12, 12), (14, 14)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 10, 10), (5, 11, 12), (6, 12, 14)], "O"),
]
