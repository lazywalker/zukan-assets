"""Guardian Arkveld, arkveld variant. The constructed chain: milky white
armor with the chain wing and tail threaded by an amber energy line."""
from arkveld import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "guardian-arkveld"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (222, 220, 214, 255)  # milky white armor
CONFIG["palette"]["D"] = (184, 182, 176, 255)  # darker armor
CONFIG["palette"]["N"] = (120, 116, 108, 255)  # pale dark chain
CONFIG["palette"]["C"] = (240, 238, 232, 255)  # brighter chest
CONFIG["palette"]["W"] = (246, 242, 230, 255)  # white stays white
CONFIG["palette"]["V"] = (236, 178, 88, 255)   # amber energy line

CONFIG["fills"] = list(_base["fills"]) + [
    # amber energy threading the chain wing arc
    ("runs", [(4, 14, 15), (5, 15, 17), (6, 16, 18)], "V", "N"),
    # amber on the hook blade and the tail blade tip
    ("put", 7, 25, "V"),
    ("put", 15, 26, "V"),
]
