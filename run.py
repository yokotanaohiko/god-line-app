#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask
app = Flask(__file__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=port)
