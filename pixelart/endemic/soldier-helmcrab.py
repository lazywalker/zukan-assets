"""Endemic life: soldier-helmcrab.
Derived from the archetype base; palette carries the species identity."""
from _crab import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "soldier-helmcrab"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 90, 60, 255)
CONFIG["palette"]["D"] = (104, 64, 42, 255)
CONFIG["palette"]["C"] = (206, 160, 120, 255)

# structural patch over the archetype
CONFIG["spans"] = {
    **_base["spans"],
    6: [(12, 13), (16, 17)],
    7: [(10, 19), (14, 15)]
}
