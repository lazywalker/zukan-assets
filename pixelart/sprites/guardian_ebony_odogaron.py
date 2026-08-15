"""Guardian Ebony Odogaron, ebony-odogaron variant. The constructed
hound: pale white fur over the ebony frame with an amber glow on the
hackles."""
from ebony_odogaron import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "guardian-ebony-odogaron"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (218, 216, 210, 255)  # pale white fur
CONFIG["palette"]["D"] = (180, 178, 172, 255)  # darker fur
CONFIG["palette"]["W"] = (236, 178, 88, 255)   # amber glow fangs

CONFIG["fills"] = list(_base["fills"]) + [
    # amber glow on the hackles
    ("runs", [(9, 11, 11), (9, 14, 14), (9, 17, 17)], "W", "D"),
]
