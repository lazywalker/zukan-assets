"""Barnos, wingdrake. The dark roost rat: mernos' glide frame in a dark
red-brown coat with a shorter crest."""
from mernos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "barnos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (138, 88, 70, 255)    # dark red-brown body
CONFIG["palette"]["D"] = (106, 66, 52, 255)    # darker shade
CONFIG["palette"]["B"] = (96, 78, 76, 255)     # dark wing
CONFIG["palette"]["R"] = (180, 110, 66, 255)   # crest

# shorter crest
CONFIG["spans"] = {
    **_base["spans"],
    2:  [],
    3:  [(4, 7), (8, 9)],
}
