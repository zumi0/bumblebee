import re
from latlon import *

def SHAPE_TEXT(text):
    time = re.search(r"[0-9]+:[0-9]+", text).group(0)
    direction = re.search(r"([0-9]+)。*[一-龥]+", text).group(1)
    # ido
    fake_lat = MAKE_LATLON(re.search(r"北緯\s*(\d{2}).?(\d+)\'(\d*?)\"", text).group(1),
                           re.search(r"北緯\s*(\d{2}).?(\d+)\'(\d*?)\"", text).group(2),
                           re.search(r"北緯\s*(\d{2}).?(\d+)\'(\d*?)\"", text).group(3))
    # keido
    fake_lon = MAKE_LATLON(re.search(r"東経\s*(\d{3}).?(\d+)\'(\d*?)\"", text).group(1),
                           re.search(r"東経\s*(\d{3}).?(\d+)\'(\d*?)\"", text).group(2),
                           re.search(r"東経\s*(\d{3}).?(\d+)\'(\d*?)\"", text).group(3))
    lat = CONVERT_WGS(fake_lat,fake_lon)[0]
    lon = CONVERT_WGS(fake_lat,fake_lon)[1]
    return [time, direction, lat, lon]
