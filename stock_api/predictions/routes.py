from stock_api.predictions import predictions
from stock_lib.models import Prediction
from stock_lib.database import db
from flask import jsonify, Response, request

@predictions.route('/', methods = ['GET'])
def index():
    query = db.query(Prediction)

    arg_stock_id = request.args.get('stock_id')
    if arg_stock_id is not None:
        query = query.filter(Prediction.stock_id == arg_stock_id)

    predictions = query.all()
    return jsonify(Prediction.list_json(*predictions))

@predictions.route('/<int:id>', methods = ['GET'])
def details(id: int ) -> Response:
    prediction = db.query(Prediction).get(id)
    if prediction is None:
        return jsonify(None)
    
    return jsonify(prediction.json)
