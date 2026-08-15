"""Black Gravios, gravios subspecies. Charcoal plating over the stone tank
frame with a faint blue chest sheen."""
from gravios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "black-gravios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (78, 74, 80, 255)     # charcoal plate
CONFIG["palette"]["D"] = (56, 52, 60, 255)     # darker charcoal
CONFIG["palette"]["C"] = (120, 124, 142, 255)  # blue-grey chest

# fire breath: the mouth notch taller and deeper than the parent's
CONFIG["spans"] = {
    **_base["spans"],
    12: [(4, 27)],
    13: [(4, 27)],
    14: [(4, 27)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # ember glow around the gaping mouth
    ("runs", [(12, 4, 7), (13, 4, 7), (14, 4, 7)], "C", "G"),
]
