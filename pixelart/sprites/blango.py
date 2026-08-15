"""Blango, fanged beast. The blue pack runner: blangonga's baboon frame in
a blue-grey coat, whiskers and tusks gone, mane tufts kept."""
from blangonga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blango"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (148, 156, 176, 255)  # blue-grey fur
CONFIG["palette"]["D"] = (114, 122, 142, 255)  # darker fur
CONFIG["palette"]["V"] = (90, 78, 116, 255)    # purple face
CONFIG["palette"]["R"] = (148, 156, 176, 255)  # whiskers gone (coat)

# whiskers dropped, head rounded
CONFIG["spans"] = {
    **_base["spans"],
    11: [(0, 15), (6, 25)],
    12: [(0, 15), (7, 26)],
}
