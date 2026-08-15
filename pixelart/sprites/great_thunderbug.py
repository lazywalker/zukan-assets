"""Great Thunderbug, neopteron. The storm bulb: vespoid's frame swollen
into a round glowing blue body with a lightning shimmer, wings tucked."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-thunderbug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (94, 128, 198, 255)   # storm blue body
CONFIG["palette"]["Y"] = (180, 216, 246, 255)  # pale shimmer bands
CONFIG["palette"]["D"] = (64, 92, 156, 255)    # darker blue
CONFIG["palette"]["W"] = (246, 250, 255, 255)  # bright wings

# rounder body: abdomen bulges
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(2, 15), (9, 20)],
    10: [(2, 15), (9, 21)],
    11: [(2, 15), (10, 21)],
    12: [(3, 15), (11, 20)],
}
