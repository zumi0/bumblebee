# -*- coding: utf-8 -*-
import requests
import base64
import json
from API_KEY import *

# endpoint URL
GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='

# APIを呼び、認識結果をjson型で返す
def request_cloud_vison_api(image_base64):
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    req_body = json.dumps({
        'requests': [{
            'image': {
                'content': image_base64.decode('utf-8') # jsonに変換するためにstring型に変換する
            },
            'features': [{
                'type': 'TEXT_DETECTION', # ここを変更することで分析内容を変更できる
                'maxResults': 10,
            }]
        }]
    })
    res = requests.post(api_url, data=req_body)
    return res.json()

# 画像読み込み
def img_to_base64(filepath):
    with open(filepath, 'rb') as img:
        img_byte = img.read()
    return base64.b64encode(img_byte)

def GET_TEXT(img_path):
    img_base64 = img_to_base64(img_path)
    result = request_cloud_vison_api(img_base64)
    text = result["responses"][0]["fullTextAnnotation"]["text"]
    # print(text)
    return text
