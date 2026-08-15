"""Apex Arzuros, arzuros apex. The scarred heavyweight: darker bruised fur
over the honey bear frame, pale scar slashes across the shoulder, and a
bigger fish-bone catch in the mouth."""
from arzuros import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-arzuros"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (128, 104, 84, 255)   # bruised dark fur
CONFIG["palette"]["D"] = (98, 78, 62, 255)     # darker fur

# scar slashes across the shoulder
CONFIG["spans"] = {
    **_base["spans"],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # pale scar slashes
    ("runs", [(10, 16, 17), (11, 18, 19), (12, 17, 18)], "W", "D"),
    # bulked shoulders
    ("runs", [(9, 16, 22), (10, 16, 22)], "D", "F"),
]
