"""Apex Rathalos, rathalos apex. The blackened king: charcoal scales over
the rathalos frame with a burning red chest."""
from rathalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-rathalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (72, 66, 72, 255)     # charcoal scales
CONFIG["palette"]["D"] = (50, 46, 52, 255)     # darker charcoal
CONFIG["palette"]["C"] = (214, 96, 66, 255)    # burning red membrane
