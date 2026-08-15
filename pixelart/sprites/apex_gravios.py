"""Apex Gravios, gravios apex. The scarred tank: darker battle hide over
the gravios frame with pale scar slashes across the shell."""
from gravios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-gravios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (116, 108, 96, 255)   # battle-scarred hide
CONFIG["palette"]["D"] = (86, 80, 70, 255)     # darker shade

# battle damage: a chunk blown out of the dome top
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(11, 13), (15, 16)],
    4:  [(9, 11), (13, 18), (21, 22)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # pale scar slashes
    ("runs", [(10, 18, 19), (11, 20, 21), (12, 19, 20)], "C", "G"),
]
