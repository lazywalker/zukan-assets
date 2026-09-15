"""Risen Teostra, teostra variant. The flame ascended: hotter red body
over the flaming lion frame with a blazing white-hot mane."""
from teostra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "risen-teostra"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (214, 74, 52, 255)    # hotter red body
CONFIG["palette"]["D"] = (166, 52, 40, 255)    # darker red
CONFIG["palette"]["M"] = (248, 230, 180, 255)  # blazing white-hot mane
CONFIG["palette"]["E"] = (250, 160, 60, 255)   # brighter embers
