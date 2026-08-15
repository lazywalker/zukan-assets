"""Onimusha, fanged beast. The ogre fist: goss-harag's yeti frame in demon
red with bone-tipped clubs and a horned face."""
from goss_harag import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "onimusha"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (188, 78, 56, 255)    # demon red fur
CONFIG["palette"]["D"] = (146, 56, 42, 255)    # darker red
CONFIG["palette"]["N"] = (56, 36, 34, 255)     # dark face
CONFIG["palette"]["I"] = (238, 226, 202, 255)  # bone club tips
CONFIG["palette"]["Y"] = (232, 176, 66, 255)   # yellow eyes

# face horns
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(5, 6), (10, 11)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(2, 5, 6), (2, 10, 11)], "I"),
]
