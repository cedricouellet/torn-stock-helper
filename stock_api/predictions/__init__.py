from flask import Blueprint

predictions = Blueprint('predictions', __name__)

from stock_api.predictions import routes