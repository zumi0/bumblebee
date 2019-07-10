import glob
import sys
import pandas as pd
from ocr import *
from shape_text import *

def MAKE_FILES(date):
    path = './image/' + date + '/*'
    # path = './image/' + "190710" + '/*'
    image_list = glob.glob(path)
    arr = []
    for image in image_list:
        text = GET_TEXT(image)
        arr.append(SHAPE_TEXT(text))
    name = './data/' + date + '.csv'
    df = pd.DataFrame(arr, columns=['time', 'direction', 'lat', 'lon'])
    df.to_csv(name, header=True, index=False)

MAKE_FILES(sys.argv[1])
