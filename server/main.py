# -*- coding: utf-8 -*-
import os
from flask import Flask, request, redirect
import requests
import importlib


app = Flask(__name__)


@app.route('/<module_name>/<username>/', methods=['GET', 'POST'])
def webhook(module_name, username):

    module = importlib.import_module(module_name)
    translate = getattr(module, 'translate',)
    text = translate(request)

    default_token = os.environ.get('API_TOKEN')
    data = {'api_token': os.environ.get(module_name.upper() + '_YO_TOKEN', default_token),
            'text': text,
            'is_push_only': 1,
            'username': username}

    response = requests.post("http://api.justyo.co/yo/",
                             json=data)
    return response.text, response.status_code


@app.route('/', methods=['GET'])
def home():
    return redirect('https://github.com/YoApp/yo-hooks')


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5003")), use_reloader=False)

