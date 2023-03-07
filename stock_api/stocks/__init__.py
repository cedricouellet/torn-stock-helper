from flask import Blueprint

stocks = Blueprint('stocks', __name__)

from stock_api.stocks import routes
