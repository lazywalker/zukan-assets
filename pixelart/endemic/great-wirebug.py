"""Endemic life: great-wirebug.
Derived from the archetype base; palette carries the species identity."""
from _wirebug import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-wirebug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 90, 150, 255)
CONFIG["palette"]["D"] = (80, 64, 116, 255)
CONFIG["palette"]["G"] = (250, 190, 110, 255)

CONFIG["size"] = (32, 24)

# structural patch over the archetype
CONFIG["spans"] = {
    **_base["spans"],
    10: [(4, 25)],
    11: [(4, 25)],
    12: [(5, 24)],
    13: [(7, 22)],
    14: [(9, 20)],
    15: [(11, 18)],
    8: [(7, 22)],
    9: [(5, 24)]
}
