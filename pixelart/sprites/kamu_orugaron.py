"""Kamu Orugaron, fanged beast. The dusk wolf: lunagaron's wolf frame in a
dark charcoal coat with a straighter, fiercer mane."""
from lunagaron import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "kamu-orugaron"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (86, 82, 90, 255)     # dusk charcoal fur
CONFIG["palette"]["D"] = (62, 58, 66, 255)     # darker fur
CONFIG["palette"]["M"] = (40, 38, 44, 255)     # darker mane
CONFIG["palette"]["V"] = (222, 178, 82, 255)   # gold claws

# fiercer mane: crest spikes on the neck
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(1, 5), (6, 7)],
    4:  [(0, 6), (6, 7), (7, 8)],
}
