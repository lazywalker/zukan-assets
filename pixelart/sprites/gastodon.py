"""Gastodon, herbivore. The golden grazer: aptonoth's long-neck frame in a
brassy gold coat with a darker green stripe."""
from aptonoth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gastodon"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (198, 164, 92, 255)   # brassy gold hide
CONFIG["palette"]["D"] = (158, 128, 68, 255)   # darker gold
CONFIG["palette"]["V"] = (108, 132, 84, 255)   # darker green stripe
