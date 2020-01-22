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


"""web application must be listening on 0.0.0.0, port 5000"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
