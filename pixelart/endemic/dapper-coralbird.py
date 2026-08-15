"""Endemic life: dapper-coralbird.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dapper-coralbird"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (80, 110, 160, 255)
CONFIG["palette"]["D"] = (56, 80, 122, 255)
CONFIG["palette"]["C"] = (170, 190, 220, 255)
