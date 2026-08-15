"""Seething Bazelgeuse, bazelgeuse deviation. The stable bomber: deep
green-black hide over the flying bomber frame, scale clusters glowing hot
orange-red."""
from bazelgeuse import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "seething-bazelgeuse"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (74, 86, 72, 255)     # deep green-black hide
CONFIG["palette"]["D"] = (54, 64, 54, 255)     # darker hide
CONFIG["palette"]["N"] = (40, 42, 56, 255)     # darker pinecone clusters
CONFIG["palette"]["O"] = (240, 96, 48, 255)    # hot orange-red glow
