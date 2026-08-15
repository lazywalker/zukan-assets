"""Endemic life: emperor-hopper.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "emperor-hopper"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 130, 90, 255)
CONFIG["palette"]["D"] = (80, 98, 64, 255)
CONFIG["palette"]["G"] = (230, 200, 100, 255)

# structural patch over the archetype
CONFIG["spans"] = {
    **_base["spans"],
    14: [(5, 11), (12, 18)],
    15: [(5, 5), (8, 8), (11, 11), (14, 14), (17, 17), (20, 20)],
    16: [(6, 7), (12, 13), (17, 18)],
    17: [(7, 7), (13, 13), (18, 18)]
}
