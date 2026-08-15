"""Melynx, lynian. The shadow cat: felyne's frame in black fur with a
white muzzle and belly, and a green bauble eye."""
from felyne import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "melynx"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (64, 60, 66, 255)     # black fur
CONFIG["palette"]["D"] = (44, 40, 48, 255)     # darker fur
CONFIG["palette"]["R"] = (110, 190, 110, 255)  # green nose bauble
