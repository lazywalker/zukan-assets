"""Viper Tobi-Kadachi, fanged wyvern subspecies. The venom glider: dark
grey-green fur over the tobi frame, the neck flared into a cobra hood,
and the gliding membrane tinted venom pink."""
from tobi_kadachi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "viper-tobi-kadachi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (120, 126, 112, 255)  # grey-green fur
CONFIG["palette"]["G"] = (86, 92, 80, 255)     # shade
CONFIG["palette"]["N"] = (44, 40, 66, 255)     # dark purple markings
CONFIG["palette"]["P"] = (226, 122, 178, 255)  # venom pink membrane
CONFIG["palette"]["R"] = (232, 120, 180, 255)  # pink eye

# cobra hood: neck flared wide below the head
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(1, 12), (12, 22), (27, 31)],
    9:  [(1, 12), (11, 24), (26, 32)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # venom pink over the flared membrane
    ("runs", [(12, 10, 11), (13, 10, 12), (13, 13, 13), (14, 10, 12),
              (15, 10, 12)], "P", "W"),
]
