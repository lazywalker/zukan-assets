"""Versa Pietru, elder dragon. The dark twin: makili-pietru's frame in
black-violet with a violet-tipped crest."""
from makili_pietru import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "versa-pietru"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (72, 60, 88, 255)     # black-violet body
CONFIG["palette"]["D"] = (52, 42, 64, 255)     # darker violet
CONFIG["palette"]["T"] = (150, 104, 190, 255)  # violet crest
CONFIG["palette"]["G"] = (188, 140, 226, 255)  # violet rune marks
