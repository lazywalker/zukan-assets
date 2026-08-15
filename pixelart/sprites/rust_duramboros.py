"""Rust Duramboros, duramboros subspecies. Rust-red hide over the same
hunchback frame, the hump cap weathered pale, and two extra spikes
breaking off the hump top."""
from duramboros import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rust-duramboros"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (152, 92, 58, 255)    # rust-red hide
CONFIG["palette"]["D"] = (114, 66, 42, 255)    # darker rust
CONFIG["palette"]["C"] = (214, 186, 158, 255)  # weathered hump cap
CONFIG["palette"]["M"] = (168, 120, 84, 255)   # dry moss patches

# spikes breaking off the hump top
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(15, 15), (18, 18)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(1, 15, 15), (1, 18, 18)], "D"),
]
