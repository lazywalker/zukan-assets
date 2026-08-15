"""Pyre-Rakna-Kadaki, rakna-kadaki variant. The furnace widow: ember red
body and charcoal crown with molten leg tips over the widow frame."""
from rakna_kadaki import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pyre-rakna-kadaki"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["Y"] = (178, 74, 54, 255)    # ember red body
CONFIG["palette"]["D"] = (134, 52, 40, 255)    # darker ember
CONFIG["palette"]["V"] = (52, 40, 44, 255)     # charcoal crown
CONFIG["palette"]["O"] = (240, 142, 60, 255)   # molten legs
