"""Endemic life: wintermoon-nettle.
Derived from the archetype base; palette carries the species identity."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wintermoon-nettle"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (110, 150, 190, 255)
CONFIG["palette"]["D"] = (78, 112, 148, 255)
CONFIG["palette"]["C"] = (190, 212, 234, 255)
