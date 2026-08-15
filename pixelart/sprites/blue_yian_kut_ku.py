"""Blue Yian Kut-Ku, kut-ku subspecies. Blue scales and a wilder frill:
the ear-frill flares one row taller and two columns wider than the pink
variant's, crest tips over the head."""
from yian_kut_ku import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blue-yian-kut-ku"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (110, 120, 195, 255)  # blue scales
CONFIG["palette"]["S"] = (72, 82, 150, 255)    # dark blue spots / shade

# wilder frill: raised top edge, wider flare
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(9, 15)],
    3:  [(6, 8), (9, 16)],
    4:  [(4, 9), (8, 17)],
    5:  [(2, 9), (7, 17)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # cream over the enlarged frill edges
    ("runs", [(2, 9, 15), (3, 15, 16), (4, 16, 17), (5, 16, 17)], "C"),
]
