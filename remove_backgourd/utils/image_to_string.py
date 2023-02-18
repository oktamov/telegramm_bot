import requests
import json
from PIL import Image
from pytesseract import pytesseract

url = "https://ocr-extract-text.p.rapidapi.com/ocr"
headers = {
    "X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
    "X-RapidAPI-Host": "ocr-extract-text.p.rapidapi.com"
}


# test payload


async def get_text(img_url):
    querystring = {'url': img_url}
    response = requests.request("GET", url, headers=headers, params=querystring)

    img_link = response.json()['text']

    return img_link




async def get_textt(img_url):
    text = pytesseract.image_to_string(Image.open(img_url))

    return text

