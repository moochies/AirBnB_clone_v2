#!/usr/bin/python3
"""
    a module that implements a flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        A function that return the home page when you hit / route
    """
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        A function that displays  HBNB when you hit /hbnb route
    """
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """
    A function that displays string  passed
    on the url when you hit /c/ route
    """
    string = text.replace("_", " ")
    return f'C {string}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    A function that displays a string  passed
    on the url when you hit /python/ route
    """
    string = text.replace("_", " ")
    return f'Python {string}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    A function that displays a number  passed
    on the url when you hit /number/<n> route
    """
    # if type(n) == int:
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
