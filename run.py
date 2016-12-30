#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/.well-known/acme-challenge/<post_id>')
def auth(post_id):
    if post_id == os.environ['LETSENCRYPT_REQUEST']:
        return os.environ['LETSENCRYPT_RESPONSE']

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
