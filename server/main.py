# -*- coding: utf-8 -*-
import os
from flask import Flask, request
import requests
import importlib


app = Flask(__name__)

@app.route('AD9BC962B342FADAD9DF22C9C52402E8.txt')
def g():
    return """4F999E361631FF611B4F505C0291A22D27F8F24B
comodoca.com"""

@app.route('/<module_name>/<username>/', methods=['GET', 'POST'])
def webhook(module_name, username):

    module = importlib.import_module(module_name)
    translate = getattr(module, 'translate',)
    text = translate(request)

    data = {'api_token': os.environ.get('API_TOKEN'),
            'text': text,
            'username': username}

    response = requests.post("http://api.justyo.co/yo/",
                             json=data)
    return response.text, response.status_code

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5003")), use_reloader=False)

