"""Endemic life: prism-hercudrome.
Derived from the archetype base; palette carries the species identity."""
from _beetle import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "prism-hercudrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (150, 120, 180, 255)
CONFIG["palette"]["D"] = (112, 86, 140, 255)
CONFIG["palette"]["C"] = (222, 200, 245, 255)

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
