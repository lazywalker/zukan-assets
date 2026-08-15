"""Blackveil Vaal Hazak, vaal-hazak subspecies. The miasma veil: dead-grey
body over the miasma dragon frame with pale spore clouds rolling off the
fins."""
from vaal_hazak import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blackveil-vaal-hazak"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (110, 112, 104, 255)  # dead-grey body
CONFIG["palette"]["D"] = (82, 84, 78, 255)     # darker grey
CONFIG["palette"]["C"] = (188, 196, 172, 255)  # spore-pale fins
CONFIG["palette"]["R"] = (158, 176, 128, 255)  # pale green glow
