from flask import Blueprint

home = Blueprint('home', __name__)

from stock_api.home import routes