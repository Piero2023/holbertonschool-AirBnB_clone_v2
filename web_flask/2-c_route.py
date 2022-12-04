#!/usr/bin/python3
"""
Script to start flask web application
"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    return Hello HBNB!
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    return HBNB
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    return message
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
