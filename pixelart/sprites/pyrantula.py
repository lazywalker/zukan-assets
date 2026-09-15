"""Pyrantula, temnoceran. The ember tarantula: nerscylla's hooded frame in
burnt orange with a charcoal hood and molten fangs."""
from nerscylla import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pyrantula"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (206, 122, 62, 255)   # burnt orange body
CONFIG["palette"]["D"] = (158, 88, 44, 255)    # darker orange
CONFIG["palette"]["V"] = (66, 52, 50, 255)     # charcoal hood
CONFIG["palette"]["R"] = (244, 160, 70, 255)   # molten fangs
CONFIG["palette"]["W"] = (250, 220, 160, 255)  # pale abdomen mark
