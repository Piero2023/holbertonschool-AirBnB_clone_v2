#!/usr/bin/python3
"""Script to start flask web application"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    return message
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    """
    return message
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def varible_text(text=""):
    """
    return message
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    return message
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number_text(n):
    """
    return messages
    """
    if not n.isnumeric():
        abort(404)
    return "{} is a number".format(n)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """
    return message
    """
    if not n.isnumeric():
        abort(404)
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    return message
    """
    if not n.isnumeric():
        abort(404)
    return render_template('6-number_odd_or_even.html', n=int(n))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
