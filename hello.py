#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created Time: Thu 16 Feb 2017 12:51:09 PM CST

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
