"""Noios, wingdrake. The lightning-crest scavenger: mernos' glide frame in
dust brown with two yellow crest horns splitting off the head."""
from mernos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "noios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (168, 148, 118, 255)  # dust brown body
CONFIG["palette"]["D"] = (132, 114, 88, 255)   # darker brown
CONFIG["palette"]["B"] = (188, 172, 140, 255)  # pale wing
CONFIG["palette"]["Y"] = (226, 196, 70, 255)   # yellow crest horns

# two crest horns splitting up
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(1, 10), (12, 13), (14, 15), (17, 26)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 12, 13), (3, 14, 15)], "Y"),
]
