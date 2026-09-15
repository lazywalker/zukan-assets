"""Endemic life: gold-hercudrome.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gold-hercudrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (222, 178, 82, 255)
CONFIG["palette"]["D"] = (178, 138, 58, 255)
CONFIG["palette"]["C"] = (246, 224, 150, 255)

# structural patch over the archetype
CONFIG["spans"] = {
    **_base["spans"],
    4: [(15, 20)],
    5: [(14, 21)],
    6: [(9, 13), (17, 22)]
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 15, 20), (5, 14, 21), (6, 17, 22)], "C"),
]
