#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__file__)

@app.route('/')
def hello():
    return 'Hello World'
