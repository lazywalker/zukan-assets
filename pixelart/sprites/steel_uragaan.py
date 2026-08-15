"""Steel Uragaan, uragaan subspecies. Silver plating over the same
rolling boulder, the chin axe pushed forward past the snout, and ore
glints turned pale silver."""
from uragaan import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "steel-uragaan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (140, 146, 156, 255)  # steel plate body
CONFIG["palette"]["D"] = (104, 110, 122, 255)  # darker steel
CONFIG["palette"]["O"] = (208, 218, 232, 255)  # silver ore glints

# chin axe pushed forward past the snout tip
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(0, 29)],
    9:  [(0, 30)],
}
