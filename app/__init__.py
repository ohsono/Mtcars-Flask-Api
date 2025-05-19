"""
Mtcars Flask API Package

This package provides a Flask-based API for the Mtcars dataset, offering:
- Linear regression model for MPG prediction
- RESTful endpoints for model interaction
- Health checks and model information

Example:
    >>> from app.server import flask_app
    >>> app = flask_app()
    >>> app.run()
"""

__version__ = '1.0.0'
__author__ = 'Hochan Son'

# Import core components
from .model import MtcarsModel
from .server import flask_app

# Define what should be imported with "from app import *"
__all__ = ['MtcarsModel', 'flask_app']
