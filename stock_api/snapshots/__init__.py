from flask import Blueprint

snapshots = Blueprint('snapshots', __name__)

from stock_api.snapshots import routes