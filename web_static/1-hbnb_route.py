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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
