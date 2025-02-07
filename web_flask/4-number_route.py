#!/usr/bin/python3
"""Script to start flask web application"""
from flask import Flask, abort
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return messages"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    """Return messages"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def varible_text(text=""):
    """Return messages"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Return messages"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number_int(n):
    """Return messages"""
    if not n.isnumeric():
        abort(404)
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
