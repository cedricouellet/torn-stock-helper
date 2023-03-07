from stock_api.stocks import stocks
from stock_lib.models import Stock
from stock_lib.database import db
from flask import jsonify, Response, request

@stocks.route('/', methods = ['GET'])
def index():
    stocks = db.query(Stock).all()
    return jsonify(Stock.list_json(*stocks))

@stocks.route('/<int:id>', methods = ['GET'])
def details(id: int ) -> Response:
    stock = db.query(Stock).get(id)
    if stock is None:
        return jsonify(None)
    
    return jsonify(stock.json)
