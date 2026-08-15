"""Endemic life: puppet-spider.
Derived from the archetype base; palette carries the species identity."""
from _spider import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "puppet-spider"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
