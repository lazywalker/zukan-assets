"""Dread Baelidae, temnoceran. The widow reaper: nerscylla's hooded frame
in blood red with a bone-pale hood mark."""
from nerscylla import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dread-baelidae"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (172, 62, 54, 255)    # blood red body
CONFIG["palette"]["D"] = (132, 44, 40, 255)    # darker red
CONFIG["palette"]["V"] = (232, 214, 186, 255)  # bone-pale hood
