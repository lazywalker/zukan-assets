"""Hallowed Jhen Mohran, jhen-mohran variant. The sandstorm temple: paler
sand-crusted hide over the sand ship frame with jade trim."""
from jhen_mohran import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "hallowed-jhen-mohran"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (108, 104, 88, 255)   # sand-crusted hide
CONFIG["palette"]["D"] = (80, 76, 64, 255)     # darker crust
CONFIG["palette"]["Y"] = (156, 186, 148, 255)  # jade trim
