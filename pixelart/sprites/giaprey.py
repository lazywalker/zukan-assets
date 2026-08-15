"""Giaprey, small bird wyvern. The blue runner: velocidrome's lunge in
bright blue with a low flat crest."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "giaprey"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (108, 140, 196, 255)  # bright blue scales
CONFIG["palette"]["F"] = (80, 108, 164, 255)   # dark crest
CONFIG["palette"]["C"] = (198, 214, 234, 255)  # pale belly
CONFIG["palette"]["S"] = (70, 96, 148, 255)    # dark spots

# low flat crest only
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(8, 11)],
}
