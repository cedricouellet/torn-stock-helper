from flask import jsonify
from stock_api.home import home

@home.route('/')
def index():
    data = {
        'message': 'Welcome to Torn Stock Helper API!',
        'routes': [
            {
                'title': 'Stocks',
                'endpoints': [
                    { 'location': '/api/stocks', 'name': 'Get all Stocks', 'url_params': [], 'body_params': [], 'headers': [], 'methods': ['GET'] },
                    { 'location': '/api/stocks/{id}', 'name': 'Get Stock details', 'url_params': [], 'body_params': [], 'headers': [], 'methods': ['GET'] }
                ]
            },
            {
                'title': 'Snapshots',
                'endpoints': [
                    { 'location': '/api/snapshots', 'name': 'Get all Snapshots', 'url_params': [{'name': 'stock_id', 'type': 'integer'}], 'body_params': [], 'headers': [], 'methods': ['GET'] },
                    { 'location': '/api/snapshots/{id}', 'name': 'Get Snapshot details', 'url_params': [], 'body_params': [], 'headers': [], 'methods': ['GET']}
                ]
            },
            {
                'title': 'Predictions',
                'endpoints': [
                    { 'location': '/api/predictions', 'name': 'Get all Predictions', 'url_params': [{'name': 'stock_id', 'type': 'integer'}], 'body_params': [], 'headers': [], 'methods': ['GET'] },
                    { 'location': '/api/predictions/{id}', 'name': 'Get Prediction details', 'url_params': [], 'body_params': [], 'headers': [], 'methods': ['GET']}
                ]
            }
        ]
    }

    return jsonify(data)