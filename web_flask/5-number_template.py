#!/usr/bin/python3
"""A script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """Print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_what(text):
    """Print C + text provided"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_what(text='is cool'):
    """Print python + text  default is cool"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_number(n):
    """Print n is a number if n is only int"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """Render html template only if n is integer"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
