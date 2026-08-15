"""Ruby Basarios, basarios subspecies. Pink-ruby rock over the sleeping
boulder frame."""
from basarios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ruby-basarios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (188, 118, 118, 255)  # ruby rock
CONFIG["palette"]["D"] = (148, 86, 88, 255)    # darker ruby
CONFIG["palette"]["C"] = (228, 176, 172, 255)  # pale pink face
