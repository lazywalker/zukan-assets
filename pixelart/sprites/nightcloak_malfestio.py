"""Nightcloak Malfestio, malfestio variant. The midnight owl: near-black
plumage, teal-glow eyes and collar, ear tufts one row taller."""
from malfestio import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nightcloak-malfestio"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (74, 74, 94, 255)     # midnight plumage
CONFIG["palette"]["D"] = (52, 52, 70, 255)     # darker bars
CONFIG["palette"]["C"] = (150, 158, 168, 255)  # pale belly
CONFIG["palette"]["O"] = (110, 210, 190, 255)  # teal glow collar / eyes
CONFIG["palette"]["N"] = (34, 34, 50, 255)     # black tufts

# ear tufts one row taller
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(5, 6), (12, 13)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(1, 5, 6), (1, 12, 13)], "N"),
]
