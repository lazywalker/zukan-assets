"""Cephalos, piscine wyvern pack. The sand shark pup: delex's dart frame
in a sandy green coat with a broader sand fin."""
from delex import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "cephalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["Y"] = (168, 168, 116, 255)  # sandy green body
CONFIG["palette"]["D"] = (128, 128, 86, 255)   # darker sand
CONFIG["palette"]["R"] = (200, 184, 128, 255)  # pale sand fin
CONFIG["palette"]["C"] = (212, 204, 158, 255)  # pale belly

# broader sand fin
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(7, 10), (13, 16)],
    5:  [(5, 11), (12, 17)],
}
