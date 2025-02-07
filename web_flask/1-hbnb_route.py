#!/usr/bin/python3
"""Script for start flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return Messenges"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    """Return Messenges"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
