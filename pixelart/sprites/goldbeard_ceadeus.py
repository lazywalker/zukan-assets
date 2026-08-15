"""Goldbeard Ceadeus, ceadeus variant. The gilded sea wolf: ceadeus' frame
in a deeper sea-green with the horn grown into a full gold crown."""
from ceadeus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "goldbeard-ceadeus"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (128, 156, 142, 255)  # deeper sea-green hide
CONFIG["palette"]["D"] = (98, 124, 110, 255)   # darker green
CONFIG["palette"]["Y"] = (238, 200, 80, 255)   # full gold crown

# horn crown grown: extra gold spikes on the brow
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(2, 9), (10, 11)],
    5:  [(1, 11), (9, 14)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 10, 11), (5, 13, 14)], "Y"),
]
