import re
from latlon import *

def SHAPE_TEXT(text):
    time = re.search(r"[0-9]+:[0-9]+", text).group(0)
    direction = re.search(r"([0-9]+).?\s*[一-龥]+", text).group(1)
    # ido
    lat_text = re.search(r"北緯*\s*(\d{2}).?(\d{1,2})\'(\d{1,2})\"", text)
    fake_lat = MAKE_LATLON(lat_text.group(1), lat_text.group(2), lat_text.group(3))
    # keido
    lon_text = re.search(r"東経*\s*(\d{3}).?(\d{1,2})\'(\d{1,2})\"", text)
    fake_lon = MAKE_LATLON(lon_text.group(1), lon_text.group(2), lon_text.group(3))
    lat = CONVERT_WGS(fake_lat,fake_lon)[0]
    lon = CONVERT_WGS(fake_lat,fake_lon)[1]
    return [time, direction, lat, lon]
