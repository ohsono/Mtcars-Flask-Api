#!/bin/python3
from flask import Blueprint, request, jsonify
from .model import MtcarsModel
import numpy as np
import pandas as pd
from flask import Flask

def flask_app():
    app = Flask(__name__)
    
    # Initialize model
    model = MtcarsModel()
    model._load_data()
    model._fit()

    @app.route('/', methods=['GET'])
    def server_is_up():
        # print("success")
        return 'everything looks good! :)   \n \n'

    @app.route('/health', methods=['GET'])
    def health():
        """Health check endpoint"""
        return jsonify({
            'status': 'healthy',
            'code': 200,
            'model_features': model._features,
            'model_status': 'trained' if model._is_trained else 'not trained'
        })

    @app.route('/predict', methods=['POST'])
    def predict_mpg():
        """
        Predict mpg using MtcarsModel
        """
        json_data = request.get_json()

        for feature in model._features:
            if feature not in json_data:
                return jsonify({'error': f'Missing required feature: {feature}'}), 400

        input = pd.DataFrame([json_data])
        prediction = model._predict(input)
        
        return jsonify({
            'predicted_mpg': float(prediction[0]),
            'features_used': model._features
        })

    @app.route('/model/info', methods=['GET'])
    def model_info():
        """
        Return model information
        """
        if not model._is_trained:
            return jsonify({'error': 'Model not trained yet'}), 500
        
        # Defensive: check for None values
        if model._r_squared is None or model._rmse is None:
            return jsonify({'error': 'Model statistics not available'}), 500
        
        return jsonify({
            'coefficients': {feature: float(coef) for feature, coef in zip(model._features, model._model.coef_)},
            'intercept': float(model._model.intercept_),
            'r_squared': float(model._r_squared),
            'rmse': float(model._rmse),
            'sample_size': int(model._sample_size)
        })

    return app

    @app.route('/retrain', methods=['GET'])
    def retrain():
        """
        Retrain the model as the input coming into the system
        """
        return