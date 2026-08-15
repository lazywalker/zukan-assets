"""Green Plesioth, plesioth subspecies. Green scales over the fish wyvern
frame, the dorsal fin split into two blades, cream belly kept."""
from plesioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "green-plesioth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (96, 142, 84, 255)    # green scales
CONFIG["palette"]["D"] = (68, 108, 60, 255)    # darker green
CONFIG["palette"]["C"] = (214, 216, 170, 255)  # pale green belly

# dorsal fin split into two blades
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(25, 26), (29, 30)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(2, 25, 26), (2, 29, 30)], "F"),
]
