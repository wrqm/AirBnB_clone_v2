#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """url- 0.0.0.0/5000: display “Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """url-0.0.0.0/5000/hbnb: display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """url- 0.0.0.0/5000/c/<text>: display “C ” y value of the text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text=None):
    """"url- 0.0.0.0/5000/python/(<text>): display “Python" y text"""

    if text is None:
        text = 'is cool'
    return 'Python {}'.format(text.replace('_', ' '))


"""web application must be listening on 0.0.0.0, port 5000"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
