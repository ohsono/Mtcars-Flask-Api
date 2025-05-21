#!/bin/python3
from app.server import flask_app

app = flask_app()

if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(host='0.0.0.0', port=5001, debug=debug_mode)