"""Makili Pietru, elder dragon. The pale fury: a small white elder with a
red-tipped crest and vicious clawed fins."""
from leshen import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "makili-pietru"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (222, 218, 210, 255)  # pale white body
CONFIG["palette"]["D"] = (186, 182, 174, 255)  # shade
CONFIG["palette"]["T"] = (216, 96, 80, 255)    # red-tipped crest
CONFIG["palette"]["G"] = (226, 120, 100, 255)  # red rune marks

# vicious claw fins larger
CONFIG["spans"] = {
    **_base["spans"],
    7:  [(1, 10), (5, 19)],
    8:  [(1, 10), (5, 18)],
}
