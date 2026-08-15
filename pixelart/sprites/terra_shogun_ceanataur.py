"""Terra Shogun Ceanataur, shogun-ceanataur variant. The earth shogun:
soil-brown shell with a golden blade edge over the shogun frame."""
from shogun_ceanataur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "terra-shogun-ceanataur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (128, 100, 68, 255)   # soil-brown shell
CONFIG["palette"]["D"] = (96, 74, 48, 255)     # darker soil
CONFIG["palette"]["G"] = (178, 156, 118, 255)  # tan body
CONFIG["palette"]["W"] = (238, 202, 110, 255)  # golden blade edge
