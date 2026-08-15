"""Endemic life: tyrant-hopper.
Derived from the archetype base; palette carries the species identity."""
from _fly import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "tyrant-hopper"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 80, 70, 255)
CONFIG["palette"]["D"] = (112, 56, 50, 255)
CONFIG["palette"]["G"] = (240, 170, 90, 255)

# structural patch over the archetype
CONFIG["spans"] = {
    **_base["spans"],
    14: [(5, 11), (12, 18)],
    15: [(5, 5), (8, 8), (11, 11), (14, 14), (17, 17), (20, 20)],
    16: [(6, 7), (12, 13), (17, 18)],
    17: [(7, 7), (13, 13), (18, 18)]
}
