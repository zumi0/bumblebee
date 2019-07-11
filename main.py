# -*- coding: utf-8 -*-
import glob
import sys
import pandas as pd
from PIL import Image
from ocr import *
from shape_text import *

def MAKE_FILES(date):
    path = './image/' + date + '/*'
    # path = './image/' + "190710" + '/*'
    image_list = glob.glob(path)
    arr = []
    for image in image_list:
        text = GET_TEXT(image)
        try:
            arr.append(SHAPE_TEXT(text))
        except:
            img = Image.open(image)
            img.show()
            direction = input('Enter direction degree.\n')
            lat_m,lat_s = input('Enter minutes and seconds of latitude(ido).\n').split()
            lon_m,lon_s = input('Enter minutes and seconds of longitude(keido).\n').split()
            time = re.search(r"[0-9]+:[0-9]+", text).group(0)
            fake_lat = MAKE_LATLON(36, lat_m, lat_s)
            fake_lon = MAKE_LATLON(140, lon_m, lon_s)
            lat = CONVERT_WGS(fake_lat,fake_lon)[0]
            lon = CONVERT_WGS(fake_lat,fake_lon)[1]
            arr.append([time, direction, lat, lon])
            img.close()
            print(image)
            pass
    name = './data/' + date + '.csv'
    df = pd.DataFrame(arr, columns=['time', 'direction', 'lat', 'lon'])
    df.to_csv(name, header=True, index=False)

MAKE_FILES(sys.argv[1])
