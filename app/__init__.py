import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('THE_CAT_API_KEY')

from flask import Flask, render_template

import requests
import json
from urllib.request import urlopen, Request

from io import BytesIO
from base64 import encodebytes
from PIL import Image

url = "https://api.thecatapi.com/v1/images/search?format=json"
payload = {}
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'API_KEY'
}

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def display_cat():
        return render_template('index.html')

        # from Cat API
        # response = requests.request("GET", url, headers=headers, data=payload)
        # img = json.loads(response.text)[0]["url"]
        # r = Request(img, headers={'User-Agent': 'Mozilla/5.0'})
        # im = urlopen(r).read()
        # img = Image.open(BytesIO(im))
        #
        # return img

        # from static folder
        # img = Image.open(`../static/scottish_fold.jpeg`, mode='r')
        # return img

        # pil_img = Image.open(img, mode='r') #Pillow does not seem to work with actual URLs
        # return pil_img


    return app
