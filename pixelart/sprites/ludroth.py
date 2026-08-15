"""Ludroth, leviathan. The pack swimmer: epioth's little frame in a
green-grey coat with a crest ridge and a pale belly."""
from epioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ludroth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (128, 142, 106, 255)  # green-grey scales
CONFIG["palette"]["D"] = (98, 112, 80, 255)    # darker green
CONFIG["palette"]["C"] = (216, 210, 168, 255)  # pale belly

# crest ridge on the head
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(2, 5), (6, 6)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 2, 5), (4, 6, 6)], "D"),
]
