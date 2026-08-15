"""Dahren Mohran, elder dragon. The crimson mountain: jhen's sand ship
frame in a red-rock hide with a broader drill head and coral-gold trim."""
from jhen_mohran import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "dahren-mohran"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (168, 84, 62, 255)    # red-rock hide
CONFIG["palette"]["D"] = (128, 60, 46, 255)    # darker red
CONFIG["palette"]["Y"] = (232, 158, 96, 255)   # coral-gold trim

# broader drill head
CONFIG["spans"] = {
    **_base["spans"],
    7:  [(0, 17), (9, 21)],
    8:  [(0, 18), (8, 24)],
}
