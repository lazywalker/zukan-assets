"""Guardian Fulgur Anjanath, fulgur-anjanath variant. The constructed
storm: milky white hide over the fulgur frame with an amber sail glow."""
from fulgur_anjanath import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "guardian-fulgur-anjanath"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (218, 216, 210, 255)  # milky white hide
CONFIG["palette"]["p"] = (184, 182, 176, 255)  # darker fur
CONFIG["palette"]["G"] = (236, 178, 88, 255)   # amber sail glow
CONFIG["palette"]["O"] = (216, 150, 70, 255)   # warm zigzag
