"""Steel Uragaan, uragaan subspecies. Silver plating over the same rolling
boulder, the chin axe widened past the snout, and ore glints turned pale
silver."""
from uragaan import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "steel-uragaan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (140, 146, 156, 255)  # steel plate body
CONFIG["palette"]["D"] = (104, 110, 122, 255)  # darker steel
CONFIG["palette"]["Y"] = (208, 218, 232, 255)  # pale silver glints

# chin axe widened past the snout tip
CONFIG["spans"] = {
    **_base["spans"],
    14: [(1, 32)],
    15: [(1, 32)],
}
