#!/usr/bin/python3
"""
starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask("__name__")

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
