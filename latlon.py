def MAKE_LATLON(degree, minutes, seconds):
    return float(degree) + float(minutes) / 60 + float(seconds) / 3600

def CONVERT_WGS(fake_lat,fake_lon):
    lat = fake_lat - fake_lat * 0.00010695 + fake_lon * 0.000017464 + 0.0046017
    lon = fake_lon - fake_lat * 0.000046038 - fake_lon * 0.000083043 + 0.010040
    return [lat,lon]
