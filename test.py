# -*- coding: utf-8 -*-
import glob
import sys
import pandas as pd
from PIL import Image
from ocr import *
from shape_text import *

def TEST(date):
    path = './image/' + date + '/*'
    image_list = glob.glob(path)
    for image in image_list:
        print(image)
        print(GET_TEXT(image))

TEST(sys.argv[1])
