#!/bin/python3
from app.server import flask_app

app = flask_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)